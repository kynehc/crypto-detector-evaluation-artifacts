This case is to show the FP of constant keys of SecretKeySpec.

```
=======================================
***Violated Rule 3: Used constant keys in code
***Found: Constant "ENC" in <com.example.testorthogonal_secretkeyspec.OperatorUtils: java.security.Key getJceKey(com.example.testorthogonal_secretkeyspec.GenericKey)>::getJceKey:13.
=======================================
```

Cgd set its orthogonal slicing as only 1 and its `HeuristicBasedInstructionSlicer` will report any constants that in the def-use chains of `return` stmt in the last depth of method. Thus, this limitation leads to the "ENC" FP.