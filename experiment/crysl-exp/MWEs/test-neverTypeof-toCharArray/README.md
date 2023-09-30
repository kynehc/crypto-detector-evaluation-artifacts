This case is to show NeverTypeOf error false positive for String.toCharArray()

```
Findings in Java Class: com.example.testnevertypeoftochararray.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		NeverTypeOfError violating CrySL rule for java.net.PasswordAuthentication (on Object #790af46fb64feb729f768daa0f895949c700af37c309812fb191331e8d287647)
			Second parameter should never be of type java.lang.String.
			at statement: specialinvoke r6.<java.net.PasswordAuthentication: void <init>(java.lang.String,char[])>(varReplacer8, $r2)

		HardCodedError violating CrySL rule for java.net.PasswordAuthentication (on Object #790af46fb64feb729f768daa0f895949c700af37c309812fb191331e8d287647)
			Second parameter should never be hardcoded.
			at statement: specialinvoke r6.<java.net.PasswordAuthentication: void <init>(java.lang.String,char[])>(varReplacer8, $r2)
```

Crysl takes String.toCharArray() as String, which violates neverTypeOf String rule. At the same time, this always also violated notHardCoded Error, pls refer to NotHardCoded FP.
