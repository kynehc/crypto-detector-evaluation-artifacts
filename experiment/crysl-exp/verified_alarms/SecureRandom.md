#### java.security.SecureRandom

```
----------------------------------------------------------------------
#1
Class: org.spongycastle.crypto.engines.NaccacheSternEngine
Method: byte[] processBlock(byte[],int,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
se.lublin.mumla_92.apk                                      => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
net.screenfreeze.deskcon_10.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
org.ligi.satoshiproof_104.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
org.c_base.c_beam_29.apk                                    => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
org.lumicall.android_192.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.mschlauch.comfortreader_13.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
net.vreeken.quickmsg_16.apk                                 => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.tananaev.passportreader_16.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
network.ubic.ubic_7.apk                                     => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
swati4star.createpdf_108.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.rehanced.lunary_31.apk                                  => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.standardnotes_3000323.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
ru.valle.btc_260.apk                                        => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.eletac.tronwallet_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.morlunk.mumbleclient_72.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $i3 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
com.lesspass.android_90503.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
eu.pretix.pretixprint_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
kiwi.root.an2linuxclient_19.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.NaccacheSternEngine: int getInputBlockSize()>()
```

FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#2
Class: org.spongycastle.crypto.engines.ElGamalEngine
Method: byte[] processBlock(byte[],int,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
se.lublin.mumla_92.apk                                      => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
net.screenfreeze.deskcon_10.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
org.ligi.satoshiproof_104.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
org.c_base.c_beam_29.apk                                    => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
org.lumicall.android_192.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.mschlauch.comfortreader_13.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
net.vreeken.quickmsg_16.apk                                 => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.tananaev.passportreader_16.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
network.ubic.ubic_7.apk                                     => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
swati4star.createpdf_108.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.rehanced.lunary_31.apk                                  => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.standardnotes_3000323.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
ru.valle.btc_260.apk                                        => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.eletac.tronwallet_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.morlunk.mumbleclient_72.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
com.lesspass.android_90503.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
eu.pretix.pretixprint_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
kiwi.root.an2linuxclient_19.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.engines.ElGamalEngine: int getInputBlockSize()>()
```

FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#3
Class: org.spongycastle.crypto.encodings.PKCS1Encoding
Method: byte[] encodeBlock(byte[],int,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
se.lublin.mumla_92.apk                                      => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
net.screenfreeze.deskcon_10.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
org.ligi.satoshiproof_104.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
org.c_base.c_beam_29.apk                                    => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
org.lumicall.android_192.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.mschlauch.comfortreader_13.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
net.vreeken.quickmsg_16.apk                                 => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.tananaev.passportreader_16.apk                          => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
network.ubic.ubic_7.apk                                     => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
swati4star.createpdf_108.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.rehanced.lunary_31.apk                                  => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.standardnotes_3000323.apk                               => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
ru.valle.btc_260.apk                                        => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.eletac.tronwallet_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.morlunk.mumbleclient_72.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $i3 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
com.lesspass.android_90503.apk                              => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
eu.pretix.pretixprint_37.apk                                => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()
kiwi.root.an2linuxclient_19.apk                             => at statement: $i2 = virtualinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int getInputBlockSize()>()

Error Type: TypestateError
Error Reason: Unexpected call to method nextBytes on object of type java.security.SecureRandom. Expect a call to one of the following methods init,getInstanceStrong,getInstance
Apk Num: 21
com.genonbeta.TrebleShot_104.apk                            => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)
se.lublin.mumla_92.apk                                      => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
net.screenfreeze.deskcon_10.apk                             => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
org.ligi.satoshiproof_104.apk                               => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
org.c_base.c_beam_29.apk                                    => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
org.lumicall.android_192.apk                                => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
com.mschlauch.comfortreader_13.apk                          => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
com.tananaev.passportreader_16.apk                          => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)
network.ubic.ubic_7.apk                                     => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
swati4star.createpdf_108.apk                                => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
com.rehanced.lunary_31.apk                                  => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)
com.standardnotes_3000323.apk                               => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
ru.valle.btc_260.apk                                        => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
com.eletac.tronwallet_37.apk                                => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>($r4)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r3)
com.morlunk.mumbleclient_72.apk                             => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>(r2)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: virtualinvoke $r5.<java.security.SecureRandom: void nextBytes(byte[])>($r4)
com.lesspass.android_90503.apk                              => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)
eu.pretix.pretixprint_37.apk                                => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)
kiwi.root.an2linuxclient_19.apk                             => at statement: virtualinvoke $r4.<java.security.SecureRandom: void nextBytes(byte[])>($r1)

Error Type: TypestateError
Error Reason: Unexpected call to method nextInt on object of type java.security.SecureRandom. Expect a call to one of the following methods init,getInstanceStrong,getInstance
Apk Num: 4
net.screenfreeze.deskcon_10.apk                             => at statement: $i3 = virtualinvoke $r5.<java.security.SecureRandom: int nextInt()>()
com.rehanced.lunary_31.apk                                  => at statement: $i3 = virtualinvoke $r4.<java.security.SecureRandom: int nextInt()>()
com.morlunk.mumbleclient_72.apk                             => at statement: $i3 = virtualinvoke $r5.<java.security.SecureRandom: int nextInt()>()
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $i3 = virtualinvoke $r5.<java.security.SecureRandom: int nextInt()>()
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

For TypestateError, FP: The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output TypestateError error.

```
----------------------------------------------------------------------
#4
Class: org.spongycastle.crypto.encodings.PKCS1Encoding
Method: byte[] decodeBlock(byte[],int,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
se.lublin.mumla_92.apk                                      => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
net.screenfreeze.deskcon_10.apk                             => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
org.ligi.satoshiproof_104.apk                               => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
org.c_base.c_beam_29.apk                                    => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
org.lumicall.android_192.apk                                => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.mschlauch.comfortreader_13.apk                          => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>(b2, $r1)
net.vreeken.quickmsg_16.apk                                 => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.tananaev.passportreader_16.apk                          => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
network.ubic.ubic_7.apk                                     => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
swati4star.createpdf_108.apk                                => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
com.rehanced.lunary_31.apk                                  => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.standardnotes_3000323.apk                               => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
ru.valle.btc_260.apk                                        => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.eletac.tronwallet_37.apk                                => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
com.morlunk.mumbleclient_72.apk                             => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
com.lesspass.android_90503.apk                              => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
eu.pretix.pretixprint_37.apk                                => at statement: $i0 = specialinvoke r0.<org.spongycastle.crypto.encodings.PKCS1Encoding: int findStart(byte,byte[])>($b3, $r1)
kiwi.root.an2linuxclient_19.apk                             => at statement: $i1 = interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: int getOutputBlockSize()>()
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.


```
----------------------------------------------------------------------
#5
Class: org.spongycastle.crypto.encodings.OAEPEncoding
Method: void init(boolean,org.spongycastle.crypto.CipherParameters)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
se.lublin.mumla_92.apk                                      => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
net.screenfreeze.deskcon_10.apk                             => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.ligi.satoshiproof_104.apk                               => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.c_base.c_beam_29.apk                                    => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.lumicall.android_192.apk                                => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.mschlauch.comfortreader_13.apk                          => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
net.vreeken.quickmsg_16.apk                                 => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.tananaev.passportreader_16.apk                          => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
network.ubic.ubic_7.apk                                     => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
swati4star.createpdf_108.apk                                => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.rehanced.lunary_31.apk                                  => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.standardnotes_3000323.apk                               => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
ru.valle.btc_260.apk                                        => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.eletac.tronwallet_37.apk                                => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.morlunk.mumbleclient_72.apk                             => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.lesspass.android_90503.apk                              => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
eu.pretix.pretixprint_37.apk                                => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
kiwi.root.an2linuxclient_19.apk                             => at statement: interfaceinvoke $r4.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#6
Class: org.spongycastle.crypto.encodings.OAEPEncoding
Method: byte[] decodeBlock(byte[],int,int)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer53050, $i1, $i2)
se.lublin.mumla_92.apk                                      => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer31016, $i0, $i1)
net.screenfreeze.deskcon_10.apk                             => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer11320, $i0, $i1)
org.ligi.satoshiproof_104.apk                               => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer18808, $i0, $i1)
org.c_base.c_beam_29.apk                                    => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer24648, $i0, $i1)
org.lumicall.android_192.apk                                => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer30465, $i0, $i1)
com.mschlauch.comfortreader_13.apk                          => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer21327, $i0, $i1)
net.vreeken.quickmsg_16.apk                                 => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer10656, $i0, $i1)
com.tananaev.passportreader_16.apk                          => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer51666, $i0, $i1)
network.ubic.ubic_7.apk                                     => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer25288, $i0, $i1)
swati4star.createpdf_108.apk                                => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer62746, $i0, $i1)
com.rehanced.lunary_31.apk                                  => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer49200, $i0, $i1)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer36661, $i0, $i1)
com.standardnotes_3000323.apk                               => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer34523, $i0, $i1)
ru.valle.btc_260.apk                                        => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer10402, $i0, $i1)
com.eletac.tronwallet_37.apk                                => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer49689, $i0, $i1)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer30826, $i0, $i1)
com.morlunk.mumbleclient_72.apk                             => at statement: r2 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer25062, $i0, $i1)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer47333, $i0, $i1)
com.lesspass.android_90503.apk                              => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer43080, $i1, $i2)
eu.pretix.pretixprint_37.apk                                => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer69061, $i1, $i2)
kiwi.root.an2linuxclient_19.apk                             => at statement: $r3 = specialinvoke r0.<org.spongycastle.crypto.encodings.OAEPEncoding: byte[] maskGeneratorFunction1(byte[],int,int,int)>($r1, varReplacer17794, $i0, $i1)
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#7
Class: org.spongycastle.crypto.encodings.ISO9796d1Encoding
Method: void init(boolean,org.spongycastle.crypto.CipherParameters)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 22
com.genonbeta.TrebleShot_104.apk                            => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
se.lublin.mumla_92.apk                                      => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
net.screenfreeze.deskcon_10.apk                             => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.ligi.satoshiproof_104.apk                               => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.c_base.c_beam_29.apk                                    => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
org.lumicall.android_192.apk                                => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.mschlauch.comfortreader_13.apk                          => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
net.vreeken.quickmsg_16.apk                                 => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.tananaev.passportreader_16.apk                          => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
network.ubic.ubic_7.apk                                     => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
swati4star.createpdf_108.apk                                => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
com.rehanced.lunary_31.apk                                  => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
com.standardnotes_3000323.apk                               => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
ru.valle.btc_260.apk                                        => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.eletac.tronwallet_37.apk                                => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
com.morlunk.mumbleclient_72.apk                             => at statement: interfaceinvoke $r5.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: interfaceinvoke $r2.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.lesspass.android_90503.apk                              => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
eu.pretix.pretixprint_37.apk                                => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
kiwi.root.an2linuxclient_19.apk                             => at statement: interfaceinvoke $r1.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r2)
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#8
Class: org.spongycastle.pqc.crypto.ntru.NTRUEngine
Method: byte[] decrypt(byte[],org.spongycastle.pqc.crypto.ntru.NTRUEncryptionPrivateKeyParameters)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 21
com.genonbeta.TrebleShot_104.apk                            => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
se.lublin.mumla_92.apk                                      => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
net.screenfreeze.deskcon_10.apk                             => at statement: r13 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, i0, $i6, $z0)
org.c_base.c_beam_29.apk                                    => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
org.lumicall.android_192.apk                                => at statement: r13 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, i0, $i6, $z0)
com.mschlauch.comfortreader_13.apk                          => at statement: r13 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, i0, $i6, $z0)
net.vreeken.quickmsg_16.apk                                 => at statement: r13 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, i0, $i6, $z0)
com.tananaev.passportreader_16.apk                          => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
network.ubic.ubic_7.apk                                     => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
swati4star.createpdf_108.apk                                => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
com.rehanced.lunary_31.apk                                  => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
com.standardnotes_3000323.apk                               => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
ru.valle.btc_260.apk                                        => at statement: $i7 = virtualinvoke $r6.<org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial: int count(int)>(varReplacer10429)
com.eletac.tronwallet_37.apk                                => at statement: $r12 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
com.morlunk.mumbleclient_72.apk                             => at statement: r13 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, i0, $i6, $z0)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $r12 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i2, $i6, $z0)
com.lesspass.android_90503.apk                              => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
eu.pretix.pretixprint_37.apk                                => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
kiwi.root.an2linuxclient_19.apk                             => at statement: $r10 = specialinvoke r0.<org.spongycastle.pqc.crypto.ntru.NTRUEngine: org.spongycastle.pqc.math.ntru.polynomial.IntegerPolynomial MGF(byte[],int,int,boolean)>($r1, $i1, $i6, $z0)
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#9
Class: org.spongycastle.crypto.tls.TlsRSAUtils
Method: byte[] generateEncryptedPreMasterSecret(org.spongycastle.crypto.tls.TlsContext,org.spongycastle.crypto.params.RSAKeyParameters,java.io.OutputStream)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 21
com.genonbeta.TrebleShot_104.apk                            => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer66114, varReplacer66115)
se.lublin.mumla_92.apk                                      => at statement: $r10 = virtualinvoke $r7.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r4, varReplacer39361, $i0)
net.screenfreeze.deskcon_10.apk                             => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer12888, $i0)
org.c_base.c_beam_29.apk                                    => at statement: $r10 = virtualinvoke $r7.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r4, varReplacer26218, $i0)
org.lumicall.android_192.apk                                => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer29657, $i0)
com.mschlauch.comfortreader_13.apk                          => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer29135, $i0)
net.vreeken.quickmsg_16.apk                                 => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer15855, $i0)
com.tananaev.passportreader_16.apk                          => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer49426, varReplacer49427)
network.ubic.ubic_7.apk                                     => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer27890, $i0)
swati4star.createpdf_108.apk                                => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer56019, $i0)
com.rehanced.lunary_31.apk                                  => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer47993, $i0)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer35101, varReplacer35102)
com.standardnotes_3000323.apk                               => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer41284, $i0)
ru.valle.btc_260.apk                                        => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer9817, $i0)
com.eletac.tronwallet_37.apk                                => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer48160, $i0)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer29600, $i0)
com.morlunk.mumbleclient_72.apk                             => at statement: $r10 = virtualinvoke r4.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>(r5, varReplacer27631, $i0)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r3, varReplacer45506, $i0)
com.lesspass.android_90503.apk                              => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer39425, varReplacer39426)
eu.pretix.pretixprint_37.apk                                => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer84508, varReplacer84509)
kiwi.root.an2linuxclient_19.apk                             => at statement: $r9 = virtualinvoke $r6.<org.spongycastle.crypto.encodings.PKCS1Encoding: byte[] processBlock(byte[],int,int)>($r0, varReplacer20495, varReplacer20496)
```

For IncompleteOperationError, FP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse. The SecureRandom object indeed called initilization methods (init/getInstance). Multiple branches/paths makes it output IncompleteOperationError error.

```
----------------------------------------------------------------------
#10
Class: org.spongycastle.crypto.signers.RSADigestSigner
Method: void init(boolean,org.spongycastle.crypto.CipherParameters)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.SecureRandom object not completed. Expected call to init, getInstanceStrong, getInstance
Apk Num: 21
com.genonbeta.TrebleShot_104.apk                            => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
se.lublin.mumla_92.apk                                      => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
net.screenfreeze.deskcon_10.apk                             => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.c_base.c_beam_29.apk                                    => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.lumicall.android_192.apk                                => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.mschlauch.comfortreader_13.apk                          => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
net.vreeken.quickmsg_16.apk                                 => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.tananaev.passportreader_16.apk                          => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
network.ubic.ubic_7.apk                                     => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
swati4star.createpdf_108.apk                                => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.rehanced.lunary_31.apk                                  => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.vecturagames.android.app.passwordmaster_6.apk           => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.standardnotes_3000323.apk                               => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
ru.valle.btc_260.apk                                        => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.eletac.tronwallet_37.apk                                => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
org.zephyrsoft.sdbviewer_6.apk                              => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.morlunk.mumbleclient_72.apk                             => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.outdoordevs.ellaism.wallet_35.apk                       => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
com.lesspass.android_90503.apk                              => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
eu.pretix.pretixprint_37.apk                                => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
kiwi.root.an2linuxclient_19.apk                             => at statement: interfaceinvoke $r6.<org.spongycastle.crypto.AsymmetricBlockCipher: void init(boolean,org.spongycastle.crypto.CipherParameters)>($z0, $r1)
```

For IncompleteOperationError, ITP: SecureRandom IncompleteOperationError does not cause any vulnerability of Cryptography misuse.