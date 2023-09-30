This case is to show the predicate error false positive as below:

```
Findings in Java Class: com.example.testalgoparam.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		RequiredPredicateError violating CrySL rule for javax.crypto.Cipher
			Third parameter was not properly generated as preparedAlg
			at statement: virtualinvoke $r6.<javax.crypto.Cipher: void init(int,java.security.Key,java.security.AlgorithmParameters)>(varReplacer11, $r5, $r7)

		RequiredPredicateError violating CrySL rule for java.security.AlgorithmParameters
			First parameter was not properly generated as preparedIV
			at statement: virtualinvoke $r7.<java.security.AlgorithmParameters: void init(java.security.spec.AlgorithmParameterSpec)>(r10)

		RequiredPredicateError violating CrySL rule for javax.crypto.spec.IvParameterSpec
			First parameter was not properly generated as randomized
			at statement: specialinvoke r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r8)
```

All three RequiredPredicateError is due to the IV is not called from SecureRandom. The IV is obtained from the parameters of a cipher object for encryption as `byte[] iv= params.getParameterSpec(IvParameterSpec.class).getIV();`  The this error propogate to another two required predicate.
