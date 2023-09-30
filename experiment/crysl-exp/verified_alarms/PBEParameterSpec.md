#### javax.crypto.spec.PBEParameterSpec

```
----------------------------------------------------------------------
#1
Class: org.eclipse.jgit.transport.WalkEncryption$ObjectEncryptionV2
Method: void <init>(java.lang.String,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 2
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r1, $i0)
com.madgag.agit_139000000.apk                               => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r5, $i0)
```

TP: constant salts for encryption.

```
----------------------------------------------------------------------
#2
Class: org.runnerup.util.Encryption
Method: void decrypt(java.io.InputStream,java.io.OutputStream,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
org.runnerup.free_15000312.apk                              => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r7, varReplacer7010)

Error Type: ConstraintError
Error Reason: Second parameter (with value 100)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.runnerup.free_15000312.apk                              => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r7, varReplacer7010)
```

For RequiredPredicateError, ITP: decryption operation needs to read salt from InputStream.

For ConstraintError, TP: 100 Iteration count.


```
----------------------------------------------------------------------
#3
Class: org.openintents.safe.CryptoHelper
Method: void initialize(int)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
org.openintents.safe_30.apk                                 => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r1, varReplacer1065)

Error Type: ConstraintError
Error Reason: Second parameter (with value 20)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.openintents.safe_30.apk                                 => at statement: specialinvoke $r8.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r1, varReplacer1065)
```

For RequiredPredicateError, FP: the salt value is indeed randomized. Pls refer to `testPBEParameterSpec-RandomizedSalt` case.

For ConstraintError, TP: 20 Iteration count.


```
----------------------------------------------------------------------
#4
Class: org.connectbot.util.PubkeyUtils
Method: java.lang.String exportPEM(java.security.PrivateKey,java.lang.String)

Error Type: ConstraintError
Error Reason: Second parameter (with value 1)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.connectbot_10908000.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r3, varReplacer11129)
```

For ConstraintError, TP: 1 Iteration count.

```
----------------------------------------------------------------------
#5
Class: l.b.c.a.a
Method: byte[] c(byte[])

Error Type: ConstraintError
Error Reason: Second parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
me.blog.korn123.easydiary_260.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r12, $i0)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.

```
----------------------------------------------------------------------
#6
Class: l.b.c.a.a
Method: byte[] b(byte[])

Error Type: ConstraintError
Error Reason: Second parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
me.blog.korn123.easydiary_260.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r7, $i0)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.

```
----------------------------------------------------------------------
#7
Class: host.stjin.anonaddy.service.BackupHelper
Method: javax.crypto.Cipher makeCipher(char[],boolean)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r9, varReplacer35652)

Error Type: ConstraintError
Error Reason: Second parameter (with value 43)Variable iterationCountmust be  at least 10000
Apk Num: 1
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r9, varReplacer35652)
```

For RequiredPredicateError, TP.

For ConstraintError, TP.

```
----------------------------------------------------------------------
#8
Class: com.zoffcc.applications.aagtl.StringEnc
Method: void <init>(java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
com.zoffcc.applications.aagtl_36.apk                        => at statement: specialinvoke r3.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>(r4, varReplacer818)

Error Type: ConstraintError
Error Reason: Second parameter (with value 19)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.zoffcc.applications.aagtl_36.apk                        => at statement: specialinvoke r3.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>(r4, varReplacer818)
```

For RequiredPredicateError, TP.

For ConstraintError, TP.

```
----------------------------------------------------------------------
#9
Class: com.rfo.basic.Basic$Encryption
Method: void <init>(int,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
com.rfo.basic_500.apk                                       => at statement: specialinvoke r4.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r6, varReplacer2498)

Error Type: ConstraintError
Error Reason: Second parameter (with value 19)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.rfo.basic_500.apk                                       => at statement: specialinvoke r4.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r6, varReplacer2498)
```

For RequiredPredicateError, TP.

For ConstraintError, TP.

```
----------------------------------------------------------------------
#10
Class: com.rfo.LASKmobile.Basic$Encryption
Method: void <init>(int,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
com.rfo.LASKmobile_501.apk                                  => at statement: specialinvoke r4.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r6, varReplacer2346)

Error Type: ConstraintError
Error Reason: Second parameter (with value 19)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.rfo.LASKmobile_501.apk                                  => at statement: specialinvoke r4.<javax.crypto.spec.PBEParameterSpec: void <init>(byte[],int)>($r6, varReplacer2346)
```

For RequiredPredicateError, TP.

For ConstraintError, TP.