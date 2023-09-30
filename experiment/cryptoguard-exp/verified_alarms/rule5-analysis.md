Rule: 5 Used export grade public Key

------------------------------------------------
```
#1
Class: io.jsonwebtoken.impl.crypto.RsaProvider
Method: java.security.KeyPair generateKeyPair(java.lang.String,int,java.security.SecureRandom)
Apk Num:8

Apk:im.vector.app_40103150.apk
Err: Cause: Used default key size

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Cause: Used default key size

Apk:com.dimtion.shaarlier_33.apk
Err: Cause: Used default key size

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Cause: Used default key size

Apk:ch.corona.tracing_20010.apk
Err: Cause: Used default key size

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Cause: Used default key size

Apk:de.spiritcroc.riotx_40100720.apk
Err: Cause: Used default key size

Apk:app.tice.TICE.production_38.apk
Err: Cause: Used default key size

Misuse Num:8
```

ITP: In summary, CryptoGuard always takes the final statement in the directed graph as the slicing result for the entire method. `KeyPairGenerator.getInstance()` would result in another branch that throws `NoSuchAlgorithmException` exception without calling `initialize` next, which caused such false alarm.

------------------------------------------------
```
#2
Class: okhttp3.tls.HeldCertificate$Builder
Method: okhttp3.tls.HeldCertificate$Builder ecdsa256()
Apk Num:4

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "256"
Err: Found: "256"

Apk:com.duckduckgo.mobile.android_51080000.apk
Err: Found: "256"
Err: Found: "256"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "256"
Err: Found: "256"

Apk:app.tice.TICE.production_38.apk
Err: Found: "256"
Err: Found: "256"

Misuse Num:8
```

ITP: 512 key size for EC is unfair compared to RSA-2048.

------------------------------------------------
```
#3
Class: io.netty.handler.ssl.util.SelfSignedCertificate
Method: void <init>(java.lang.String,java.util.Date,java.util.Date)
Apk Num:2

Apk:com.greenaddress.greenbits_android_wallet.testnet_205.apk
Err: Found: "1024"

Apk:com.itds.sms.ping_6.apk
Err: Found: "1024"

Misuse Num:2
```

TP

------------------------------------------------
```
#4
Class: okhttp3.tls.internal.TlsUtil$localhost$2
Method: java.lang.Object invoke()
Apk Num:1

Apk:fr.gouv.android.stopcovid_448.apk
Err: Found: "256"

Misuse Num:1
```

ITP: 512 key size for EC is unfair compared to RSA-2048.

------------------------------------------------
```
#5
Class: o5.c$a
Method: java.lang.Object c()
Apk Num:1

Apk:io.vertretungsplan.client.android_5.apk
Err: Found: "256"

Misuse Num:1
```

ITP: 512 key size for EC is unfair compared to RSA-2048.

------------------------------------------------
```
#6
Class: net.majorkernelpanic.http.ModSSL$X509KeyManager
Method: void <init>(char[],java.lang.String)
Apk Num:1

Apk:net.majorkernelpanic.spydroid_1000.apk
Err: Found: "1024"

Misuse Num:1
```

TP

------------------------------------------------
```
#7
Class: net.majorkernelpanic.http.ModSSL$X509KeyManager
Method: java.lang.String chooseServerAlias(java.lang.String,java.security.Principal[],java.net.Socket)
Apk Num:1

Apk:net.majorkernelpanic.spydroid_1000.apk
Err: Found: "1024"

Misuse Num:1
```

TP

------------------------------------------------
```
#8
Class: n9.c$a
Method: n9.c$a d()
Apk Num:1

Apk:io.timelimit.android.aosp.direct_177.apk
Err: Found: "256"

Misuse Num:1
```

ITP: 512 key size for EC is unfair compared to RSA-2048.

------------------------------------------------
```
#9
Class: com.jonbanjo.cupsprint.CertificateActivity$3
Method: void onClick(android.content.DialogInterface,int)
Apk Num:1

Apk:com.jonbanjo.cupsprintservice_23.apk
Err: Found: "1024"

Misuse Num:1
```

TP

------------------------------------------------
```
#10
Class: com.gitlab.dibdib.dib2qm.EcDhQm
Method: boolean createDhKey(java.lang.String,char)
Apk Num:1

Apk:net.sourceforge.dibdib.android.dib2qm_2275.apk
Err: Found: "256"

Misuse Num:1
```

ITP: 512 key size for EC is unfair compared to RSA-2048.

------------------------------------------------
```
#11
Class: app.trigger.ssh.GenerateIdentityTask
Method: java.lang.String doInBackground(java.lang.Object[])
Apk Num:1

Apk:com.example.trigger_336.apk
Err: Found: "384"
Err: Found: "256"
Err: Found: "1024"
Err: Found: "384"
Err: Found: "256"

Misuse Num:5
```

4 ITP and 1 TP.

```java
protected String doInBackground(Object... params) {
    if (params.length != 1) {
        Log.e(TAG, "Unexpected number of params.");
        return "Internal Error";
    }

    try {
        String type = (String) params[0];

        if (type.equals("ED25519")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_ED25519, 256);
        } else if (type.equals("ECDSA-384")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_EC, 384);
        } else if (type.equals("ECDSA-521")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_EC, 521);
        } else if (type.equals("RSA-2048")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_RSA, 2048);
        } else if (type.equals("RSA-4096")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_RSA, 4096);
        } else if (type.equals("DSA-1024")) {
            keypair = createKeyPair(KeyPairBean.KEY_TYPE_DSA, 1024);
        } else {
            return "Unknown key type: " + type;
        }
    } catch (Exception e) {
        return e.getMessage();
    }

    return "Done";
}
```