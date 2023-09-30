This case is to show the IncompleteOperationError false positive in KeyPairGenerator.

```
Findings in Java Class: com.example.testkeypairgenerator.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		IncompleteOperationError violating CrySL rule for java.security.KeyPairGenerator (on Object #daa18da83ff6b523924c397345e039ae09a5845ea07c07eed1b7d75e3419e965)
			Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
			at statement: $r3 = virtualinvoke r2.<com.example.testkeypairgenerator.KeyPairWrapper: byte[] getModulus()>()
```

The KeyPairGenerator indeed called `initialize` in an if-else block. Although the condition is obviously fulfilled in static code, Crysl static analysis is path-insensitive that always consider a path that does not execute the code in if block. Consequently, this IncompleteOperationError false positive occured.