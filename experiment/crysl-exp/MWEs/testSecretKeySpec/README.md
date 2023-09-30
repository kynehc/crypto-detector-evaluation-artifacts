This case is to show the model false positive of SecretKeySpec required Predicate:

```
Findings in Java Class: com.example.testsecretkeyspec.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		RequiredPredicateError violating CrySL rule for javax.crypto.spec.SecretKeySpec
			First parameter was not properly generated as preparedKeyMaterial
			at statement: specialinvoke r2.<javax.crypto.spec.SecretKeySpec: void <init>(byte[],java.lang.String)>(r4, varReplacer8)
```

The SecretKeySpec object is initialize by a byte array generated from SecureRandom, which is violating the rule for SecretKeySpec. However, the SecretKeySpec object is intended to be initialized by a byte array without necessarily from a existing Key/SecretKey object.
