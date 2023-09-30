#### javax.crypto.spec.PBEKeySpec

```
----------------------------------------------------------------------
#1
Class: com.jcraft.jsch.jce.PBKDF
Method: byte[] getKey(byte[],byte[],int,int)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 8
org.courville.nova_404911.apk                               => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.elektropepi.bootboi_11.apk                              => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
io.mainframe.hacs_53.apk                                    => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.vadimfrolov.duorem_6.apk                                => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
org.ligi.etheremote_2.apk                                   => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>(r3, $r2, $i0, $i1)
it.skarafaz.mercury_9.apk                                   => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
org.kknickkk.spider_13.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 8
org.courville.nova_404911.apk                               => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
com.elektropepi.bootboi_11.apk                              => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
io.mainframe.hacs_53.apk                                    => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
com.vadimfrolov.duorem_6.apk                                => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
com.manichord.mgit_220.apk                                  => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
org.ligi.etheremote_2.apk                                   => at statement: $r6 = virtualinvoke $r5.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r4)
it.skarafaz.mercury_9.apk                                   => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)
org.kknickkk.spider_13.apk                                  => at statement: $r8 = virtualinvoke $r7.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r6)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 8
org.courville.nova_404911.apk                               => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.elektropepi.bootboi_11.apk                              => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
io.mainframe.hacs_53.apk                                    => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.vadimfrolov.duorem_6.apk                                => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
org.ligi.etheremote_2.apk                                   => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>(r3, $r2, $i0, $i1)
it.skarafaz.mercury_9.apk                                   => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
org.kknickkk.spider_13.apk                                  => at statement: specialinvoke $r6.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r4, $i0, $i1)
```

For RequiredPredicateError, ITP: the method is used under decrypt context, thus the second parameter (salt) should be read from the external instead of SecureRandom.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.

```
----------------------------------------------------------------------
#2
Class: eu.siacs.conversations.services.ExportBackupService
Method: byte[] getKey(java.lang.String,byte[])

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 4
org.snikket.android_42024.apk                               => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17836, varReplacer17837)
com.cweb.messenger_42012.apk                                => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer25968, varReplacer25969)
eu.siacs.conversations_42023.apk                            => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17871, varReplacer17872)
im.quicksy.client_42023.apk                                 => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer18236, varReplacer18237)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 4
org.snikket.android_42024.apk                               => at statement: $r5 = virtualinvoke $r3.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r0)
com.cweb.messenger_42012.apk                                => at statement: $r5 = virtualinvoke $r3.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r0)
eu.siacs.conversations_42023.apk                            => at statement: $r5 = virtualinvoke $r3.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r0)
im.quicksy.client_42023.apk                                 => at statement: $r5 = virtualinvoke $r3.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r0)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 4
org.snikket.android_42024.apk                               => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17836, varReplacer17837)
com.cweb.messenger_42012.apk                                => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer25968, varReplacer25969)
eu.siacs.conversations_42023.apk                            => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17871, varReplacer17872)
im.quicksy.client_42023.apk                                 => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer18236, varReplacer18237)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 4
org.snikket.android_42024.apk                               => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17836, varReplacer17837)
com.cweb.messenger_42012.apk                                => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer25968, varReplacer25969)
eu.siacs.conversations_42023.apk                            => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer17871, varReplacer17872)
im.quicksy.client_42023.apk                                 => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, varReplacer18236, varReplacer18237)
```

For NeverTypeOfError, ITP: vain predicate.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#3
Class: Crypto
Method: javax.crypto.SecretKey deriveKeyPbkdf2(byte[],java.lang.String)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 4
de.moroway.oc_70300.apk                                     => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)
net.khertan.forrunners_101030.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
fr.librinfo.evecontrol2_20000.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
com.xBrowserSync.android_15201.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 4
de.moroway.oc_70300.apk                                     => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)
net.khertan.forrunners_101030.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
fr.librinfo.evecontrol2_20000.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
com.xBrowserSync.android_15201.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 4
de.moroway.oc_70300.apk                                     => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)
net.khertan.forrunners_101030.apk                           => at statement: $r6 = virtualinvoke $r5.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r2)
fr.librinfo.evecontrol2_20000.apk                           => at statement: $r6 = virtualinvoke $r5.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r2)
com.xBrowserSync.android_15201.apk                          => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 4
de.moroway.oc_70300.apk                                     => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)
net.khertan.forrunners_101030.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
fr.librinfo.evecontrol2_20000.apk                           => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r0, $i1, $i2)
com.xBrowserSync.android_15201.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, $i2, $i0)
```

For RequiredPredicateError, ITP: Under decryption context, the salt has to be loaded from an external source.

For NeverTypeOfError, ITP: vain predicate.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.


```
----------------------------------------------------------------------
#4
Class: kellinwood.security.zipsigner.ZipSigner
Method: java.security.spec.KeySpec decryptPrivateKey(byte[],java.lang.String)

Error Type: ForbiddenMethodError
Error Reason: Detected call to forbidden method void <init>(char[]) of class javax.crypto.spec.PBEKeySpec. Instead, call method <javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>.
Apk Num: 3
org.fdroid.fdroid_1013051.apk                               => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[])>($r5)
ie.defo.ech_apps_1014003.apk                                => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[])>($r5)
org.fdroid.nearby_2.apk                                     => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[])>($r5)
```

For ForbiddenMethodError, TP: iteration count and salt problem.


```
----------------------------------------------------------------------
#5
Class: com.tozny.crypto.android.AesCbcWithIntegrity
Method: com.tozny.crypto.android.AesCbcWithIntegrity$SecretKeys generateKeyFromPassword(java.lang.String,byte[],int)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 3
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer50417)
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer3119)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer66439)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 3
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer50417)
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer3119)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer66439)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 3
ch.protonvpn.android_102119017.apk                          => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)
com.manichord.mgit_220.apk                                  => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 3
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer50417)
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer3119)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, $i0, varReplacer66439)
```

For RequiredPredicateError, TP: it use following code to return value as salt.

```
private static String getDeviceSerialNumber(Context context) {
        try {
            String str = (String) Build.class.getField("SERIAL").get(null);
            return TextUtils.isEmpty(str) ? Settings.Secure.getString(context.getContentResolver(), "android_id") : str;
        } catch (Exception unused) {
            return Settings.Secure.getString(context.getContentResolver(), "android_id");
        }
    }
```

For NeverTypeOfError, ITP: vain predicate.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.


```
----------------------------------------------------------------------
#6
Class: com.github.javiersantos.licensing.AESObfuscator
Method: void <init>(byte[],java.lang.String,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 3
de.spiritcroc.darkcroc.substratum_11.apk                    => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer781, varReplacer782)
com.x1unix.s60icons_110.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer12564, varReplacer12565)
de.spiritcroc.defaultdarktheme_oms_53.apk                   => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer573, varReplacer574)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 3
de.spiritcroc.darkcroc.substratum_11.apk                    => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer781, varReplacer782)
com.x1unix.s60icons_110.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer12564, varReplacer12565)
de.spiritcroc.defaultdarktheme_oms_53.apk                   => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer573, varReplacer574)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 3
de.spiritcroc.darkcroc.substratum_11.apk                    => at statement: $r8 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r5)
com.x1unix.s60icons_110.apk                                 => at statement: $r8 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r5)
de.spiritcroc.defaultdarktheme_oms_53.apk                   => at statement: $r8 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r5)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 3
de.spiritcroc.darkcroc.substratum_11.apk                    => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer781, varReplacer782)
com.x1unix.s60icons_110.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer12564, varReplacer12565)
de.spiritcroc.defaultdarktheme_oms_53.apk                   => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer573, varReplacer574)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 3
de.spiritcroc.darkcroc.substratum_11.apk                    => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer781, varReplacer782)
com.x1unix.s60icons_110.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer12564, varReplacer12565)
de.spiritcroc.defaultdarktheme_oms_53.apk                   => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer573, varReplacer574)
```

For RequiredPredicateError, TP: it use following code to return value as salt. https://github.com/javiersantos/PiracyChecker/blob/cd0cbacc28cf84b3be271e230615d310c1548c26/library/src/main/java/com/github/javiersantos/piracychecker/utils/SaltUtils.kt#L26

For NeverTypeOfError, ITP: vain predicate.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#7
Class: org.spongycastle.cms.jcajce.EnvelopedDataHelper
Method: byte[] calculateDerivedKey(int,char[],org.spongycastle.asn1.x509.AlgorithmIdentifier,int)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 2
com.mschlauch.comfortreader_13.apk                          => at statement: specialinvoke $r14.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r1, $r9, $i0, $i1)
eu.pretix.pretixprint_37.apk                                => at statement: specialinvoke $r14.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r1, $r8, $i0, $i1)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 2
com.mschlauch.comfortreader_13.apk                          => at statement: specialinvoke $r14.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r1, $r9, $i0, $i1)
eu.pretix.pretixprint_37.apk                                => at statement: specialinvoke $r14.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r1, $r8, $i0, $i1)
```

For RequiredPredicateError, ITP: it is for decryption context, the salt is loaded from external source.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.


```
----------------------------------------------------------------------
#8
Class: org.eclipse.jgit.transport.WalkEncryption$ObjectEncryptionV2
Method: void <init>(java.lang.String,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 2
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, $i0, varReplacer21411)
com.madgag.agit_139000000.apk                               => at statement: specialinvoke r3.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r5, $i0, varReplacer12318)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 2
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, $i0, varReplacer21411)
com.madgag.agit_139000000.apk                               => at statement: specialinvoke r3.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r5, $i0, varReplacer12318)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 2
com.manichord.mgit_220.apk                                  => at statement: $r7 = virtualinvoke $r6.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r4)
com.madgag.agit_139000000.apk                               => at statement: $r7 = virtualinvoke $r6.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r3)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 2
com.manichord.mgit_220.apk                                  => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, $i0, varReplacer21411)
com.madgag.agit_139000000.apk                               => at statement: specialinvoke r3.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r5, $i0, varReplacer12318)
```

For RequiredPredicateError, TP.

For NeverTypeOfError, ITP: vain predicate.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.


```
----------------------------------------------------------------------
#9
Class: com.tozny.crypto.android.AesCbcWithIntegrity
Method: com.tozny.crypto.android.AesCbcWithIntegrity$SecretKeys generateKeyFromPassword(java.lang.String,byte[])

Error Type: RequiredPredicateError
Error Reason: Second parameter was not properly generated as randomized
Apk Num: 2
peanutencryption.peanutencryption_4.apk                     => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, varReplacer6674, varReplacer6675)
com.github.onetimepass_1002003.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, varReplacer4632, varReplacer4633)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 2
peanutencryption.peanutencryption_4.apk                     => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, varReplacer6674, varReplacer6675)
com.github.onetimepass_1002003.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, varReplacer4632, varReplacer4633)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type javax.crypto.spec.PBEKeySpec object not completed. Expected call to clearPassword
Apk Num: 2
peanutencryption.peanutencryption_4.apk                     => at statement: $r7 = virtualinvoke $r6.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>(r4)
com.github.onetimepass_1002003.apk                          => at statement: $r5 = virtualinvoke $r4.<javax.crypto.SecretKeyFactory: javax.crypto.SecretKey generateSecret(java.security.spec.KeySpec)>($r2)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 2
peanutencryption.peanutencryption_4.apk                     => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, varReplacer6674, varReplacer6675)
com.github.onetimepass_1002003.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r1, varReplacer4632, varReplacer4633)
```

For RequiredPredicateError, ITP: it either load salt from `settings.getString("passwordSalt", null);` or generate salt from `SecureRandom().nextBytes()`;

For NeverTypeOfError, ITP: vain predicate.

For IncompleteOperationError, ITP: Crysl require to call `clearPassword`. We argue that its threat model is not reasonable in Android context.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.


```
----------------------------------------------------------------------
#10
Class: com.gitlab.dibdib.common.TcvCodecAes
Method: byte[] getKey(byte[],byte[],byte[],int)

Error Type: NeverTypeOfError
Error Reason: First parameter should never be of type java.lang.String.
Apk Num: 2
net.sourceforge.dibdib.android.dib2qm_2275.apk              => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r4, $i0, varReplacer3660)
com.gitlab.dibdib.dib2calc_1262.apk                         => at statement: specialinvoke r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r3, $i0, varReplacer990)

Error Type: HardCodedError
Error Reason: First parameter should never be hardcoded.
Apk Num: 2
net.sourceforge.dibdib.android.dib2qm_2275.apk              => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r4, $i0, varReplacer3658)
com.gitlab.dibdib.dib2calc_1262.apk                         => at statement: specialinvoke r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r3, $i0, varReplacer990)

Error Type: ConstraintError
Error Reason: Third parameter (with value 0)Variable iterationCountmust be  at least 10000
Apk Num: 2
net.sourceforge.dibdib.android.dib2qm_2275.apk              => at statement: specialinvoke $r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r12, $r4, $i0, varReplacer3653)
com.gitlab.dibdib.dib2calc_1262.apk                         => at statement: specialinvoke r7.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r3, $i0, varReplacer990)
```

For NeverTypeOfError, ITP: vain predicate.

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testPBEKeySpec.

For ConstraintError, TP.


```
----------------------------------------------------------------------
#11
Class: p4.c
Method: javax.crypto.SecretKey c(java.lang.String,byte[],java.lang.String,java.lang.String,int)

Error Type: ConstraintError
Error Reason: Third parameter (with value 2020)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.machiav3lli.backup_7000.apk                             => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r1, varReplacer23995, varReplacer23996)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#21
Class: org.purple.smoke.Cryptography
Method: byte[] pbkdf2(byte[],char[],int,int)

Error Type: ConstraintError
Error Reason: Third parameter (with value 4096)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.purple.smoke_20211225.apk                               => at statement: specialinvoke $r1.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r0, $r3, $i0, $i1)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#27
Class: org.bouncycastle.openssl.jcajce.PEMUtilities
Method: javax.crypto.SecretKey getKey(org.bouncycastle.jcajce.util.JcaJceHelper,char[],java.lang.String,int,byte[],boolean)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.ubergeek42.WeechatAndroid_10701.apk                     => at statement: specialinvoke $r9.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r0, varReplacer35250, $i0)
```

For ConstraintError, TP.


```
----------------------------------------------------------------------
#32
Class: net.robotmedia.billing.utils.AESObfuscator
Method: void <init>(byte[],java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 1
net.androidcomics.acv_46.apk                                => at statement: specialinvoke r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer672, varReplacer673)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#39
Class: info.guardianproject.cacheword.PassphraseSecrets
Method: javax.crypto.spec.SecretKeySpec hashPassphrase(char[],byte[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 100)Variable iterationCountmust be  at least 10000
Apk Num: 1
info.guardianproject.notepadbot_12.apk                      => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r0, $r1, varReplacer7573, varReplacer7574)
```

For ConstraintError, TP.


```
----------------------------------------------------------------------
#42
Class: im.status.keycard.applet.Mnemonic
Method: byte[] toBinarySeed(java.lang.String,java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 2048)Variable iterationCountmust be  at least 10000
Apk Num: 1
im.status.ethereum_2022011816.apk                           => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r7, varReplacer5142, varReplacer5143)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#43
Class: im.status.keycard.applet.KeycardCommandSet
Method: byte[] pairingPasswordToSecret(java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 10)Variable iterationCountmust be  at least 10000
Apk Num: 1
im.status.ethereum_2022011816.apk                           => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r6, $i0, varReplacer28269)
```

For ConstraintError, TP.


```
----------------------------------------------------------------------
#45
Class: global.msnthrp.xvii.core.crypto.algorithm.Pbkdf2HmacSha1
Method: byte[] deriveFromKey(java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r3, $r4, varReplacer23364, varReplacer23365)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#50
Class: de.jepfa.yapm.service.secret.SecretService
Method: de.jepfa.yapm.model.secret.SecretKeyHolder generatePBESecretKey(de.jepfa.yapm.model.secret.Password,de.jepfa.yapm.model.secret.Key,int,de.jepfa.yapm.model.encrypted.CipherAlgorithm)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
de.jepfa.yapm_105004.apk                                    => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r6, $i0, $i1)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#51
Class: de.idyl.winzipaes.impl.AESUtilsJCA
Method: void <init>(java.lang.String,int,byte[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.rareventure.gps2_91.apk                                 => at statement: specialinvoke $r18.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r6, $r2, varReplacer14179, $i1)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#56
Class: com.rareventure.android.Crypt
Method: byte[] getRawKey(java.lang.String,byte[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 2048)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.rareventure.gps2_91.apk                                 => at statement: specialinvoke $r0.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r2, $s0, $i1)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#57
Class: com.notecrypt.utils.Cryptox
Method: byte[] a(java.lang.String,byte[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.notecryptpro_22.apk                                     => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r5, $r1, varReplacer4554, varReplacer4555)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#59
Class: com.google.android.vending.licensing.a
Method: void <init>(byte[],java.lang.String,java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.totschnig.myexpenses_505.apk                            => at statement: specialinvoke $r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r7, $r1, varReplacer36057, varReplacer36058)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#60
Class: com.google.android.vending.licensing.AESObfuscator
Method: void <init>(byte[],java.lang.String,java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 1
org.materialos.icons_10.apk                                 => at statement: specialinvoke r5.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r9, $r1, varReplacer11756, varReplacer11757)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#66
Class: com.beemdevelopment.aegis.importers.AuthyImporter$EncryptedState
Method: com.beemdevelopment.aegis.importers.AuthyImporter$DecryptedState decrypt(char[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.beemdevelopment.aegis_50.apk                            => at statement: specialinvoke $r15.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r1, $r7, varReplacer23490, varReplacer23491)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#68
Class: com.akop.bach.Preferences
Method: void initCryptors(android.content.Context)

Error Type: ConstraintError
Error Reason: Third parameter (with value 1024)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.akop.bach_120.apk                                       => at statement: specialinvoke r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r10, $r11, varReplacer1307, varReplacer1308)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#69
Class: com.aidinhut.simpletextcrypt.Crypter
Method: javax.crypto.SecretKey deriveKey(java.lang.String,java.lang.String)

Error Type: ConstraintError
Error Reason: Third parameter (with value 2000)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.aidinhut.simpletextcrypt_12.apk                         => at statement: specialinvoke $r4.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r2, $r5, varReplacer246, varReplacer247)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.


```
----------------------------------------------------------------------
#72
Class: b.c.b.a.e$a
Method: byte[] a(javax.crypto.SecretKeyFactory,char[],byte[])

Error Type: ConstraintError
Error Reason: Third parameter (with value 1000)Variable iterationCountmust be  at least 10000
Apk Num: 1
com.yubico.yubioath_20199.apk                               => at statement: specialinvoke $r2.<javax.crypto.spec.PBEKeySpec: void <init>(char[],byte[],int,int)>($r4, $r1, varReplacer7537, varReplacer7538)
```

For ConstraintError, ITP: RFC only requires iteration count in PBE to at least 1000. pls refer to https://www.rfc-editor.org/rfc/inline-errata/rfc8018.html.