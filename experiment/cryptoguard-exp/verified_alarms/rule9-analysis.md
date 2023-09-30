Rule: 9 Found constant salts in code

------------------------------------------------
```
#1
Class: org.eclipse.jgit.transport.WalkEncryption$ObjectEncryptionV2
Method: void <clinit>()
Apk Num:6

Apk:com.manichord.mgit_220.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Apk:com.jbirdvegas.mgerrit_2111084.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Apk:io.github.lonamiwebs.stringlate_1007.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Apk:com.coste.syncorg_10.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Apk:com.madgag.agit_139000000.apk
Err: Found: "-56"
Err: Found: "19"
Err: Found: "-107"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "-13"

Misuse Num:48
```

TP

------------------------------------------------
```
#2
Class: im.status.keycard.applet.KeycardCommandSet
Method: byte[] pairingPasswordToSecret(java.lang.String)
Apk Num:2

Apk:org.walleth_514.apk
Err: Found: "Keycard Pairing Password Salt"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "Keycard Pairing Password Salt"

Misuse Num:2
```

TP

------------------------------------------------
```
#3
Class: s9.k5$c
Method: void <clinit>()
Apk Num:1

Apk:com.orgzly_161.apk
Err: Found: "-56"
Err: Found: "-92"
Err: Found: "52"
Err: Found: "19"
Err: Found: "-13"
Err: Found: "11"
Err: Found: "-42"
Err: Found: "-107"

Misuse Num:8
```

TP

------------------------------------------------
```
#4
Class: org.smssecure.smssecure.crypto.MasterSecretUtil
Method: org.smssecure.smssecure.crypto.MasterSecret getMasterSecret(android.content.Context,java.lang.String)
Apk Num:1

Apk:org.smssecure.smssecure_145.apk
Err: Found: "AES"
Err: Found: "HmacSHA1"

Misuse Num:2
```

FP: shallow orthogonal slicing (HeuristicBasedInstructionSlicer problem)

------------------------------------------------
```
#5
Class: org.picketbox.datasource.security.PBEIdentityLoginModule
Method: void main(java.lang.String[])
Apk Num:1

Apk:org.lumicall.android_192.apk
Err: Found: "jaas is the way"

Misuse Num:1
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#6
Class: org.picketbox.datasource.security.PBEIdentityLoginModule
Method: void <init>(java.lang.String,char[],byte[],int)
Apk Num:1

Apk:org.lumicall.android_192.apk
Err: Found: "3"
Err: Found: "11"
Err: Found: "9"
Err: Found: "13"
Err: Found: "7"
Err: Found: "2"
Err: Found: "4"
Err: Found: "1"

Misuse Num:8
```

TP

------------------------------------------------
```
#7
Class: org.picketbox.datasource.security.PBEIdentityLoginModule
Method: void <init>()
Apk Num:1

Apk:org.lumicall.android_192.apk
Err: Found: "4"
Err: Found: "1"
Err: Found: "11"
Err: Found: "7"
Err: Found: "3"
Err: Found: "13"
Err: Found: "9"
Err: Found: "2"

Misuse Num:8
```

TP

------------------------------------------------
```
#8
Class: me.sheimi.android.utils.SecurePrefsHelper
Method: void <init>(android.content.Context)
Apk Num:1

Apk:com.manichord.mgit_220.apk
Err: Found: "sec_prefs.xml"

Misuse Num:1
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#9
Class: info.guardianproject.pixelknot.StegoDecryptionJob$2
Method: void run()
Apk Num:1

Apk:info.guardianproject.pixelknot_101.apk
Err: Found: "----* PK v 1.0 REQUIRES PASSWORD ----*"

Misuse Num:1
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#10
Class: im.status.ethereum.keycard.SmartCardSecrets
Method: im.status.ethereum.keycard.SmartCardSecrets generate(java.lang.String)
Apk Num:1

Apk:im.status.ethereum_2022011816.apk
Err: Found: "KeycardDefaultPairing"

Misuse Num:1
```

FP: broken def-use chains due to intervening definitions.