#### java.security.KeyPairGenerator

```
----------------------------------------------------------------------
#1
Class: com.jcraft.jsch.Session
Method: void run()

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 11
org.courville.nova_404911.apk                               => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
com.elektropepi.bootboi_11.apk                              => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
com.example.sshtry_1.apk                                    => at statement: r7 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r9)
io.mainframe.hacs_53.apk                                    => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
com.vadimfrolov.duorem_6.apk                                => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
org.brandroid.openmanager_212.apk                           => at statement: r7 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r9)
horse.amazin.my.stratum0.statuswidget_22.apk                => at statement: $r5 = null
org.ligi.etheremote_2.apk                                   => at statement: r7 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r9)
it.skarafaz.mercury_9.apk                                   => at statement: $i2 = virtualinvoke $r9.<com.jcraft.jsch.KeyExchange: int getState()>()
org.kknickkk.spider_13.apk                                  => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
com.madgag.agit_139000000.apk                               => at statement: r7 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r9)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to genKeyPair, initialize, generateKeyPair
Apk Num: 1
com.manichord.mgit_220.apk                                  => at statement: $r9 = specialinvoke r0.<com.jcraft.jsch.Session: com.jcraft.jsch.KeyExchange receive_kexinit(com.jcraft.jsch.Buffer)>($r11)
```

IncompleteOperationError, FP: There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse. We suspect this error is caused by multiple incorrectly handling generics.

```
----------------------------------------------------------------------
#2
Class: com.google.crypto.tink.subtle.AesSiv
Method: byte[] encryptDeterministically(byte[],byte[])

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 11
com.zell_mbc.medilog_5351.apk                               => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
org.openhab.habdroid_404.apk                                => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
ch.protonvpn.android_102119017.apk                          => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
me.lucky.wasted_21.apk                                      => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
net.ivpn.client_100.apk                                     => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
host.stjin.anonaddy_29.apk                                  => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
io.github.domi04151309.home_180.apk                         => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
net.taler.cashier_1.apk                                     => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r1 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r1)
```

IncompleteOperationError, FP: There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse. We suspect this error is caused by multiple incorrectly handling generics.

```
----------------------------------------------------------------------
#3
Class: com.jcraft.jsch.jce.DH
Method: byte[] getE()

Error Type: TypestateError
Error Reason: Unexpected call to method initialize on object of type java.security.KeyPairGenerator.
Apk Num: 10
org.courville.nova_404911.apk                               => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
com.elektropepi.bootboi_11.apk                              => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
com.example.sshtry_1.apk                                    => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>(r1)
io.mainframe.hacs_53.apk                                    => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
com.vadimfrolov.duorem_6.apk                                => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
org.brandroid.openmanager_212.apk                           => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>(r1)
org.ligi.etheremote_2.apk                                   => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>(r1)
it.skarafaz.mercury_9.apk                                   => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
org.kknickkk.spider_13.apk                                  => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)
com.madgag.agit_139000000.apk                               => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>(r1)

Error Type: TypestateError
Error Reason: Unexpected call to method initialize on object of type java.security.KeyPairGenerator. Expect a call to one of the following methods genKeyPair,generateKeyPair
Apk Num: 1
com.manichord.mgit_220.apk                                  => at statement: virtualinvoke $r4.<java.security.KeyPairGenerator: void initialize(java.security.spec.AlgorithmParameterSpec)>($r2)

Error Type: TypestateError
Error Reason: Unexpected call to method <java.security.KeyPairGenerator: java.security.KeyPair generateKeyPair()> on object of type java.security.KeyPairGenerator. Expect a call to one of the following methods java.security.KeyPairGenerator: java.security.KeyPair generateKeyPair(),java.security.KeyPairGenerator: java.security.KeyPair genKeyPair(),java.security.KeyPairGeneratorSpi: java.security.KeyPair generateKeyPair()
Apk Num: 1
com.manichord.mgit_220.apk                                  => at statement: $r5 = virtualinvoke $r4.<java.security.KeyPairGenerator: java.security.KeyPair generateKeyPair()>()
```

TypestateError, FP: The KeyPairGenerator object indeed called getInstance first. This error is caused by multiple paths/branches. Please refer to `testKeyPairGenerator-PathInsensitive` case.

```
----------------------------------------------------------------------
#4
Class: com.jcraft.jsch.Session
Method: boolean checkKex(com.jcraft.jsch.Session,java.lang.String)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 10
org.courville.nova_404911.apk                               => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer39629, varReplacer39629, varReplacer39629, varReplacer39629)
com.elektropepi.bootboi_11.apk                              => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer14594, varReplacer14594, varReplacer14594, varReplacer14594)
com.example.sshtry_1.apk                                    => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r0, varReplacer1549, varReplacer1549, varReplacer1549, varReplacer1549)
io.mainframe.hacs_53.apk                                    => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer13474, varReplacer13474, varReplacer13474, varReplacer13474)
com.vadimfrolov.duorem_6.apk                                => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer7175, varReplacer7175, varReplacer7175, varReplacer7175)
org.brandroid.openmanager_212.apk                           => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r0, varReplacer10489, varReplacer10489, varReplacer10489, varReplacer10489)
org.ligi.etheremote_2.apk                                   => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r0, varReplacer8012, varReplacer8012, varReplacer8012, varReplacer8012)
it.skarafaz.mercury_9.apk                                   => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer11342, varReplacer11342, varReplacer11342, varReplacer11342)
org.kknickkk.spider_13.apk                                  => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer5635, varReplacer5635, varReplacer5635, varReplacer5635)
com.madgag.agit_139000000.apk                               => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r0, varReplacer8068, varReplacer8068, varReplacer8068, varReplacer8068)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to genKeyPair, initialize, generateKeyPair
Apk Num: 1
com.manichord.mgit_220.apk                                  => at statement: virtualinvoke $r5.<com.jcraft.jsch.KeyExchange: void init(com.jcraft.jsch.Session,byte[],byte[],byte[],byte[])>($r1, varReplacer11705, varReplacer11705, varReplacer11705, varReplacer11705)
```

IncompleteOperationError, FP: There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse. We suspect this error is caused by multiple incorrectly handling generics.

```
----------------------------------------------------------------------
#5
Class: com.google.crypto.tink.subtle.RsaSsaPssSignJce
Method: void <init>(java.security.interfaces.RSAPrivateCrtKey,com.google.crypto.tink.subtle.Enums$HashType,com.google.crypto.tink.subtle.Enums$HashType,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 10
com.zell_mbc.medilog_5351.apk                               => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
org.openhab.habdroid_404.apk                                => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
ch.protonvpn.android_102119017.apk                          => at statement: $r11 = virtualinvoke $r8.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r9)
me.lucky.wasted_21.apk                                      => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
net.ivpn.client_100.apk                                     => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
host.stjin.anonaddy_29.apk                                  => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
net.taler.cashier_1.apk                                     => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r10 = virtualinvoke $r7.<java.security.KeyFactory: java.security.PublicKey generatePublic(java.security.spec.KeySpec)>($r8)
```

IncompleteOperationError, FP: There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse. We suspect this error is caused by multiple incorrectly handling generics.

```
----------------------------------------------------------------------
#6
Class: com.google.crypto.tink.subtle.EngineWrapper$TKeyPairGenerator
Method: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)

Error Type: ConstraintError
Error Reason: First parameter (with value "AES/CTR/NoPadding") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 10
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
net.ivpn.client_100.apk                                     => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
host.stjin.anonaddy_29.apk                                  => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
io.github.domi04151309.home_180.apk                         => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
security.pEp_470.apk                                        => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "SHA-512") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 8
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
host.stjin.anonaddy_29.apk                                  => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.example.trigger_336.apk                                 => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
org.connectbot_10908000.apk                                 => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
security.pEp_470.apk                                        => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "SHA-384") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 5
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
security.pEp_470.apk                                        => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "SHA-256") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 5
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
security.pEp_470.apk                                        => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)

Error Type: ConstraintError
Error Reason: First parameter (with value "SHA-1") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 5
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
security.pEp_470.apk                                        => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)

Error Type: ConstraintError
Error Reason: First parameter (with value "AES/GCM/NoPadding") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 3
net.ivpn.client_100.apk                                     => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "AES/ECB/NoPadding") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 3
io.github.domi04151309.home_180.apk                         => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "RSA/ECB/NOPADDING") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 2
com.zell_mbc.medilog_5351.apk                               => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "HmacSha512") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 2
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "HmacSha384") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 2
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "HmacSha256") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 2
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)

Error Type: ConstraintError
Error Reason: First parameter (with value "HmacSha1") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 2
la.daube.photochiotte_19.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String)>($r2)

Error Type: ConstraintError
Error Reason: First parameter (with value "ECDH") should be any of {RSA, EC, DSA, DiffieHellman, DH}
Apk Num: 1
com.github.igrmk.smsq_16.apk                                => at statement: $r3 = staticinvoke <java.security.KeyPairGenerator: java.security.KeyPairGenerator getInstance(java.lang.String,java.security.Provider)>($r2, $r1)
```

FP: Crysl handle generics in Java incorrectly.

```
----------------------------------------------------------------------
#7
Class: com.google.crypto.tink.subtle.Ed25519
Method: byte[] getHashedScalar(byte[])

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 10
com.zell_mbc.medilog_5351.apk                               => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
org.openhab.habdroid_404.apk                                => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
ch.protonvpn.android_102119017.apk                          => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
me.lucky.wasted_21.apk                                      => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
net.ivpn.client_100.apk                                     => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
host.stjin.anonaddy_29.apk                                  => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
com.example.trigger_336.apk                                 => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
org.connectbot_10908000.apk                                 => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
net.taler.cashier_1.apk                                     => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r0 = virtualinvoke $r3.<java.security.MessageDigest: byte[] digest()>()
```

IncompleteOperationError, FP: Crysl handle generics in Java incorrectly. There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse.

```
----------------------------------------------------------------------
#8
Class: com.google.crypto.tink.subtle.RsaSsaPssVerifyJce
Method: void emsaPssVerify(byte[],byte[],int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 9
com.zell_mbc.medilog_5351.apk                               => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
org.openhab.habdroid_404.apk                                => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
ch.protonvpn.android_102119017.apk                          => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
me.lucky.wasted_21.apk                                      => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
net.ivpn.client_100.apk                                     => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
host.stjin.anonaddy_29.apk                                  => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
org.openhab.habdroid.beta_416.apk                           => at statement: $r2 = virtualinvoke $r10.<java.security.MessageDigest: byte[] digest(byte[])>($r8)
```

IncompleteOperationError, FP: Crysl handle generics in Java incorrectly. There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse.

```
----------------------------------------------------------------------
#9
Class: com.google.crypto.tink.subtle.AesSiv
Method: byte[] decryptDeterministically(byte[],byte[])

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 9
com.zell_mbc.medilog_5351.apk                               => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
ch.protonvpn.android_102119017.apk                          => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
me.lucky.wasted_21.apk                                      => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
net.ivpn.client_100.apk                                     => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
host.stjin.anonaddy_29.apk                                  => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
io.github.domi04151309.home_180.apk                         => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
net.taler.cashier_1.apk                                     => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r9 = virtualinvoke $r5.<javax.crypto.Cipher: byte[] doFinal(byte[])>($r7)
```

IncompleteOperationError, FP: Crysl handle generics in Java incorrectly. There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse.

```
----------------------------------------------------------------------
#10
Class: com.jcraft.jsch.DHGEX
Method: int check2048(java.lang.Class,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to initialize
Apk Num: 7
org.courville.nova_404911.apk                               => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
com.elektropepi.bootboi_11.apk                              => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
io.mainframe.hacs_53.apk                                    => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
com.vadimfrolov.duorem_6.apk                                => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
org.ligi.etheremote_2.apk                                   => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
it.skarafaz.mercury_9.apk                                   => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
org.kknickkk.spider_13.apk                                  => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyPairGenerator object not completed. Expected call to genKeyPair, initialize, generateKeyPair
Apk Num: 1
com.manichord.mgit_220.apk                                  => at statement: interfaceinvoke $r4.<com.jcraft.jsch.DH: byte[] getE()>()
```

IncompleteOperationError, FP: Crysl handle generics in Java incorrectly. There is no KeyPairGenerator object in the target location method. Other KeyPairGenerator objects in the apk called `initilize`. Also, the IncompleteOperationError does not cause vulnerability of cryptography misuse.