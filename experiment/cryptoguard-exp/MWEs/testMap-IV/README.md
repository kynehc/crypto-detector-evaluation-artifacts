This is to show the FP of identifiers of value source for constant IV.

```
=======================================
***Violated Rule 10: Found constant IV in code
***Found: "IV" in <com.example.testmap_iv.testIV: java.lang.String encryptWrapper(java.lang.String)>::encryptWrapper.
=======================================
```

"IV" is an identifier to get raw IV (byte array) in a map data structure. Cgd wrongly take this FP.