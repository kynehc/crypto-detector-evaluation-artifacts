This case is to show the FP of SSLSocket generated from SSLSocketFactory without Hostname verification.

```
=======================================
***Violated Rule 12: Should check HostnameVerification manually
***Didn't manually verify hostname in test in <com.example.testpath_hostnameverifier.TestClass: void test()>::test.
=======================================
```

Cgd simply take final statement in the method body as final slicing result, which leads to this FP. This case just put a null-check before the `verify()` method and cause cgd output the FP.