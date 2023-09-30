/* Licensed under GPL-3.0 */
package slicer.backward;

/*-
 * #%L
 * Soot - a J*va Optimization Framework
 * %%
 * Copyright (C) 1997 - 1999 Raja Vallee-Rai
 * %%
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation, either version 2.1 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Lesser Public License for more details.
 *
 * You should have received a copy of the GNU General Lesser Public
 * License along with this program.  If not, see
 * <http://www.gnu.org/licenses/lgpl-2.1.html>.
 * #L%
 */

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import soot.toolkits.graph.DirectedGraph;

/**
 * Abstract class that provides the fixed point iteration functionality required by all
 * BackwardFlowAnalyses.
 */
public abstract class CustomBackwardFlowAnalysis<N, A> extends CustomFlowAnalysis<N, A> {
  /** Construct the analysis from a DirectedGraph representation of a Body. */
  public CustomBackwardFlowAnalysis(DirectedGraph<N> graph) {
    super(graph);
  }

  /**
   * Returns <code>false</code>
   *
   * @return false
   */
  @Override
  protected boolean isForward() {
    return false;
  }

  @Override
  protected void doAnalysis() {
    doAnalysis(
        GraphView.BACKWARD, InteractionFlowHandler.BACKWARD, unitToAfterFlow, unitToBeforeFlow);

    // soot.Timers.v().totalFlowNodes += graph.size();
    // soot.Timers.v().totalFlowComputations += numComputations;
  }

  protected <T> List<T> unionList(List<T> list1, List<T> list2) {
    Set<T> set = new HashSet<T>();
    set.addAll(list1);
    set.addAll(list2);

    return new ArrayList<T>(set);
  }
}
