This case is to show the false positive of MessageDigest:

```
Findings in Java Class: com.example.testpoly.HasherWrapper

	 in Method: byte[] getHash(com.example.testpoly.Hasher)
		TypestateError violating CrySL rule for java.security.MessageDigest (on Object #7258ec65b7d8b185d62f4ec3c3de7d12981f211c9724ae277f29cb9eb5b7f0c9)
			Unexpected call to method <java.security.MessageDigest: byte[] digest()> on object of type java.security.MessageDigest. Expect a call to one of the following methods java.security.MessageDigest: void update(byte[],int,int),java.security.MessageDigest: void update(java.nio.ByteBuffer),java.security.MessageDigest: byte[] digest(byte[]),java.security.MessageDigest: void update(byte),java.security.MessageDigest: void update(byte[])
			at statement: $r4 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
```

Crysl does not leverage the type information of `UpdateKey` and consider all classes that implemented the interface as possible cases, which leads to this FP.