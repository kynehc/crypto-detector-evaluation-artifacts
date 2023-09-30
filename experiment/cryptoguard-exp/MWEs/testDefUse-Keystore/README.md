This case is to show the FP of predictable KeyStore password.

```
=======================================
***Violated Rule 14: Used Predictable KeyStore Password
***Found: "jks" in <java.security.KeyStore: java.lang.String getDefaultType()>::getDefaultType:971.
=======================================
```

Cgd does not kill any use of variables in slicing and thus, the variable reassignment would lead to this FP due to broken def-use chains.