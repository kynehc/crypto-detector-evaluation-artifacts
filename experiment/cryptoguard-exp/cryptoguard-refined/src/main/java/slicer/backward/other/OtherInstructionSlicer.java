/* Licensed under GPL-3.0 */
package slicer.backward.other;

import analyzer.backward.UnitContainer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import slicer.ValueArraySparseSet;
import slicer.backward.CustomBackwardFlowAnalysis;
import slicer.backward.property.PropertyAnalysisResult;
import soot.ArrayType;
import soot.Unit;
import soot.ValueBox;
import soot.jimple.internal.JInvokeStmt;
import soot.toolkits.graph.DirectedGraph;
import soot.toolkits.scalar.FlowSet;
import util.FieldInitializationInstructionMap;
import util.Utils;

/**
 * OtherInstructionSlicer class.
 *
 * @author CryptoguardTeam
 * @version 03.07.01
 * @since V01.00.00
 */
public class OtherInstructionSlicer extends CustomBackwardFlowAnalysis {

  private FlowSet emptySet;
  private String slicingCriteria;
  private String method;
  private Map<String, List<PropertyAnalysisResult>> propertyUseMap;

  /**
   * Constructor for OtherInstructionSlicer.
   *
   * @param g a {@link soot.toolkits.graph.DirectedGraph} object.
   * @param slicingCriteria a {@link java.lang.String} object.
   * @param method a {@link java.lang.String} object.
   */
  public OtherInstructionSlicer(DirectedGraph g, String slicingCriteria, String method) {
    super(g);
    this.emptySet = new ValueArraySparseSet();
    this.slicingCriteria = slicingCriteria;
    this.method = method;
    this.propertyUseMap = new HashMap<>();
    doAnalysis();
  }

  /** {@inheritDoc} */
  @Override
  protected void flowThrough(Object in, Object node, Object out) {
    FlowSet inSet = (FlowSet) in, outSet = (FlowSet) out;
    Unit currInstruction = (Unit) node;

    if (currInstruction.toString().startsWith(slicingCriteria)) {
      addCurrInstInOutSet(outSet, currInstruction);
      return;
    }

    if (!inSet.isEmpty()) {
      for (Object anInSet : inSet.toList()) {

        UnitContainer insetInstruction = (UnitContainer) anInSet;
        // List<ValueBox> useBoxes = insetInstruction.getUnit().getUseBoxes();
        List<ValueBox> useBoxes = insetInstruction.getUseBoxes();

        outSet.union(inSet);

        for (ValueBox usebox : useBoxes) {

          if ((usebox.getValue().toString().equals("r0")
                  && insetInstruction.getUnit().toString().contains("r0."))
              || (usebox.getValue().toString().equals("this")
                  && insetInstruction.getUnit().toString().contains("this."))) {
            continue;
          }

          if (isInvokeOn(currInstruction, usebox)) {
            addCurrInstInOutSet(outSet, currInstruction);
            return;
          }

          for (ValueBox defbox : currInstruction.getDefBoxes()) {

            if ((defbox.getValue().toString().equals("r0")
                    && currInstruction.toString().startsWith("r0."))
                || (defbox.getValue().toString().equals("this")
                    && currInstruction.toString().startsWith("this."))) {
              continue;
            }

            if (defbox.getValue().equivTo(usebox.getValue())) {
              addCurrInstInOutSet(outSet, currInstruction);
              // fix: remove useBox once def
              insetInstruction.removeUseBox(usebox);
              return;
            } else if (defbox.getValue().toString().contains(usebox.getValue().toString())) {
              // fix: add aditional match for any array variables, e.g., r2[1] or $r2[1].
              if (defbox.getValue().toString().matches("\\$?[a-z][0-9]+\\[.*\\]")) {
                String defVarName = defbox.getValue().toString().split("\\[")[0];
                if (defVarName.equals(usebox.getValue().toString())
                    && usebox.getValue().getType() instanceof ArrayType) {
                  addCurrInstInOutSet(outSet, currInstruction);
                  return;
                }
              }
            }
          }
        }
      }
    }
  }

  private void addCurrInstInOutSet(FlowSet outSet, Unit currInstruction) {

    for (ValueBox usebox : currInstruction.getUseBoxes()) {
      if (propertyUseMap.get(usebox.getValue().toString()) == null) {

        List<PropertyAnalysisResult> specialInitInsts = null;
        // fix: correct field match
        if (usebox.getValue().toString().matches("\\$?r[0-9]+\\.<[^\\>]+>")) {
          Matcher matches = Utils.fieldPattern.matcher(usebox.getValue().toString());
          if (matches.find()) {
            specialInitInsts =
                FieldInitializationInstructionMap.getInitInstructions(matches.group(0));
          }
        } else if (usebox.getValue().toString().startsWith("this.")) {
          specialInitInsts =
              FieldInitializationInstructionMap.getInitInstructions(
                  usebox.getValue().toString().substring(5));
        } else {
          specialInitInsts =
              FieldInitializationInstructionMap.getInitInstructions(usebox.getValue().toString());
        }

        if (specialInitInsts != null) {
          propertyUseMap.put(usebox.getValue().toString(), specialInitInsts);
        }
      }
    }

    UnitContainer currUnitContainer = new UnitContainer();
    currUnitContainer.setUnit(currInstruction);
    currUnitContainer.setMethod(method);

    outSet.add(currUnitContainer);
  }

  private boolean isInvokeOn(Unit currInstruction, ValueBox usebox) {
    return currInstruction instanceof JInvokeStmt
        && currInstruction.toString().contains(usebox.getValue().toString() + ".<");
  }

  /** {@inheritDoc} */
  @Override
  protected Object newInitialFlow() {
    return emptySet.clone();
  }

  /** {@inheritDoc} */
  @Override
  protected Object entryInitialFlow() {
    return emptySet.clone();
  }

  /** {@inheritDoc} */
  @Override
  protected void merge(Object in1, Object in2, Object out) {
    FlowSet inSet1 = (FlowSet) in1, inSet2 = (FlowSet) in2, outSet = (FlowSet) out;

    // deal with merge point: union usebox of same unitcontainer in all branches
    ArrayList inSetList1 = new ArrayList<>(inSet1.toList());
    ArrayList inSetList2 = new ArrayList<>(inSet2.toList());
    int len = inSet1.size() <= inSet2.size() ? inSet1.size() : inSet2.size();
    for (int i = 0; i < len; i++) {
      UnitContainer uc1 = (UnitContainer) inSetList1.get(i);
      UnitContainer uc2 = (UnitContainer) inSetList2.get(i);

      // same UnitContainer but may with different useBoxes
      if (uc1.toString().equals(uc2.toString())) {
        List<ValueBox> unionUseBoxes = unionList(uc1.getUseBoxes(), uc2.getUseBoxes());
        uc1.setUseBoxes(unionUseBoxes);
      }
    }

    inSet1.union(inSet2, outSet);
  }

  /** {@inheritDoc} */
  @Override
  protected void copy(Object source, Object dest) {
    FlowSet srcSet = (FlowSet) source, destSet = (FlowSet) dest;
    srcSet.copy(destSet);
  }

  /**
   * Getter for the field <code>propertyUseMap</code>.
   *
   * @return a {@link java.util.Map} object.
   */
  public Map<String, List<PropertyAnalysisResult>> getPropertyUseMap() {
    return propertyUseMap;
  }
}
