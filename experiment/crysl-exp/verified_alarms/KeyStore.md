#### java.security.KeyStore

```
----------------------------------------------------------------------
#1
Class: androidx.biometric.CryptoObjectUtils
Method: androidx.biometric.BiometricPrompt$CryptoObject createFakeCryptoObject()

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 25
com.zell_mbc.medilog_5351.apk                               => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer13076)
io.simplelogin.android.fdroid_19.apk                        => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer8698)
com.soumikshah.investmenttracker_3.apk                      => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer1215)
com.infomaniak.drive_40004201.apk                           => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer24519)
io.homeassistant.companion.android.minimal_1818.apk         => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer130730)
com.greenaddress.greenbits_android_wallet_22000378.apk      => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer20133)
org.openhab.habdroid_404.apk                                => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer44306)
site.leos.apps.lespas_45.apk                                => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer63227)
ml.docilealligator.infinityforreddit_91.apk                 => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer27269)
host.stjin.anonaddy_29.apk                                  => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18882)
org.mian.gitnex_410.apk                                     => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer7199)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer11941)
com.simplemobiletools.voicerecorder_17.apk                  => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer33209)
ch.corona.tracing_20010.apk                                 => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer26700)
org.liberty.android.freeotpplus_18.apk                      => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer25155)
com.nextcloud.talk2_130000090.apk                           => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer127523)
eu.kanade.tachiyomi_69.apk                                  => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer13179)
xyz.hisname.fireflyiii_108.apk                              => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer32811)
de.tutao.tutanota_389250.apk                                => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer6389)
io.bluewallet.bluewallet_60205.apk                          => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22547)
com.gaurav.avnc_8.apk                                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer3698)
org.stingle.photos_51.apk                                   => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer11659)
org.openhab.habdroid.beta_416.apk                           => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer44239)
com.lesspass.android_90503.apk                              => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer27595)
com.simplemobiletools.smsmessenger_42.apk                   => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer43146)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#2
Class: androidx.biometric.h
Method: androidx.biometric.BiometricPrompt$c a()

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 20
com.simplemobiletools.calendar.pro_212.apk                  => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer29106)
com.simplemobiletools.dialer_32.apk                         => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer19374)
com.simplemobiletools.draw.pro_65.apk                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18810)
com.pitchedapps.frost_3010200.apk                           => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer56696)
com.simplemobiletools.filemanager.pro_114.apk               => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer19783)
com.termux.api_51.apk                                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer3815)
com.simplemobiletools.musicplayer_92.apk                    => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer32702)
com.abhinavmarwaha.lifehq_9.apk                             => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer12342)
design.codeux.authpass.fdroid_159.apk                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer27615)
com.simplemobiletools.flashlight_49.apk                     => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer17926)
com.invoiceninja.app_73.apk                                 => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer6921)
com.simplemobiletools.gallery.pro_358.apk                   => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer29784)
com.simplemobiletools.calculator_45.apk                     => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18140)
io.timelimit.android.open_177.apk                           => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer29497)
com.simplemobiletools.contacts.pro_89.apk                   => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer26044)
com.simplemobiletools.applauncher_38.apk                    => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer17358)
com.simplemobiletools.clock_25.apk                          => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer24133)
com.simplemobiletools.notes.pro_89.apk                      => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer16587)
de.jbservices.nc_passwords_app_21.apk                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22271)
com.simplemobiletools.thankyou_21.apk                       => at statement: $r0 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer15487)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#3
Class: com.google.crypto.tink.integration.android.AndroidKeystoreKmsClient$Builder
Method: void <init>()

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 17
com.zell_mbc.medilog_5351.apk                               => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22854)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer59639)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer43290)
org.openhab.habdroid_404.apk                                => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer52430)
ch.protonvpn.android_102119017.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer71145)
me.lucky.wasted_21.apk                                      => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer5670)
net.ivpn.client_100.apk                                     => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer36588)
host.stjin.anonaddy_29.apk                                  => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18079)
at.bitfire.davdroid_401000005.apk                           => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer42940)
io.github.domi04151309.home_180.apk                         => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer4762)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer60382)
ch.corona.tracing_20010.apk                                 => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22520)
security.pEp_470.apk                                        => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer41262)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer66324)
org.openhab.habdroid.beta_416.apk                           => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer52382)
org.mosad.teapod_4200.apk                                   => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer8760)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer11375)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#4
Class: com.google.crypto.tink.integration.android.AndroidKeystoreKmsClient
Method: boolean hasKey(java.lang.String)

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 16
com.zell_mbc.medilog_5351.apk                               => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22863)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer59646)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer43295)
org.openhab.habdroid_404.apk                                => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer52436)
ch.protonvpn.android_102119017.apk                          => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer71149)
me.lucky.wasted_21.apk                                      => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer5674)
net.ivpn.client_100.apk                                     => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer36596)
host.stjin.anonaddy_29.apk                                  => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18084)
at.bitfire.davdroid_401000005.apk                           => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer38924)
io.github.domi04151309.home_180.apk                         => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer4770)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer60387)
ch.corona.tracing_20010.apk                                 => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22508)
security.pEp_470.apk                                        => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer41269)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer66329)
org.openhab.habdroid.beta_416.apk                           => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer52386)
org.mosad.teapod_4200.apk                                   => at statement: $r4 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer8703)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#5
Class: ch.qos.logback.core.net.ssl.KeyStoreFactoryBean
Method: java.security.KeyStore createKeyStore()

Error Type: NeverTypeOfError
Error Reason: Second parameter should never be of type java.lang.String.
Apk Num: 15
com.lukekorth.screennotifications_22.apk                    => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r4, $r6)
ch.protonvpn.android_102119017.apk                          => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
net.ivpn.client_100.apk                                     => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
info.schnatterer.nusic_24.apk                               => at statement: virtualinvoke $r13.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r11, $r14)
ru.hyst329.openfool_30.apk                                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
com.better.alarm_31006.apk                                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
de.wellenvogel.bonjourbrowser_111.apk                       => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
org.totschnig.myexpenses_505.apk                            => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
fr.free.nrw.commons_1025.apk                                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
it.skarafaz.mercury_9.apk                                   => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
org.happypeng.sumatora.android.sumatoradictionary_31.apk    => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
dummydomain.yetanothercallblocker_5170.apk                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
app.tice.TICE.production_38.apk                             => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
nodomain.freeyourgadget.gadgetbridge_208.apk                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
com.serwylo.retrowars_27.apk                                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)

Error Type: HardCodedError
Error Reason: Second parameter should never be hardcoded.
Apk Num: 15
com.lukekorth.screennotifications_22.apk                    => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r4, $r6)
ch.protonvpn.android_102119017.apk                          => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
net.ivpn.client_100.apk                                     => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
info.schnatterer.nusic_24.apk                               => at statement: virtualinvoke $r13.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r11, $r14)
ru.hyst329.openfool_30.apk                                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
com.better.alarm_31006.apk                                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
de.wellenvogel.bonjourbrowser_111.apk                       => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
org.totschnig.myexpenses_505.apk                            => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
fr.free.nrw.commons_1025.apk                                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
it.skarafaz.mercury_9.apk                                   => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
org.happypeng.sumatora.android.sumatoradictionary_31.apk    => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
dummydomain.yetanothercallblocker_5170.apk                  => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
app.tice.TICE.production_38.apk                             => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
nodomain.freeyourgadget.gadgetbridge_208.apk                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
com.serwylo.retrowars_27.apk                                => at statement: virtualinvoke $r8.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r7, $r9)
```

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testKeystoreHardcoded.

For NeverTypeOfError, ITP: vain predicate.

```
----------------------------------------------------------------------
#6
Class: androidx.security.crypto.MasterKeys
Method: boolean keyExists(java.lang.String)

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 14
com.zell_mbc.medilog_5351.apk                               => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer19058)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer49971)
com.twoeightnine.root.xvii_190.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer22625)
org.openhab.habdroid_404.apk                                => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer28319)
ch.protonvpn.android_102119017.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer29283)
me.lucky.wasted_21.apk                                      => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer1233)
net.ivpn.client_100.apk                                     => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer29150)
host.stjin.anonaddy_29.apk                                  => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer18066)
io.github.domi04151309.home_180.apk                         => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer2866)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer59601)
security.pEp_470.apk                                        => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer32525)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer59901)
org.openhab.habdroid.beta_416.apk                           => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer27570)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r1 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer6576)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#7
Class: org.acra.http.BaseHttpRequest
Method: void configureHttps(javax.net.ssl.HttpsURLConnection)

Error Type: IncompleteOperationError
Error Reason: Operation on object of type java.security.KeyStore object not completed. Expected call to load
Apk Num: 11
org.courville.nova_404911.apk                               => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
fr.chenry.android.freshrss_20.apk                           => at statement: virtualinvoke $r4.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r7)
sh.ftp.rocketninelabs.meditationassistant.opensource_165.apk => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
org.midorinext.android_36.apk                               => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
pw.thedrhax.mosmetro_77.apk                                 => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
org.zephyrsoft.trackworktime_56.apk                         => at statement: virtualinvoke $r4.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r7)
io.github.chronosx88.yggdrasil_37.apk                       => at statement: virtualinvoke $r4.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r7)
eu.kanade.tachiyomi_69.apk                                  => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r13)
com.etesync.syncadapter_20204.apk                           => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
com.ichi2.anki_21506300.apk                                 => at statement: virtualinvoke $r3.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r6)
vocabletrainer.heinecke.aron.vocabletrainer_23.apk          => at statement: virtualinvoke $r4.<javax.net.ssl.TrustManagerFactory: void init(java.security.KeyStore)>($r7)
```

IncompleteOperationError, ITP: The KeyStore object is used to initialize TrustManagerFactory. `TrustManagerFactory.init(keystore)` Initializes this factory with a source of certificate authorities and related trust material.

```
----------------------------------------------------------------------
#8
Class: org.eclipse.paho.client.mqttv3.internal.security.SSLSocketFactoryFactory
Method: javax.net.ssl.SSLContext getSSLContext(java.lang.String)

Error Type: NeverTypeOfError
Error Reason: Second parameter should never be of type java.lang.String.
Apk Num: 9
com.infomaniak.drive_40004201.apk                           => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
io.mainframe.hacs_53.apk                                    => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
org.c_base.c_beam_29.apk                                    => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r9)
org.nexttracks.android_32100.apk                            => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
org.poul.bits.android_4.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
com.example.trigger_336.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
de.rwth_aachen.phyphox_1011002.apk                          => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
com.fr3ts0n.androbd.plugin.mqtt_10101.apk                   => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
net.sylvek.itracing2_82.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)

Error Type: HardCodedError
Error Reason: Second parameter should never be hardcoded.
Apk Num: 9
com.infomaniak.drive_40004201.apk                           => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
io.mainframe.hacs_53.apk                                    => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
org.c_base.c_beam_29.apk                                    => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r9)
org.nexttracks.android_32100.apk                            => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
org.poul.bits.android_4.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
com.example.trigger_336.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
de.rwth_aachen.phyphox_1011002.apk                          => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
com.fr3ts0n.androbd.plugin.mqtt_10101.apk                   => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
net.sylvek.itracing2_82.apk                                 => at statement: virtualinvoke $r14.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r15, $r10)
```

For HardCodedError, FP: This case is due to wrong implementation of extractSootArray and isHardCodedArray in constraint solver for hardcoded error. pls refer to MWE case: testKeystoreHardcoded.

For NeverTypeOfError, ITP: vain predicate.

```
----------------------------------------------------------------------
#9
Class: androidx.security.crypto.MasterKey
Method: boolean isKeyStoreBacked()

Error Type: ConstraintError
Error Reason: First parameter (with value "AndroidKeyStore") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 9
com.zell_mbc.medilog_5351.apk                               => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer5758)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer75791)
net.ivpn.client_100.apk                                     => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer15143)
host.stjin.anonaddy_29.apk                                  => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer13011)
io.github.domi04151309.home_180.apk                         => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer12434)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer13572)
security.pEp_470.apk                                        => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer16390)
eu.pretix.pretixscan.droid_56.apk                           => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer44696)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>(varReplacer13427)
```

For ConstraintError, ITP: miss `AndroidKeyStore` as a type of keystore in Android.

```
----------------------------------------------------------------------
#10
Class: org.bitcoinj.crypto.X509Utils
Method: java.security.KeyStore loadKeyStore(java.lang.String,java.lang.String,java.io.InputStream)

Error Type: NeverTypeOfError
Error Reason: Second parameter should never be of type java.lang.String.
Apk Num: 8
de.langerhans.wallet_400.apk                                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
de.schildbach.wallet_test_903_58dcd8a.apk                   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.groestlcoin.wallet_81401.apk                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
com.greenaddress.greenbits_android_wallet.testnet_205.apk   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
app.crescentcash.src_120.apk                                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
de.schildbach.wallet_903_58dcd8a.apk                        => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.groestlcoin.wallet_test_81401.apk           => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)

Error Type: HardCodedError
Error Reason: Second parameter should never be hardcoded.
Apk Num: 8
de.langerhans.wallet_400.apk                                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
de.schildbach.wallet_test_903_58dcd8a.apk                   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.groestlcoin.wallet_81401.apk                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
com.greenaddress.greenbits_android_wallet.testnet_205.apk   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
app.crescentcash.src_120.apk                                => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
de.schildbach.wallet_903_58dcd8a.apk                        => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)
hashengineering.groestlcoin.wallet_test_81401.apk           => at statement: virtualinvoke $r5.<java.security.KeyStore: void load(java.io.InputStream,char[])>($r0, $r6)

Error Type: ConstraintError
Error Reason: First parameter (with value "BKS") should be any of {JCEKS, JKS, DKS, PKCS11, PKCS12}
Apk Num: 8
de.langerhans.wallet_400.apk                                => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
de.schildbach.wallet_test_903_58dcd8a.apk                   => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
hashengineering.groestlcoin.wallet_81401.apk                => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
com.greenaddress.greenbits_android_wallet.testnet_205.apk   => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
app.crescentcash.src_120.apk                                => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
de.schildbach.wallet_903_58dcd8a.apk                        => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
hashengineering.darkcoin.wallet_70311.apk                   => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
hashengineering.groestlcoin.wallet_test_81401.apk           => at statement: $r5 = staticinvoke <java.security.KeyStore: java.security.KeyStore getInstance(java.lang.String)>($r3)
```

For HardCodedError, TP.

For NeverTypeOfError, ITP: vain predicate.

For ConstraintError, ITP: miss `BKS` as a type of keystore in Android.
