#### javax.crypto.spec.IvParameterSpec

```
----------------------------------------------------------------------
#1
Class: com.google.android.exoplayer2.upstream.crypto.AesFlushingCipher
Method: void <init>(int,byte[],long,long)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 35
org.bottiger.podcast_424.apk                                => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.infomaniak.drive_40004201.apk                           => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
io.homeassistant.companion.android.minimal_1818.apk         => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
app.fedilab.tubelab_33.apk                                  => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
agersant.polaris_415293114.apk                              => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r2)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.github.axet.callrecorder_220.apk                        => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
me.jfenn.alarmio_21.apk                                     => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
net.programmierecke.radiodroid2_94.apk                      => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
de.fragdenstaat.app_42.apk                                  => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.github.axet.audiorecorder_355.apk                       => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
me.ccrama.redditslide_337.apk                               => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.brouken.player_88.apk                                   => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
su.sadrobot.yashlang_16.apk                                 => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
ml.docilealligator.infinityforreddit_91.apk                 => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.holoplay_39.apk                                         => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.github.axet.torrentclient_711.apk                       => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.cause.commune_3.apk                                     => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
org.schabi.newpipelegacy_120.apk                            => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
org.schabi.newpipe_981.apk                                  => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
dev.leonlatsch.photok_18.apk                                => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r2)
org.mariotaku.twidere_517.apk                               => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.ensoft.imgurviewer_22200.apk                            => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.nextcloud.talk2_130000090.apk                           => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
org.saiditnet.redreader_87.apk                              => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r2)
com.podverse.fdroid_20.apk                                  => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
app.fedilab.fedilabtube_33.apk                              => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
org.stingle.photos_51.apk                                   => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r2)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.listen1.app_1.apk                                       => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
net.schueller.peertube_1077.apk                             => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.b44t.messenger_621.apk                                  => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
com.owncloud.android_21900000.apk                           => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
me.thanel.dank_24.apk                                       => at statement: specialinvoke $r7.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r2)
se.oandell.riksdagen_39.apk                                 => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r1)
```

For RequiredPredicateError, ITP: The rule require the first parameter of `IvParameterSpec(iv);` should be results that called from `SecureRandom()`. However, for this case, it have to get IV from external source (load it from a DataSpec object).


```
----------------------------------------------------------------------
#2
Class: com.google.android.exoplayer2.source.hls.Aes128DataSource
Method: long open(com.google.android.exoplayer2.upstream.DataSpec)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 35
org.bottiger.podcast_424.apk                                => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.infomaniak.drive_40004201.apk                           => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
io.homeassistant.companion.android.minimal_1818.apk         => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
app.fedilab.tubelab_33.apk                                  => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.github.axet.callrecorder_220.apk                        => at statement: specialinvoke r2.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r6)
me.jfenn.alarmio_21.apk                                     => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
net.programmierecke.radiodroid2_94.apk                      => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
de.fragdenstaat.app_42.apk                                  => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.github.axet.audiorecorder_355.apk                       => at statement: specialinvoke r2.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r6)
com.brouken.player_88.apk                                   => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
su.sadrobot.yashlang_16.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
ml.docilealligator.infinityforreddit_91.apk                 => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.holoplay_39.apk                                         => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.workingagenda.democracydroid_54.apk                     => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.dkanada.gramophone_15.apk                               => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.github.axet.torrentclient_711.apk                       => at statement: specialinvoke r2.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r6)
org.schabi.newpipelegacy_120.apk                            => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.schabi.newpipe_981.apk                                  => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.mariotaku.twidere_517.apk                               => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.ensoft.imgurviewer_22200.apk                            => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.nextcloud.talk2_130000090.apk                           => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
nekox.messenger_545.apk                                     => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.seafile.seadroid2_117.apk                               => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
app.fedilab.fedilabtube_33.apk                              => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.perflyst.twire_525.apk                                  => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.telegram.messenger_25269.apk                            => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.listen1.app_1.apk                                       => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
net.schueller.peertube_1077.apk                             => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
io.gitlab.mudassir.youtubecacher_1.apk                      => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.owncloud.android_21900000.apk                           => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
me.thanel.dank_24.apk                                       => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
se.oandell.riksdagen_39.apk                                 => at statement: specialinvoke $r5.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
```

For RequiredPredicateError, ITP: The rule require the first parameter of `IvParameterSpec(iv);` should be results that called from `SecureRandom()`. However, for this case, exoplayer is decrypting some AES encrypted data and does need to get the IV from a external data instead of only getting from `SecureRandom()`.


```
----------------------------------------------------------------------
#3
Class: com.google.android.exoplayer2.upstream.cache.CachedContentIndex$LegacyStorage
Method: void writeFile(java.util.HashMap)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 23
com.infomaniak.drive_40004201.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
io.homeassistant.companion.android.minimal_1818.apk         => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
app.fedilab.tubelab_33.apk                                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.jfenn.alarmio_21.apk                                     => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.programmierecke.radiodroid2_94.apk                      => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.ccrama.redditslide_337.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.brouken.player_88.apk                                   => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
su.sadrobot.yashlang_16.apk                                 => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ml.docilealligator.infinityforreddit_91.apk                 => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.holoplay_39.apk                                         => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.dkanada.gramophone_15.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.schabi.newpipelegacy_120.apk                            => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.schabi.newpipe_981.apk                                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
dev.leonlatsch.photok_18.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mariotaku.twidere_517.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.nextcloud.talk2_130000090.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.podverse.fdroid_20.apk                                  => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
app.fedilab.fedilabtube_33.apk                              => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.schueller.peertube_1077.apk                             => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.owncloud.android_21900000.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
se.oandell.riksdagen_39.apk                                 => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
```

FP: IV is indeed obtained by SecureRandom. However, try-catch nest make Crysl miss follow-up call sequences. Pls refer to `testIV-TryCatch` case.


```
----------------------------------------------------------------------
#4
Class: com.google.android.exoplayer2.upstream.cache.CachedContentIndex$LegacyStorage
Method: boolean readFile(java.util.HashMap,android.util.SparseArray)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 23
com.infomaniak.drive_40004201.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
io.homeassistant.companion.android.minimal_1818.apk         => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
app.fedilab.tubelab_33.apk                                  => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
me.jfenn.alarmio_21.apk                                     => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
net.programmierecke.radiodroid2_94.apk                      => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
me.ccrama.redditslide_337.apk                               => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.brouken.player_88.apk                                   => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
su.sadrobot.yashlang_16.apk                                 => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
ml.docilealligator.infinityforreddit_91.apk                 => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.holoplay_39.apk                                         => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.dkanada.gramophone_15.apk                               => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
org.schabi.newpipelegacy_120.apk                            => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
org.schabi.newpipe_981.apk                                  => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
dev.leonlatsch.photok_18.apk                                => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
org.mariotaku.twidere_517.apk                               => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.nextcloud.talk2_130000090.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.podverse.fdroid_20.apk                                  => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
app.fedilab.fedilabtube_33.apk                              => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
net.schueller.peertube_1077.apk                             => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
com.owncloud.android_21900000.apk                           => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
se.oandell.riksdagen_39.apk                                 => at statement: specialinvoke $r16.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r15)
```

ITP: The rule require the first parameter of `IvParameterSpec(iv);` should be results that called from `SecureRandom()`. However, for this case, exoplayer is decrypting some AES encrypted data and does need to get the IV from a external data instead of only getting from `SecureRandom()`.


```
----------------------------------------------------------------------
#5
Class: com.google.crypto.tink.subtle.AesGcmJce
Method: java.security.spec.AlgorithmParameterSpec getParams(byte[],int,int)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 19
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r6.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r6.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
com.github.igrmk.smsq_16.apk                                => at statement: specialinvoke $r3.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r1, $i1, $i0)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r3.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r1, $i1, $i0)
security.pEp_470.apk                                        => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r1.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r6.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r0, $i0, $i1)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r3.<javax.crypto.spec.IvParameterSpec: void <init>(byte[],int,int)>($r1, $i1, $i0)
```

FP: For encryption context, the Random class is a warpper of SecureRandom through ThreadLocal class. However, Crysl hv problem to construct the correct call graph when using ThreadLocal class to initilize the Random class, which results in this FP case. pls refer to `testIV-ThreadLocal` case.

```
----------------------------------------------------------------------
#6
Class: com.google.crypto.tink.subtle.AesEaxJce
Method: byte[] encrypt(byte[],byte[])

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 19
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
com.github.igrmk.smsq_16.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
security.pEp_470.apk                                        => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r4)
```

FP: For encryption context, the Random class is a warpper of SecureRandom through ThreadLocal class. However, Crysl hv problem to construct the correct call graph when using ThreadLocal class to initilize the Random class, which results in this FP case. pls refer to `testIV-ThreadLocal` case.

```
----------------------------------------------------------------------
#7
Class: com.google.crypto.tink.subtle.AesCtrJceCipher
Method: void doCtr(byte[],int,int,byte[],int,byte[],boolean)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 19
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.github.igrmk.smsq_16.apk                                => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
security.pEp_470.apk                                        => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r8.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
```

FP: IV byte array is using `System.arraycopy(iv, 0, bArr, 0, this.ivSize);` to copy value from parameter byte array. The parameter array is either from Random class (a wrapper of SecureRandom through ThreadLocal) under encryption context or ciphertext under decryption context.

```
----------------------------------------------------------------------
#8
Class: com.google.crypto.tink.subtle.AesSiv
Method: byte[] encryptDeterministically(byte[],byte[])

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 18
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
security.pEp_470.apk                                        => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
```

ITP: SIV mode stands for synthetic initialization vector and works by deterministically deriving an IV from the input during encryption.


```
----------------------------------------------------------------------
#9
Class: com.google.crypto.tink.subtle.AesSiv
Method: byte[] decryptDeterministically(byte[],byte[])

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 18
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
security.pEp_470.apk                                        => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r10.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
```

ITP: For RequiredPredicateError, ITP: The rule require the first parameter of `IvParameterSpec(iv);` should be results that called from `SecureRandom()`. However, under decryption context, it have to get IV from external source.


```
----------------------------------------------------------------------
#10
Class: com.google.crypto.tink.subtle.AesEaxJce
Method: byte[] decrypt(byte[],byte[])

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 18
com.zell_mbc.medilog_5351.apk                               => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.duckduckgo.mobile.android_51080000.apk                  => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.twoeightnine.root.xvii_190.apk                          => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid_404.apk                                => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.protonvpn.android_102119017.apk                          => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
me.lucky.wasted_21.apk                                      => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.ivpn.client_100.apk                                     => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
host.stjin.anonaddy_29.apk                                  => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
at.bitfire.davdroid_401000005.apk                           => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
io.github.domi04151309.home_180.apk                         => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
com.yogeshpaliyal.keypass_1404.apk                          => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
ch.corona.tracing_20010.apk                                 => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
net.taler.cashier_1.apk                                     => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
security.pEp_470.apk                                        => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
eu.pretix.pretixscan.droid_56.apk                           => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.openhab.habdroid.beta_416.apk                           => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.teapod_4200.apk                                   => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
org.mosad.seil0.projectlaogai_6000.apk                      => at statement: specialinvoke $r9.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r7)
```

For RequiredPredicateError, ITP: The rule require the first parameter of `IvParameterSpec(iv);` should be results that called from `SecureRandom()`. However, under decryption context, it have to get IV from external source.