Rule: 8 Used < 1000 iteration for PBE

------------------------------------------------
```
#1
Class: org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi$StoreEntry
Method: void <init>(org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi,java.lang.String,java.security.cert.Certificate)
Apk Num:45

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "1"

Apk:org.kontalk_500.apk
Err: Found: "1"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "1"

Apk:eu.faircode.email_1818.apk
Err: Found: "1"

Apk:org.walleth_514.apk
Err: Found: "1"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "1"

Apk:org.pacien.tincapp_33.apk
Err: Found: "1"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "1"

Apk:app.crescentcash.src_120.apk
Err: Found: "1"

Apk:com.vsmartcard.acardemulator_6.apk
Err: Found: "1"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "1"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "1"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "1"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "1"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "1"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "1"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "1"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "1"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "1"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "1"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "1"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "1"

Apk:com.eventyay.attendee_17.apk
Err: Found: "1"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "1"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "1"

Apk:de.rki.covpass.app_711.apk
Err: Found: "1"

Apk:rs.ltt.android_11.apk
Err: Found: "1"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "1"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "1"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "1"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "1"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "1"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "1"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "1"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "1"

Apk:net.osmand.plus_421.apk
Err: Found: "1"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "1"

Apk:it.greenaddress.cordova_72.apk
Err: Found: "1"

Apk:org.primftpd_55.apk
Err: Found: "1"

Apk:com.dimension.tessercube_200.apk
Err: Found: "1"

Apk:com.btcontract.wallet_95.apk
Err: Found: "1"

Apk:org.fdroid.nearby_2.apk
Err: Found: "1"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "1"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "1"

Apk:com.hasi.hasid00r_3.apk
Err: Found: "1"

Misuse Num:45
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#2
Class: org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi$StoreEntry
Method: void <init>(org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi,java.lang.String,java.security.Key,char[],java.security.cert.Certificate[])
Apk Num:45

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "4"

Apk:org.kontalk_500.apk
Err: Found: "4"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "4"

Apk:eu.faircode.email_1818.apk
Err: Found: "4"

Apk:org.walleth_514.apk
Err: Found: "4"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "4"

Apk:org.pacien.tincapp_33.apk
Err: Found: "4"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "4"

Apk:app.crescentcash.src_120.apk
Err: Found: "4"

Apk:com.vsmartcard.acardemulator_6.apk
Err: Found: "4"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "4"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "4"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "4"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "4"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "4"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "4"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "4"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "4"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "4"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "4"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "4"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "4"

Apk:com.eventyay.attendee_17.apk
Err: Found: "4"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "4"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "4"

Apk:de.rki.covpass.app_711.apk
Err: Found: "4"

Apk:rs.ltt.android_11.apk
Err: Found: "4"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "4"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "4"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "4"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "4"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "4"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "4"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "4"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "4"

Apk:net.osmand.plus_421.apk
Err: Found: "4"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "4"

Apk:it.greenaddress.cordova_72.apk
Err: Found: "4"

Apk:org.primftpd_55.apk
Err: Found: "4"

Apk:com.dimension.tessercube_200.apk
Err: Found: "4"

Apk:com.btcontract.wallet_95.apk
Err: Found: "4"

Apk:org.fdroid.nearby_2.apk
Err: Found: "4"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "4"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "4"

Apk:com.hasi.hasid00r_3.apk
Err: Found: "4"

Misuse Num:45
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#3
Class: org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi$StoreEntry
Method: void <init>(org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi,java.lang.String,byte[],java.security.cert.Certificate[])
Apk Num:45

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "3"

Apk:org.kontalk_500.apk
Err: Found: "3"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "3"

Apk:eu.faircode.email_1818.apk
Err: Found: "3"

Apk:org.walleth_514.apk
Err: Found: "3"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "3"

Apk:org.pacien.tincapp_33.apk
Err: Found: "3"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "3"

Apk:app.crescentcash.src_120.apk
Err: Found: "3"

Apk:com.vsmartcard.acardemulator_6.apk
Err: Found: "3"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "3"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "3"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "3"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "3"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "3"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "3"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "3"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "3"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "3"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "3"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "3"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "3"

Apk:com.eventyay.attendee_17.apk
Err: Found: "3"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "3"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "3"

Apk:de.rki.covpass.app_711.apk
Err: Found: "3"

Apk:rs.ltt.android_11.apk
Err: Found: "3"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "3"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "3"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "3"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "3"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "3"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "3"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "3"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "3"

Apk:net.osmand.plus_421.apk
Err: Found: "3"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "3"

Apk:it.greenaddress.cordova_72.apk
Err: Found: "3"

Apk:org.primftpd_55.apk
Err: Found: "3"

Apk:com.dimension.tessercube_200.apk
Err: Found: "3"

Apk:com.btcontract.wallet_95.apk
Err: Found: "3"

Apk:org.fdroid.nearby_2.apk
Err: Found: "3"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "3"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "3"

Apk:com.hasi.hasid00r_3.apk
Err: Found: "3"

Misuse Num:45
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#4
Class: org.bouncycastle.jcajce.provider.keystore.bc.BcKeyStoreSpi
Method: void loadStore(java.io.InputStream)
Apk Num:45

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.kontalk_500.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "1"
Err: Found: "2"

Apk:eu.faircode.email_1818.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.walleth_514.apk
Err: Found: "1"
Err: Found: "2"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.pacien.tincapp_33.apk
Err: Found: "1"
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "1"
Err: Found: "2"

Apk:app.crescentcash.src_120.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.vsmartcard.acardemulator_6.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "1"
Err: Found: "2"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "1"
Err: Found: "2"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "1"
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "1"
Err: Found: "2"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "1"
Err: Found: "2"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "1"
Err: Found: "2"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "1"
Err: Found: "2"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.eventyay.attendee_17.apk
Err: Found: "1"
Err: Found: "2"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "1"
Err: Found: "2"

Apk:de.rki.covpass.app_711.apk
Err: Found: "1"
Err: Found: "2"

Apk:rs.ltt.android_11.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "1"
Err: Found: "2"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "1"
Err: Found: "2"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "1"
Err: Found: "2"

Apk:net.osmand.plus_421.apk
Err: Found: "1"
Err: Found: "2"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "1"
Err: Found: "2"

Apk:it.greenaddress.cordova_72.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.primftpd_55.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.dimension.tessercube_200.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.btcontract.wallet_95.apk
Err: Found: "1"
Err: Found: "2"

Apk:org.fdroid.nearby_2.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "1"
Err: Found: "2"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "1"
Err: Found: "2"

Apk:com.hasi.hasid00r_3.apk
Err: Found: "1"
Err: Found: "2"

Misuse Num:90
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#5
Class: org.bouncycastle.jcajce.provider.symmetric.Twofish$PBEWithSHA
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "2"

Apk:org.kontalk_500.apk
Err: Found: "2"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "2"

Apk:eu.faircode.email_1818.apk
Err: Found: "2"

Apk:org.walleth_514.apk
Err: Found: "2"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "2"

Apk:org.pacien.tincapp_33.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "2"

Apk:app.crescentcash.src_120.apk
Err: Found: "2"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "2"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "2"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "2"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "2"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "2"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "2"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "2"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "2"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "2"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "2"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "2"

Apk:com.eventyay.attendee_17.apk
Err: Found: "2"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "2"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "2"

Apk:de.rki.covpass.app_711.apk
Err: Found: "2"

Apk:rs.ltt.android_11.apk
Err: Found: "2"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "2"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "2"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "2"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "2"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "2"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "2"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "2"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "2"

Apk:com.limelight_271.apk
Err: Found: "2"

Apk:net.osmand.plus_421.apk
Err: Found: "2"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "2"

Apk:org.primftpd_55.apk
Err: Found: "2"

Apk:com.dimension.tessercube_200.apk
Err: Found: "2"

Apk:com.btcontract.wallet_95.apk
Err: Found: "2"

Apk:org.fdroid.nearby_2.apk
Err: Found: "2"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "2"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "2"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#6
Class: org.bouncycastle.jcajce.provider.symmetric.RC2$PBEWithSHAAnd40BitRC2
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "2"

Apk:org.kontalk_500.apk
Err: Found: "2"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "2"

Apk:eu.faircode.email_1818.apk
Err: Found: "2"

Apk:org.walleth_514.apk
Err: Found: "2"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "2"

Apk:org.pacien.tincapp_33.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "2"

Apk:app.crescentcash.src_120.apk
Err: Found: "2"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "2"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "2"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "2"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "2"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "2"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "2"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "2"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "2"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "2"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "2"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "2"

Apk:com.eventyay.attendee_17.apk
Err: Found: "2"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "2"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "2"

Apk:de.rki.covpass.app_711.apk
Err: Found: "2"

Apk:rs.ltt.android_11.apk
Err: Found: "2"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "2"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "2"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "2"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "2"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "2"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "2"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "2"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "2"

Apk:com.limelight_271.apk
Err: Found: "2"

Apk:net.osmand.plus_421.apk
Err: Found: "2"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "2"

Apk:org.primftpd_55.apk
Err: Found: "2"

Apk:com.dimension.tessercube_200.apk
Err: Found: "2"

Apk:com.btcontract.wallet_95.apk
Err: Found: "2"

Apk:org.fdroid.nearby_2.apk
Err: Found: "2"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "2"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "2"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#7
Class: org.bouncycastle.jcajce.provider.symmetric.RC2$PBEWithSHAAnd128BitRC2
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "2"

Apk:org.kontalk_500.apk
Err: Found: "2"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "2"

Apk:eu.faircode.email_1818.apk
Err: Found: "2"

Apk:org.walleth_514.apk
Err: Found: "2"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "2"

Apk:org.pacien.tincapp_33.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "2"

Apk:app.crescentcash.src_120.apk
Err: Found: "2"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "2"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "2"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "2"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "2"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "2"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "2"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "2"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "2"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "2"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "2"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "2"

Apk:com.eventyay.attendee_17.apk
Err: Found: "2"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "2"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "2"

Apk:de.rki.covpass.app_711.apk
Err: Found: "2"

Apk:rs.ltt.android_11.apk
Err: Found: "2"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "2"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "2"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "2"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "2"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "2"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "2"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "2"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "2"

Apk:com.limelight_271.apk
Err: Found: "2"

Apk:net.osmand.plus_421.apk
Err: Found: "2"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "2"

Apk:org.primftpd_55.apk
Err: Found: "2"

Apk:com.dimension.tessercube_200.apk
Err: Found: "2"

Apk:com.btcontract.wallet_95.apk
Err: Found: "2"

Apk:org.fdroid.nearby_2.apk
Err: Found: "2"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "2"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "2"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#8
Class: org.bouncycastle.jcajce.provider.symmetric.RC2$PBEWithSHA1AndRC2
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "0"

Apk:org.kontalk_500.apk
Err: Found: "0"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "0"

Apk:eu.faircode.email_1818.apk
Err: Found: "0"

Apk:org.walleth_514.apk
Err: Found: "0"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "0"

Apk:org.pacien.tincapp_33.apk
Err: Found: "0"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "0"

Apk:app.crescentcash.src_120.apk
Err: Found: "0"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "0"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "0"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "0"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "0"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "0"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "0"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "0"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "0"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "0"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "0"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "0"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "0"

Apk:com.eventyay.attendee_17.apk
Err: Found: "0"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "0"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "0"

Apk:de.rki.covpass.app_711.apk
Err: Found: "0"

Apk:rs.ltt.android_11.apk
Err: Found: "0"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "0"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "0"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "0"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "0"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "0"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "0"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "0"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "0"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "0"

Apk:com.limelight_271.apk
Err: Found: "0"

Apk:net.osmand.plus_421.apk
Err: Found: "0"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "0"

Apk:org.primftpd_55.apk
Err: Found: "0"

Apk:com.dimension.tessercube_200.apk
Err: Found: "0"

Apk:com.btcontract.wallet_95.apk
Err: Found: "0"

Apk:org.fdroid.nearby_2.apk
Err: Found: "0"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "0"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "0"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#9
Class: org.bouncycastle.jcajce.provider.symmetric.RC2$PBEWithMD5AndRC2
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "0"

Apk:org.kontalk_500.apk
Err: Found: "0"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "0"

Apk:eu.faircode.email_1818.apk
Err: Found: "0"

Apk:org.walleth_514.apk
Err: Found: "0"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "0"

Apk:org.pacien.tincapp_33.apk
Err: Found: "0"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "0"

Apk:app.crescentcash.src_120.apk
Err: Found: "0"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "0"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "0"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "0"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "0"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "0"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "0"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "0"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "0"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "0"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "0"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "0"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "0"

Apk:com.eventyay.attendee_17.apk
Err: Found: "0"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "0"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "0"

Apk:de.rki.covpass.app_711.apk
Err: Found: "0"

Apk:rs.ltt.android_11.apk
Err: Found: "0"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "0"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "0"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "0"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "0"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "0"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "0"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "0"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "0"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "0"

Apk:com.limelight_271.apk
Err: Found: "0"

Apk:net.osmand.plus_421.apk
Err: Found: "0"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "0"

Apk:org.primftpd_55.apk
Err: Found: "0"

Apk:com.dimension.tessercube_200.apk
Err: Found: "0"

Apk:com.btcontract.wallet_95.apk
Err: Found: "0"

Apk:org.fdroid.nearby_2.apk
Err: Found: "0"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "0"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "0"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#10
Class: org.bouncycastle.jcajce.provider.symmetric.DESede$PBEWithSHAAndDES3Key
Method: void <init>()
Apk Num:44

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "2"

Apk:org.kontalk_500.apk
Err: Found: "2"

Apk:com.gianlu.aria2app_221.apk
Err: Found: "2"

Apk:eu.faircode.email_1818.apk
Err: Found: "2"

Apk:org.walleth_514.apk
Err: Found: "2"

Apk:hashengineering.darkcoin.wallet_70311.apk
Err: Found: "2"

Apk:org.pacien.tincapp_33.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.verifier_3030000.apk
Err: Found: "2"

Apk:app.crescentcash.src_120.apk
Err: Found: "2"

Apk:com.wa2c.android.cifsdocumentsprovider_8.apk
Err: Found: "2"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: "2"

Apk:net.tjado.passwdsafe_400.apk
Err: Found: "2"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "2"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "2"

Apk:org.sufficientlysecure.termbot_10905217.apk
Err: Found: "2"

Apk:org.sufficientlysecure.keychain_57500.apk
Err: Found: "2"

Apk:ch.admin.bag.covidcertificate.wallet_3030000.apk
Err: Found: "2"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "2"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "2"

Apk:de.rki.covpass.checkapp_711.apk
Err: Found: "2"

Apk:me.zhanghai.android.files_25.apk
Err: Found: "2"

Apk:com.eventyay.attendee_17.apk
Err: Found: "2"

Apk:io.github.muntashirakon.AppManager_397.apk
Err: Found: "2"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "2"

Apk:de.rki.covpass.app_711.apk
Err: Found: "2"

Apk:rs.ltt.android_11.apk
Err: Found: "2"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "2"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "2"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "2"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "2"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "2"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "2"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "2"

Apk:org.projectmaxs.transport.xmpp_2000503969.apk
Err: Found: "2"

Apk:com.ctemplar.app.fdroid_31.apk
Err: Found: "2"

Apk:com.limelight_271.apk
Err: Found: "2"

Apk:net.osmand.plus_421.apk
Err: Found: "2"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "2"

Apk:org.primftpd_55.apk
Err: Found: "2"

Apk:com.dimension.tessercube_200.apk
Err: Found: "2"

Apk:com.btcontract.wallet_95.apk
Err: Found: "2"

Apk:org.fdroid.nearby_2.apk
Err: Found: "2"

Apk:com.kunzisoft.keepass.libre_92.apk
Err: Found: "2"

Apk:im.status.ethereum_2022011816.apk
Err: Found: "2"

Misuse Num:44
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#42
Class: org.bouncycastle.openssl.jcajce.PEMUtilities
Method: javax.crypto.SecretKey getKey(org.bouncycastle.jcajce.util.JcaJceHelper,char[],java.lang.String,int,byte[],boolean)
Apk Num:18

Apk:nl.rijksoverheid.ctr.holder_2137.apk
Err: Found: "1"

Apk:eu.faircode.email_1818.apk
Err: Found: "1"

Apk:org.pacien.tincapp_33.apk
Err: Found: "1"

Apk:ie.defo.ech_apps_1014003.apk
Err: Found: "1"

Apk:com.todobom.opennotescanner_35.apk
Err: Found: "1"

Apk:dev.msfjarvis.aps_11350.apk
Err: Found: "1"

Apk:me.bgregos.brighttask_16.apk
Err: Found: "1"

Apk:com.nighthawkapps.wallet.android_10032800.apk
Err: Found: "1"

Apk:com.ubergeek42.WeechatAndroid_10701.apk
Err: Found: "1"

Apk:org.fdroid.fdroid_1013051.apk
Err: Found: "1"

Apk:com.tananaev.passportreader_16.apk
Err: Found: "1"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "1"

Apk:io.horizontalsystems.bankwallet_58.apk
Err: Found: "1"

Apk:nl.rijksoverheid.ctr.verifier_2161.apk
Err: Found: "1"

Apk:net.osmand.plus_421.apk
Err: Found: "1"

Apk:de.eidottermihi.raspicheck_57.apk
Err: Found: "1"

Apk:org.primftpd_55.apk
Err: Found: "1"

Apk:org.fdroid.nearby_2.apk
Err: Found: "1"

Misuse Num:18
```

ITP: Using `iteration = 1` is needed to support OpenSSL's non-standard encrypted key format (instead of PKCS#8). See [this OpenSSL man page](https://www.openssl.org/docs/manmaster/man3/PEM_read_PrivateKey.html#PEM-ENCRYPTION-FORMAT) and the [discussion here](https://stackoverflow.com/questions/58920371/what-is-the-encrypted-rsa-pem-format-from-openssl-genrsa) for details. The `PEMUtilities` in bouncycastle is a helper class for reading/generating this OpenSSL non-standard format.

------------------------------------------------
```
#43
Class: org.spongycastle.openssl.jcajce.PEMUtilities
Method: javax.crypto.SecretKey getKey(org.spongycastle.jcajce.util.JcaJceHelper,char[],java.lang.String,int,byte[],boolean)
Apk Num:13

Apk:fr.gouv.etalab.mastodon_383.apk
Err: Found: "1"

Apk:com.zorinos.zorin_connect_11700.apk
Err: Found: "1"

Apk:com.standardnotes_3000323.apk
Err: Found: "1"

Apk:com.genonbeta.TrebleShot_104.apk
Err: Found: "1"

Apk:network.ubic.ubic_7.apk
Err: Found: "1"

Apk:kiwi.root.an2linuxclient_19.apk
Err: Found: "1"

Apk:org.flyve.mdm.agent.mqtt_3238.apk
Err: Found: "1"

Apk:app.fedilab.lite_383.apk
Err: Found: "1"

Apk:com.github.axet.bookreader_408.apk
Err: Found: "1"

Apk:org.kde.kdeconnect_tp_11900.apk
Err: Found: "1"

Apk:com.mschlauch.comfortreader_13.apk
Err: Found: "1"

Apk:eu.pretix.pretixprint_37.apk
Err: Found: "1"

Apk:com.stripe1.xmouse_25.apk
Err: Found: "1"

Misuse Num:13
```

ITP: Using `iteration = 1` is needed to support OpenSSL's non-standard encrypted key format (instead of PKCS#8). See [this OpenSSL man page](https://www.openssl.org/docs/manmaster/man3/PEM_read_PrivateKey.html#PEM-ENCRYPTION-FORMAT) and the [discussion here](https://stackoverflow.com/questions/58920371/what-is-the-encrypted-rsa-pem-format-from-openssl-genrsa) for details. The `PEMUtilities` in bouncycastle is a helper class for reading/generating this OpenSSL non-standard format.
