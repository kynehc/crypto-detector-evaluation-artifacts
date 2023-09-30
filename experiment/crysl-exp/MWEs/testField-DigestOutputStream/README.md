This case is to show the IncompleteOperationError false positive for DigestOutputStream. This is a general problem also applied to other rules in typestate analysis.

```
Findings in Java Class: com.example.testdigestoutputstreamwrite.DigestOut

	 in Method: void <init>()
		IncompleteOperationError violating CrySL rule for java.security.MessageDigest (on Object #f8ce5e592a82b9de8c93c24795e70886c7373b0d44fb0ad1884308343f00fddc)
			Operation on object of type java.security.MessageDigest object not completed. Expected call to digest, update
			at statement: specialinvoke $r2.<java.security.DigestOutputStream: void <init>(java.io.OutputStream,java.security.MessageDigest)>(r1, $r3)


Findings in Java Class: com.example.testdigestoutputstreamwrite.MainActivity

	 in Method: void onCreate(android.os.Bundle)
		IncompleteOperationError violating CrySL rule for java.security.DigestOutputStream (on Object #806520232075f26a7d42f1f971c902e82811c2f9e28db94aaa5a3f229cc77173)
			Operation on object of type java.security.DigestOutputStream object not completed. Expected call to write
			at statement: virtualinvoke r4.<com.example.testdigestoutputstreamwrite.DigestOut: void writeChecksum(byte[])>($r2)
```

There is a DigestOutputStream object as class field (class member) in DigestOut class. The construct function of DigestOut class initilizes this DigestOutputStream object. Another public method `writeChecksum()` of DigestOut class calls the field object (DigestOutputStream object) `write()` method. Thus in general, for this class field, its typestate is changed in different methods in a class. 

First, this is a Model-false positive: according to original JCA-rules in dataset, they miss such a method (`write(byte[])`), since this is a method implemented in the DigestOutputStream's basic class FilterOutputStream.

Furthur, We add the missing method into rule but still get the same IncompleteOperationError error. So this is a Implementation-false positive: Crysl Typestate analysis does not change state of DigestOutputStream object when meet `write()` in the `writeChecksum()` method, which causes this false positive.