This case is to show the RequiredPredicateError false positive in IvParameterSpec caused by incorrectly handle try-catch nest.

```
Findings in Java Class: com.example.testiv.TestIV

	 in Method: void test()
		RequiredPredicateError violating CrySL rule for javax.crypto.spec.IvParameterSpec
			First parameter was not properly generated as randomized
			at statement: specialinvoke r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>(r3)
```

The wrong handling of the statements in try-catch block makes typestate analysis miss follow-up call sequence (statements) as analysis results.
