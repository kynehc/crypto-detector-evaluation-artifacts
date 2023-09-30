This case is to show the RequiredPredicateError false positive in IvParameterSpec caused by ThreadLocal.

```
Findings in Java Class: com.example.testiv2.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		RequiredPredicateError violating CrySL rule for javax.crypto.spec.IvParameterSpec
			First parameter was not properly generated as randomized
			at statement: specialinvoke r2.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r3)
```

The Random class is just a simple warpper of SecureRandom through ThreadLocal class. However, Crysl hv problem to construct the correct call graph when using ThreadLocal class to initilize the Random class, which results in this FP case.
