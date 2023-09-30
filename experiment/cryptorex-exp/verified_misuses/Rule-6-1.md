# Summary

| Pattern | # of Raw Misuses | # of Reported Misuses | # of Grouped Misuses |
| ------- | ---------------- | --------------------- | -------------------- |
| ITP-1   | 0                | 0                     | 0                    |
| ITP-2   | 0                | 0                     | 0                    |
| ITP-3   | 2                | 1                     | 1                    |
| TP      | 0                | 0                     | 0                    |
| FP      | 113              | 103                   | 4                    |
| Total   | 115              | 104                   | 5                    |

# Misuse-1 (ITP-3)

Pattern: ITP-3

Sum: 2

Desc: 

adjust: delay random rollback time when rollback by interval, to avoid all server focus on rollback default 60 (60s)

```cpp
    //use same seed for same log file, when reload may have same adjust time
    hash = ngx_crc32_short((u_char*)rbcf->logname, ngx_strlen(rbcf->logname));
    srand(hash);
    rbcf->adjust_time = rand() % rbcf->adjust_time_raw;
```

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/RBR20-V2.7.4.24.zip/RBR20-V2.7.4.24/_RBR20-V2.7.4.24.img.extracted/squashfs-root/data/funjsq/bin/funjsq_dl
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: srand (0x4a8ac)
Data: 0
Path: ['0x4a8a8']
Count: 2
Call stack:
--------------------------------------
```

# Misuse-2 (FP)

Pattern: FP

Sum: 19

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Implementation Bugs
Function name: srand (0x5e54c)
Data: 4096
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x5e510']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Implementation Bugs
Function name: srand (0x4c0a8)
Data: 180
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x4c054']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Implementation Bugs
Function name: srand (0x607f8)
Data: 600
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x607f8']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x41944)
Data: 180
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x41944']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4192c)
Data: 5
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x4192c']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x418c0)
Data: 180
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x418c0']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x418a8)
Data: 5
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x418a8']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x406e4)
Data: 264180
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x406d0']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x39678)
Data: 20
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x39678']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x39694)
Data: 20
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x39680']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x64284)
Data: 2147483647
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x64278']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x63c94)
Data: 2147483647
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x63c3c']
Count: 2
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x41b38)
Data: 269176
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x41b2c']
Count: 2
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4421c)
Data: 279120
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x44214']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x441f8)
Data: 279116
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x441f0']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4ded4)
Data: 60
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x4dec4']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
-> sub_4dec4 (0x4dec4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/newp2p
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x66b9c)
Data: 1024
Path: ['0x5a800', '0x5a7fc', '0x5a7d4', '0x66b9c']
Count: 1
Call stack:
-> sub_5a7d4 (0x5a7d4)
--------------------------------------
```

# Misuse-3 (FP)

Pattern: FP

Sum: 74

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x544d0)
Data: 600
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x544d0']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3dee8)
Data: 180
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x3de94']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x32b1c)
Data: 180
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x32b1c']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x32b04)
Data: 5
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x32b04']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x32a98)
Data: 180
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x32a98']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x32a80)
Data: 5
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x32a80']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x318bc)
Data: 203212
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x318a8']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a850)
Data: 20
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x2a850']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a86c)
Data: 20
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x2a858']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x57f5c)
Data: 2147483647
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x57f50']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x5796c)
Data: 2147483647
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x57914']
Count: 2
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x52224)
Data: 4096
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x521e8']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x32d10)
Data: 208208
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x32d04']
Count: 2
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x353f4)
Data: 218152
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x353ec']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x353d0)
Data: 218148
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x353c8']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3fd14)
Data: 60
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x3fd04']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
-> sub_3fd04 (0x3fd04)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x5a874)
Data: 1024
Path: ['0x4c640', '0x4c63c', '0x4c614', '0x5a874']
Count: 1
Call stack:
-> sub_4c614 (0x4c614)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x31bd8)
Data: 600
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x31bd8']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x242c0)
Data: 180
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x242ac']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x184a0)
Data: 99696
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x18494']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x41d0c)
Data: 512
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x2b478', '0x2b470', '0x2b464', '0x2b430', '0x41d0c']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
-> sub_2b430 (0x2b430)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x25b58)
Data: 2147483647
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x2b478', '0x2b470', '0x2b464', '0x2b430', '0x25b48']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
-> sub_2b430 (0x2b430)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x408c8)
Data: 512
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x2b478', '0x2b470', '0x2b464', '0x2b430', '0x408c8']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
-> sub_2b430 (0x2b430)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x19374)
Data: 180
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x19374']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x1932c)
Data: 180
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x1932c']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x31794)
Data: 4096
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x3178c']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x151f4)
Data: 20
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x151f4']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x15204)
Data: 20
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x151fc']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x34ed0)
Data: 2147483647
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x34ecc']
Count: 2
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x349a0)
Data: 2147483647
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x3499c']
Count: 2
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x19458)
Data: 103572
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x19450']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x1a8b4)
Data: 108756
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x1a8b4']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x1a89c)
Data: 50000
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x1a89c']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2443c)
Data: 60
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x2443c']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x346fc)
Data: 1024
Path: ['0x2b40c', '0x2b408', '0x2b3f0', '0x346fc']
Count: 1
Call stack:
-> sub_2b3f0 (0x2b3f0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x48588)
Data: 600
Path: ['0x40708', '0x40704', '0x406e4', '0x48588']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x368f4)
Data: 180
Path: ['0x40708', '0x40704', '0x406e4', '0x368e0']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x28b18)
Data: 1000000
Path: ['0x40708', '0x40704', '0x406e4', '0x28b0c']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x60584)
Data: 512
Path: ['0x40708', '0x40704', '0x406e4', '0x40768', '0x40748', '0x40730', '0x60584']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
-> tr_rand_int (0x40730)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x39158)
Data: 2147483647
Path: ['0x40708', '0x40704', '0x406e4', '0x40768', '0x40748', '0x40730', '0x39140']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
-> tr_rand_int (0x40730)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x5e780)
Data: 512
Path: ['0x40708', '0x40704', '0x406e4', '0x40768', '0x40748', '0x40730', '0x5e780']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
-> tr_rand_int (0x40730)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a1c4)
Data: 180
Path: ['0x40708', '0x40704', '0x406e4', '0x2a1c4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a1b0)
Data: 180
Path: ['0x40708', '0x40704', '0x406e4', '0x2a1b0']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a14c)
Data: 5
Path: ['0x40708', '0x40704', '0x406e4', '0x2a14c']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a18c)
Data: 5
Path: ['0x40708', '0x40704', '0x406e4', '0x2a18c']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4a220)
Data: 4096
Path: ['0x40708', '0x40704', '0x406e4', '0x4a210']
Count: 2
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x24e38)
Data: 20
Path: ['0x40708', '0x40704', '0x406e4', '0x24e38']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x24e44)
Data: 20
Path: ['0x40708', '0x40704', '0x406e4', '0x24e40']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4d3fc)
Data: 2147483647
Path: ['0x40708', '0x40704', '0x406e4', '0x4d3f8']
Count: 2
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4dbac)
Data: 2147483647
Path: ['0x40708', '0x40704', '0x406e4', '0x4dba4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x292f4)
Data: 15000
Path: ['0x40708', '0x40704', '0x406e4', '0x292f4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x29294)
Data: 15000
Path: ['0x40708', '0x40704', '0x406e4', '0x29294']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x29684)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x29684']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x29728)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x29728']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x29794)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x29794']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x297e8)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x297e8']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2983c)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x2983c']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x29890)
Data: 40000
Path: ['0x40708', '0x40704', '0x406e4', '0x29890']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x295c0)
Data: 2000
Path: ['0x40708', '0x40704', '0x406e4', '0x295c0']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2961c)
Data: 15000
Path: ['0x40708', '0x40704', '0x406e4', '0x2961c']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2a240)
Data: 1000000
Path: ['0x40708', '0x40704', '0x406e4', '0x2a238']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2c9b4)
Data: 50000
Path: ['0x40708', '0x40704', '0x406e4', '0x2c9b4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2c998)
Data: 1000000
Path: ['0x40708', '0x40704', '0x406e4', '0x2c994']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2c8d8)
Data: 50000
Path: ['0x40708', '0x40704', '0x406e4', '0x2c8d8']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x2c8b8)
Data: 1000000
Path: ['0x40708', '0x40704', '0x406e4', '0x2c8b4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x375ec)
Data: 60
Path: ['0x40708', '0x40704', '0x406e4', '0x375ec']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x386e4)
Data: 60
Path: ['0x40708', '0x40704', '0x406e4', '0x386e4']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/usr/bin/transmission-daemon
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4ce24)
Data: 1024
Path: ['0x40708', '0x40704', '0x406e4', '0x4ce24']
Count: 1
Call stack:
-> tr_rand_int_weak (0x406e4)
--------------------------------------
```

# Misuse-4 (FP)

Pattern: FP

Sum: 19

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x5ee54)
Data: 4096
Path: ['0x59270', '0x5926c', '0x59244', '0x5ee18']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4ab18)
Data: 180
Path: ['0x59270', '0x5926c', '0x59244', '0x4aac4']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x61100)
Data: 600
Path: ['0x59270', '0x5926c', '0x59244', '0x61100']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3f748)
Data: 180
Path: ['0x59270', '0x5926c', '0x59244', '0x3f748']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3f730)
Data: 5
Path: ['0x59270', '0x5926c', '0x59244', '0x3f730']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3f6c4)
Data: 180
Path: ['0x59270', '0x5926c', '0x59244', '0x3f6c4']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3f6ac)
Data: 5
Path: ['0x59270', '0x5926c', '0x59244', '0x3f6ac']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3e4e8)
Data: 255480
Path: ['0x59270', '0x5926c', '0x59244', '0x3e4d4']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3747c)
Data: 20
Path: ['0x59270', '0x5926c', '0x59244', '0x3747c']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x37498)
Data: 20
Path: ['0x59270', '0x5926c', '0x59244', '0x37484']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x64b8c)
Data: 2147483647
Path: ['0x59270', '0x5926c', '0x59244', '0x64b80']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x6459c)
Data: 2147483647
Path: ['0x59270', '0x5926c', '0x59244', '0x64544']
Count: 2
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x3f93c)
Data: 260476
Path: ['0x59270', '0x5926c', '0x59244', '0x3f930']
Count: 2
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x42020)
Data: 270420
Path: ['0x59270', '0x5926c', '0x59244', '0x42018']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x41ffc)
Data: 270416
Path: ['0x59270', '0x5926c', '0x59244', '0x41ff4']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x4c944)
Data: 60
Path: ['0x59270', '0x5926c', '0x59244', '0x4c934']
Count: 1
Call stack:
-> sub_59244 (0x59244)
-> sub_4c934 (0x4c934)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DNS-345_A2_FIRMWARE_1.03B06.ZIP/DNS-345_A2_FIRMWARE_1.03B06/_DNS-345_A2_FW_v1.03b06.extracted/squashfs-root/usrsbin/transmission-remote
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsImplementation Bugs-S
Pattern: Implementation Bugs
Function name: srand (0x674a4)
Data: 1024
Path: ['0x59270', '0x5926c', '0x59244', '0x674a4']
Count: 1
Call stack:
-> sub_59244 (0x59244)
--------------------------------------
```

# Misuse-5 (FP)

Pattern: FP

Sum: 1

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DGN1000v3-V1.0.0.22_0.0.22.zip/DGN1000v3-V1.0.0.22_0.0.22/_DGN1000v3-V1.0.0.22_0.0.22.img.extracted/squashfs-root/usr/sbin/uhttpd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsCrypto Irrelevant-S
Pattern: Implementation Bugs
Function name: srand (0x409928)
Data: 537464850
Path: ['0x4098fc']
Count: 1
Call stack:
-> sub_4098fc (0x4098fc)
--------------------------------------
```

nsCrypto Irrelevant-S
Pattern: Implementation Bugs
Function name: srand (0x409928)
Data: 537464850
Path: ['0x4098fc']
Count: 1
Call stack:
-> sub_4098fc (0x4098fc)
--------------------------------------
```

