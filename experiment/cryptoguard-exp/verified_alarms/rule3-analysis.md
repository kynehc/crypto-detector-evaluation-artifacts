Rule: 3 Used constant keys in code

------------------------------------------------
```
#1
Class: org.bouncycastle.operator.jcajce.OperatorUtils
Method: java.security.Key getJceKey(org.bouncycastle.operator.GenericKey)
Apk Num:16

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: Constant "ENC"

Apk:eu.faircode.email_1818.apk
Err: Found: Constant "ENC"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: Constant "ENC"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: Constant "ENC"

Apk:me.bgregos.brighttask_16.apk
Err: Found: Constant "ENC"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: Constant "ENC"

Apk:com.nextcloud.android.beta_20220122.apk
Err: Found: Constant "ENC"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: Constant "ENC"

Apk:com.tananaev.passportreader_16.apk
Err: Found: Constant "ENC"

Apk:com.nextcloud.client_30180190.apk
Err: Found: Constant "ENC"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: Constant "ENC"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: Constant "ENC"

Apk:org.atalk.android_208010.apk
Err: Found: Constant "ENC"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: Constant "ENC"

Apk:org.primftpd_55.apk
Err: Found: Constant "ENC"

Apk:org.fdroid.nearby_2.apk
Err: Found: Constant "ENC"

Misuse Num:16
```

FP: Shallow orthogonal slicing and cgd's `HeuristicBasedInstructionSlicer` will take any constants that in the def-use chains of `return` stmt of the orthogonal method (the invocation stmt).

------------------------------------------------
```
#2
Class: org.apache.commons.httpclient.auth.NTLM
Method: byte[] hashPassword(java.lang.String,byte[])
Apk Num:11

Apk:nl.mpcjanssen.simpletask.nextcloud_10009003.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:org.documentfoundation.libreoffice_11.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Apk:com.spisoft.quicknote_241.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.averi.worldscribe_27.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.bytesforge.linkasanote_30499.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:net.oschina.app_18.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Apk:com.nextcloud.android.beta_20220122.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.nextcloud.client_30180190.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:theakki.synctool_100.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:org.aykit.MyOwnNotes_11.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Misuse Num:110
```

FP: broken def-use chains due to intervening definitions.

here, `<org.apache.commons.httpclient.auth.NTLM: byte[] hashPassword(java.lang.String,byte[])>` jimple code like this:

```
private byte[] hashPassword(java.lang.String, byte[]) throws org.apache.commons.httpclient.auth.AuthenticationException
    {
        org.apache.commons.httpclient.auth.NTLM $r0;
        java.lang.String $r1, $r6;
        byte[] $r2, $r3, $r4, $r5;
        int $i0, $i1, $i3;
        byte $b2;

        $r0 := @this: org.apache.commons.httpclient.auth.NTLM;

        $r1 := @parameter0: java.lang.String;

        $r2 := @parameter1: byte[];

        $r1 = virtualinvoke $r1.<java.lang.String: java.lang.String toUpperCase()>();

        $r6 = $r0.<org.apache.commons.httpclient.auth.NTLM: java.lang.String credentialCharset>;

        $r5 = staticinvoke <org.apache.commons.httpclient.util.EncodingUtil: byte[] getBytes(java.lang.String,java.lang.String)>($r1, $r6);

        $r4 = newarray (byte)[7];

        $r3 = newarray (byte)[7];

        $i0 = lengthof $r5;

        if $i0 <= 7 goto label01;

        $i0 = 7;

     label01:
        $i1 = 0;

     label02:
        if $i1 >= $i0 goto label03;

        $b2 = $r5[$i1];

        $r4[$i1] = $b2;

        $i1 = $i1 + 1;

        goto label02;

     label03:
        if $i1 >= 7 goto label04;

        $r4[$i1] = 0;

        $i1 = $i1 + 1;

        goto label03;

     label04:
        $i1 = lengthof $r5;

        if $i1 <= 14 goto label05;

        $i1 = 14;

     label05:
        $i0 = 7;

     label06:
        if $i0 >= $i1 goto label07;

        $i3 = $i0 + -7;

        $b2 = $r5[$i0];

        $r3[$i3] = $b2;

        $i0 = $i0 + 1;

        goto label06;

     label07:
        if $i0 >= 14 goto label08;

        $i1 = $i0 + -7;

        $r3[$i1] = 0;

        $i0 = $i0 + 1;

        goto label07;

     label08:
        $r5 = newarray (byte)[8];

        $r5[0] = 75;

        $r5[1] = 71;

        $r5[2] = 83;

        $r5[3] = 33;

        $r5[4] = 64;

        $r5[5] = 35;

        $r5[6] = 36;

        $r5[7] = 37;

        $r4 = specialinvoke $r0.<org.apache.commons.httpclient.auth.NTLM: byte[] encrypt(byte[],byte[])>($r4, $r5);

        $r5 = specialinvoke $r0.<org.apache.commons.httpclient.auth.NTLM: byte[] encrypt(byte[],byte[])>($r3, $r5);

        $r3 = newarray (byte)[21];

        $i0 = 0;

     label09:
        $i1 = lengthof $r4;

        if $i0 >= $i1 goto label10;

        $b2 = $r4[$i0];

        $r3[$i0] = $b2;

        $i0 = $i0 + 1;

        goto label09;

     label10:
        $i0 = 0;

     label11:
        $i1 = lengthof $r5;

        if $i0 >= $i1 goto label12;

        $i1 = $i0 + 8;

        $b2 = $r5[$i0];

        $r3[$i1] = $b2;

        $i0 = $i0 + 1;

        goto label11;

     label12:
        $i0 = 0;

     label13:
        if $i0 >= 5 goto label14;

        $i1 = $i0 + 16;

        $r3[$i1] = 0;

        $i0 = $i0 + 1;

        goto label13;

     label14:
        $r4 = newarray (byte)[24];

        specialinvoke $r0.<org.apache.commons.httpclient.auth.NTLM: void calcResp(byte[],byte[],byte[])>($r3, $r2, $r4);

        return $r4;
    }
```

The slicing criteria is `$r3` in `specialinvoke $r0.<org.apache.commons.httpclient.auth.NTLM: void calcResp(byte[],byte[],byte[])>($r3, $r2, $r4);`. We can backward slice to add `$r3[$i1] = 0;`, `$r3[$i1] = $b2;`, `$r3[$i0] = $b2;` into outSet. Then `$b2` will bring in `$b2 = $r5[$i0];`, where `$r5` represents `byte[] lmHpw2`. However, `$r5` also was reassigned as `byte[] magic`, which is this magic string `KGS!@#$%`. This wrongly bring into `$r5[0] = 75;$r5[1] = 71;$r5[2] = 83;$r5[3] = 33;$r5[4] = 64;$r5[5] = 35;$r5[6] = 36;$r5[7] = 37;`.

------------------------------------------------
```
#3
Class: org.apache.commons.compress.archivers.sevenz.AES256SHA256Decoder$1
Method: javax.crypto.CipherInputStream init()
Apk Num:11

Apk:de.thecode.lmd_3100300.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:de.ccc.events.badge.card10_9.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:de.thecode.android.tazreader_3140000.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:tech.ula_7438725.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:org.mupen64plusae.v3.alpha_246.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:com.ichi2.anki_21506300.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:com.nkanaev.comics_7.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:net.osmand.plus_421.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:com.amaze.filemanager_54.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:com.renard.ocr_82.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Apk:org.yausername.dvd_10301.apk
Err: Found: Constant "1L"
Err: Found: Constant "0L"
Err: Found: Constant "1L"

Misuse Num:33
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#4
Class: net.lingala.zip4j.crypto.AESDecrypter
Method: byte[] deriveKey(byte[],char[])
Apk Num:9

Apk:io.mrarm.irc_12.apk
Err: Found: Constant "ISO-8859-1"

Apk:it.feio.android.omninotes.foss_247.apk
Err: Found: Constant "ISO-8859-1"

Apk:me.bpear.archonpackager_17.apk
Err: Found: Constant "ISO-8859-1"

Apk:com.github.axet.bookreader_408.apk
Err: Found: Constant "ISO-8859-1"

Apk:com.github.axet.torrentclient_711.apk
Err: Found: Constant "ISO-8859-1"

Apk:at.jclehner.rxdroid_9342.apk
Err: Found: Constant "ISO-8859-1"

Apk:fluddokt.opsu.android_2.apk
Err: Found: Constant "ISO-8859-1"

Apk:com.oriondev.moneywallet_75.apk
Err: Found: Constant "ISO-8859-1"

Apk:me.anon.grow_2630.apk
Err: Found: Constant "ISO-8859-1"

Misuse Num:9
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#5
Class: org.whispersystems.libsignal.ratchet.ChainKey
Method: void <clinit>()
Apk Num:8

Apk:com.dx.anonymousmessenger_46.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:org.smssecure.smssecure_145.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:com.cweb.messenger_42012.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:im.quicksy.client_42023.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:org.snikket.android_42024.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:eu.siacs.conversations_42023.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Apk:org.atalk.android_208010.apk
Err: Found: Constant "2"
Err: Found: Constant "1"

Misuse Num:16
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#6
Class: org.bouncycastle.math.ec.ECPoint
Method: byte[] getEncoded(boolean)
Apk Num:7

Apk:org.kontalk_500.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:org.atalk.android_208010.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Apk:org.primftpd_55.apk
Err: Found: Constant "4"
Err: Found: Constant "2"
Err: Found: Constant "3"

Misuse Num:21
```

FP: This is because of the exaggerated string matching for array variables in cryptoguard.

------------------------------------------------
```
#7
Class: net.lingala.zip4j.crypto.AESEncrpyter
Method: byte[] deriveKey(byte[],char[])
Apk Num:6

Apk:io.mrarm.irc_12.apk
Err: Found: Constant "ISO-8859-1"

Apk:me.bpear.archonpackager_17.apk
Err: Found: Constant "ISO-8859-1"

Apk:at.jclehner.rxdroid_9342.apk
Err: Found: Constant "ISO-8859-1"

Apk:fluddokt.opsu.android_2.apk
Err: Found: Constant "ISO-8859-1"

Apk:com.oriondev.moneywallet_75.apk
Err: Found: Constant "ISO-8859-1"

Apk:me.anon.grow_2630.apk
Err: Found: Constant "ISO-8859-1"

Misuse Num:6
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#8
Class: org.whispersystems.libsignal.groups.ratchet.SenderChainKey
Method: void <clinit>()
Apk Num:4

Apk:com.dx.anonymousmessenger_46.apk
Err: Found: Constant "1"
Err: Found: Constant "2"

Apk:org.smssecure.smssecure_145.apk
Err: Found: Constant "1"
Err: Found: Constant "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: Constant "1"
Err: Found: Constant "2"

Apk:org.atalk.android_208010.apk
Err: Found: Constant "1"
Err: Found: Constant "2"

Misuse Num:8
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#9
Class: com.trilead.ssh2.crypto.Base64
Method: byte[] decode(char[])
Apk Num:4

Apk:org.connectbot_10908000.apk
Err: Found: Constant "62"
Err: Found: Constant "64"
Err: Found: Constant "63"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: Constant "63"
Err: Found: Constant "62"
Err: Found: Constant "64"

Apk:com.example.trigger_336.apk
Err: Found: Constant "62"
Err: Found: Constant "64"
Err: Found: Constant "63"

Apk:com.gaurav.avnc_8.apk
Err: Found: Constant "62"
Err: Found: Constant "64"
Err: Found: Constant "63"

Misuse Num:12
```

FP: Shallow orthogonal slicing and cgd's `HeuristicBasedInstructionSlicer` will take any constants that in the def-use chains of `return` stmt of the orthogonal method (the invocation stmt).

------------------------------------------------
```
#10
Class: org.apache.commons.vfs2.util.DefaultCryptor
Method: void <clinit>()
Apk Num:3

Apk:com.foxdebug.acode_164.apk
Err: Found: Constant "104"
Err: Found: Constant "111"
Err: Found: Constant "109"
Err: Found: Constant "65"
Err: Found: Constant "83"
Err: Found: Constant "110"
Err: Found: Constant "115"
Err: Found: Constant "99"
Err: Found: Constant "86"
Err: Found: Constant "109"
Err: Found: Constant "97"
Err: Found: Constant "70"
Err: Found: Constant "111"
Err: Found: Constant "112"
Err: Found: Constant "67"
Err: Found: Constant "101"

Apk:com.nkanaev.comics_7.apk
Err: Found: Constant "104"
Err: Found: Constant "111"
Err: Found: Constant "109"
Err: Found: Constant "65"
Err: Found: Constant "83"
Err: Found: Constant "110"
Err: Found: Constant "115"
Err: Found: Constant "99"
Err: Found: Constant "86"
Err: Found: Constant "109"
Err: Found: Constant "97"
Err: Found: Constant "70"
Err: Found: Constant "111"
Err: Found: Constant "112"
Err: Found: Constant "67"
Err: Found: Constant "101"

Apk:com.amaze.filemanager_54.apk
Err: Found: Constant "104"
Err: Found: Constant "111"
Err: Found: Constant "109"
Err: Found: Constant "65"
Err: Found: Constant "83"
Err: Found: Constant "110"
Err: Found: Constant "115"
Err: Found: Constant "99"
Err: Found: Constant "86"
Err: Found: Constant "109"
Err: Found: Constant "97"
Err: Found: Constant "70"
Err: Found: Constant "111"
Err: Found: Constant "112"
Err: Found: Constant "67"
Err: Found: Constant "101"

Misuse Num:48
```

TP: https://github.com/apache/commons-vfs/blob/41b5278c66076a08ba934540c4d0049541f6201f/commons-vfs2/src/main/java/org/apache/commons/vfs2/util/DefaultCryptor.java.

------------------------------------------------
```
#47
Class: org.sufficientlysecure.keychain.securitytoken.SCP11bSecureMessaging
Method: org.sufficientlysecure.keychain.securitytoken.SecureMessaging establish(org.sufficientlysecure.keychain.securitytoken.SecurityTokenConnection,android.content.Context,org.sufficientlysecure.keychain.securitytoken.OpenPgpCommandApduFactory)
Apk Num:1

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: Constant "16"


Misuse Num:1
```

FP: This is because of the exaggerated string matching for array variables in cryptoguard.

------------------------------------------------
```
#62
Class: com.tom_roush.pdfbox.pdmodel.encryption.StandardSecurityHandler
Method: byte[] computeHash2B(byte[],byte[],byte[])
Apk Num:1

Apk:eu.pretix.pretixprint_37.apk
Err: Found: Constant "3"

Misuse Num:1
```

FP: Shallow orthogonal slicing and cgd's `HeuristicBasedInstructionSlicer` will take any constants that in the def-use chains of `return` stmt of the orthogonal method (the invocation stmt).

------------------------------------------------
```
#138
Class: de.cotech.hw.openpgp.internal.securemessaging.Scp11bSecureMessaging
Method: de.cotech.hw.openpgp.internal.securemessaging.SecureMessaging establish(de.cotech.hw.openpgp.internal.OpenPgpAppletConnection,de.cotech.hw.openpgp.internal.OpenPgpCommandApduFactory,java.security.KeyStore)
Apk Num:1

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: Constant "16"


Misuse Num:1
```

FP: This is because of the exaggerated string matching for array variables in cryptoguard.