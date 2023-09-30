This case is to show the HardCodedError false positive in KeyStore:

```
Findings in Java Class: com.example.testkeystorehardcoded.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		NeverTypeOfError violating CrySL rule for java.security.KeyStore (on Object #b325ce14a262f8116a503805a574b099bdcd199e4a3a00c0c8511136f5f6e1fe)
			Second parameter should never be of type java.lang.String.
			at statement: virtualinvoke $r3.<java.security.KeyStore: void load(java.io.InputStream,char[])>(varReplacer10, $r4)

		HardCodedError violating CrySL rule for java.security.KeyStore (on Object #b325ce14a262f8116a503805a574b099bdcd199e4a3a00c0c8511136f5f6e1fe)
			Second parameter should never be hardcoded.
			at statement: virtualinvoke $r3.<java.security.KeyStore: void load(java.io.InputStream,char[])>(varReplacer10, $r4)
```

The wrong implementation of extractSootArray and isHardCodedArray caused this false positive. Specifcally, extractSootArray can not extract any array and always return 0 array, and then isHardCodedArray always return True. This buggy implementation caused lots of false positive for HardCodedError.