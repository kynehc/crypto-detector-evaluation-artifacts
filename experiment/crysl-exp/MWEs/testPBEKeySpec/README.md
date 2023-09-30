This case is to show the HardCodedError false positive in PBEKeySpec:

```
Findings in Java Class: com.example.testpbekeyspec.MainActivity

	 in Method: byte[] getKey(byte[],byte[],int,int)
		HardCodedError violating CrySL rule for javax.crypto.spec.PBEKeySpec (on Object #4e326a2b1621461fa1d29a812ff8a257ff59adef231f0cfb6660bd6f494d5a72)
			First parameter should never be hardcoded.
			at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>(r3, $r2, $i0, $i1)

		RequiredPredicateError violating CrySL rule for javax.crypto.SecretKeyFactory
			First parameter was not properly generated as speccedKey
			at statement: $r6 = virtualinvoke $r5.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r4)

		IncompleteOperationError violating CrySL rule for javax.crypto.spec.PBEKeySpec (on Object #4e326a2b1621461fa1d29a812ff8a257ff59adef231f0cfb6660bd6f494d5a72)
			Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
			at statement: $r6 = virtualinvoke $r5.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r4)
```

The wrong implementation of extractSootArray and isHardCodedArray caused this false positive. Specifcally, extractSootArray can not extract any array and always return 0 array, and then isHardCodedArray always return True, which means lots of false positives of HardCoded.

Then this HardCodedError will be propagated to RequiredPredicateError of javax.crypto.SecretKeyFactory, since PBEKeySpec already occur an error.