This case is to show the notHardCoded error false positive for PasswordAuthentication

```
Findings in Java Class: com.example.testnothardcodedpa.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		HardCodedError violating CrySL rule for java.net.PasswordAuthentication (on Object #f896ae8d3c4bb186db37bea97a13bff5562c843b6b9c10c7996d407f1f27c787)
			Second parameter should never be hardcoded.
			at statement: specialinvoke r5.<java.net.PasswordAuthentication: void <init>(java.lang.String,char[])>(varReplacer7, $r2)
```

The wrong implementation of `extractSootArray` and `isHardCodedArray` caused this false positive. Specifcally, `extractSootArray` can not extract any array and always return 0 array, and then `isHardCodedArray` always return True, which means lots of false positives of HardCoded.
