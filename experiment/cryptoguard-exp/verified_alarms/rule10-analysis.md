Rule: 10 Found constant IV in code

------------------------------------------------
```
#1
Class: com.google.android.exoplayer2.source.hls.HlsSampleStreamWrapper
Method: void initMediaChunkLoad(com.google.android.exoplayer2.source.hls.HlsMediaChunk)
Apk Num:12

Apk:com.owncloud.android_21900000.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.talk2_130000090.apk
Err: Found: "-9223372036854775807L"

Apk:com.brouken.player_88.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid.beta_416.apk
Err: Found: "-9223372036854775807L"

Apk:com.workingagenda.democracydroid_54.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid_404.apk
Err: Found: "-9223372036854775807L"

Apk:io.homeassistant.companion.android.minimal_1818.apk
Err: Found: "-9223372036854775807L"

Apk:com.infomaniak.drive_40004201.apk
Err: Found: "-9223372036854775807L"

Apk:com.perflyst.twire_525.apk
Err: Found: "-9223372036854775807L"

Apk:org.mariotaku.twidere_517.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "-9223372036854775807L"

Apk:org.schabi.newpipe_981.apk
Err: Found: "-9223372036854775807L"

Misuse Num:12
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#2
Class: com.google.android.exoplayer2.source.hls.HlsSampleStreamWrapper
Method: boolean continueLoading(long)
Apk Num:12

Apk:com.owncloud.android_21900000.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.talk2_130000090.apk
Err: Found: "-9223372036854775807L"

Apk:com.brouken.player_88.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid.beta_416.apk
Err: Found: "-9223372036854775807L"

Apk:com.workingagenda.democracydroid_54.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid_404.apk
Err: Found: "-9223372036854775807L"

Apk:io.homeassistant.companion.android.minimal_1818.apk
Err: Found: "-9223372036854775807L"

Apk:com.infomaniak.drive_40004201.apk
Err: Found: "-9223372036854775807L"

Apk:com.perflyst.twire_525.apk
Err: Found: "-9223372036854775807L"

Apk:org.mariotaku.twidere_517.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "-9223372036854775807L"

Apk:org.schabi.newpipe_981.apk
Err: Found: "-9223372036854775807L"

Misuse Num:12
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#3
Class: com.google.android.exoplayer2.source.hls.HlsChunkSource
Method: long resolveTimeToLiveEdgeUs(long)
Apk Num:12

Apk:com.owncloud.android_21900000.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.talk2_130000090.apk
Err: Found: "-9223372036854775807L"

Apk:com.brouken.player_88.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid.beta_416.apk
Err: Found: "-9223372036854775807L"

Apk:com.workingagenda.democracydroid_54.apk
Err: Found: "-9223372036854775807L"

Apk:org.openhab.habdroid_404.apk
Err: Found: "-9223372036854775807L"

Apk:io.homeassistant.companion.android.minimal_1818.apk
Err: Found: "-9223372036854775807L"

Apk:com.infomaniak.drive_40004201.apk
Err: Found: "-9223372036854775807L"

Apk:com.perflyst.twire_525.apk
Err: Found: "-9223372036854775807L"

Apk:org.mariotaku.twidere_517.apk
Err: Found: "-9223372036854775807L"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "-9223372036854775807L"

Apk:org.schabi.newpipe_981.apk
Err: Found: "-9223372036854775807L"

Misuse Num:12
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#4
Class: com.google.android.exoplayer2.source.hls.HlsChunkSource
Method: com.google.android.exoplayer2.source.hls.HlsChunkSource$SegmentBaseHolder getNextSegmentHolder(com.google.android.exoplayer2.source.hls.playlist.HlsMediaPlaylist,long,int)
Apk Num:12

Apk:com.owncloud.android_21900000.apk
Err: Found: "1L"

Apk:com.nextcloud.talk2_130000090.apk
Err: Found: "1L"

Apk:com.brouken.player_88.apk
Err: Found: "1L"

Apk:org.openhab.habdroid.beta_416.apk
Err: Found: "1L"

Apk:com.workingagenda.democracydroid_54.apk
Err: Found: "1L"

Apk:org.openhab.habdroid_404.apk
Err: Found: "1L"

Apk:io.homeassistant.companion.android.minimal_1818.apk
Err: Found: "1L"

Apk:com.infomaniak.drive_40004201.apk
Err: Found: "1L"

Apk:com.perflyst.twire_525.apk
Err: Found: "1L"

Apk:org.mariotaku.twidere_517.apk
Err: Found: "1L"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "1L"

Apk:org.schabi.newpipe_981.apk
Err: Found: "1L"

Misuse Num:12
```

FP: unrelated array operations.

------------------------------------------------
```
#5
Class: com.google.android.exoplayer2.C
Method: long usToMs(long)
Apk Num:8

Apk:com.owncloud.android_21900000.apk
Err: Found: "1000L"

Apk:com.workingagenda.democracydroid_54.apk
Err: Found: "1000L"

Apk:org.openhab.habdroid_404.apk
Err: Found: "1000L"

Apk:io.homeassistant.companion.android.minimal_1818.apk
Err: Found: "1000L"

Apk:com.perflyst.twire_525.apk
Err: Found: "1000L"

Apk:org.mariotaku.twidere_517.apk
Err: Found: "1000L"

Apk:com.nextcloud.client_30180190.apk
Err: Found: "1000L"

Apk:org.schabi.newpipe_981.apk
Err: Found: "1000L"

Misuse Num:8
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#6
Class: org.whispersystems.libsignal.ratchet.ChainKey
Method: void <clinit>()
Apk Num:7

Apk:com.dx.anonymousmessenger_46.apk
Err: Found: "1"

Apk:org.smssecure.smssecure_145.apk
Err: Found: "1"

Apk:com.cweb.messenger_42012.apk
Err: Found: "1"

Apk:im.quicksy.client_42023.apk
Err: Found: "1"

Apk:org.snikket.android_42024.apk
Err: Found: "1"

Apk:eu.siacs.conversations_42023.apk
Err: Found: "1"

Apk:org.tigase.messenger.phone.pro_90.apk
Err: Found: "1"

Misuse Num:7
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#7
Class: com.google.android.exoplayer2.util.Util
Method: long usToMs(long)
Apk Num:4

Apk:com.nextcloud.talk2_130000090.apk
Err: Found: "1000L"

Apk:com.brouken.player_88.apk
Err: Found: "1000L"

Apk:org.openhab.habdroid.beta_416.apk
Err: Found: "1000L"

Apk:com.infomaniak.drive_40004201.apk
Err: Found: "1000L"

Misuse Num:4
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#8
Class: com.github.javiersantos.licensing.AESObfuscator
Method: void <clinit>()
Apk Num:3

Apk:com.x1unix.s60icons_110.apk
Err: Found: "32"
Err: Found: "-80"
Err: Found: "101"
Err: Found: "74"
Err: Found: "-47"
Err: Found: "16"
Err: Found: "0"
Err: Found: "65"
Err: Found: "74"
Err: Found: "117"
Err: Found: "-29"
Err: Found: "72"
Err: Found: "71"
Err: Found: "-12"
Err: Found: "-14"
Err: Found: "70"

Apk:de.spiritcroc.defaultdarktheme_oms_53.apk
Err: Found: "32"
Err: Found: "-80"
Err: Found: "101"
Err: Found: "74"
Err: Found: "-47"
Err: Found: "16"
Err: Found: "0"
Err: Found: "65"
Err: Found: "74"
Err: Found: "117"
Err: Found: "-29"
Err: Found: "72"
Err: Found: "71"
Err: Found: "-12"
Err: Found: "-14"
Err: Found: "70"

Apk:de.spiritcroc.darkcroc.substratum_11.apk
Err: Found: "32"
Err: Found: "-80"
Err: Found: "101"
Err: Found: "74"
Err: Found: "-47"
Err: Found: "16"
Err: Found: "0"
Err: Found: "65"
Err: Found: "74"
Err: Found: "117"
Err: Found: "-29"
Err: Found: "72"
Err: Found: "71"
Err: Found: "-12"
Err: Found: "-14"
Err: Found: "70"

Misuse Num:48
```

TP

------------------------------------------------
```
#9
Class: org.matrix.android.sdk.internal.crypto.secrets.DefaultSharedSecretStorageService$storeSecret$2
Method: java.lang.Object invokeSuspend(java.lang.Object)
Apk Num:2

Apk:im.vector.app_40103150.apk
Err: Found: "0"

Apk:de.spiritcroc.riotx_40100720.apk
Err: Found: "0"

Misuse Num:2
```

FP: broken def-use chains due to intervening definitions.

------------------------------------------------
```
#10
Class: org.matrix.android.sdk.internal.crypto.secrets.DefaultSharedSecretStorageService$getSecret$3
Method: java.lang.Object invokeSuspend(java.lang.Object)
Apk Num:2

Apk:im.vector.app_40103150.apk
Err: Found: "0"

Apk:de.spiritcroc.riotx_40100720.apk
Err: Found: "0"

Misuse Num:2
```

FP: broken def-use chains due to intervening definitions.