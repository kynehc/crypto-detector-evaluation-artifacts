This case is to show the FP of constant keys of SecretKeySpec.

```
=======================================
***Violated Rule 3: Used constant keys in code
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:69.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:62.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:63.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:68.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:64.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:67.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:65.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:66.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:71.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "97" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "112" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch:70.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
***Found: Constant "115" in <com.example.teststringmatch_secretkeyspec.StringMatch: void StringMatch()>::StringMatch.
=======================================
```

Cgd wrongly use `toString().contains()` to determine if the definition of an array variable match use of array variables in def-use analysis. Thus, this leads to exaggerated matching in some cases. Here, we deliberately triggered such FP with allocating lots of unrelated byte array. In experiment, we found real-world cases of this FP.