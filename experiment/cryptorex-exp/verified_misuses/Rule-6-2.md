# Summary

| Pattern | # of Raw Misuses | # of Reported Misuses | # of Grouped Misuses |
| ------- | ---------------- | --------------------- | -------------------- |
| ITP-1   | 0                | 0                     | 0                    |
| ITP-2   | 0                | 0                     | 0                    |
| ITP-3   | 270              | 13                    | 13                   |
| ITP-4   | 328              | 9                     | 9                    |
| TP      | 28               | 2                     | 2                    |
| FP      | 0                | 0                     | 0                    |
| Total   | 763              | 29                    | 29                   |

# Misuse-1 (ITP-3)

Pattern: ITP-3

Sum: 101

Desc: Generating random time interval

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WN2500RP-V1.0.0.30_1.0.58.zip/WN2500RP-V1.0.0.30_1.0.58/_WN2500RP-V1.0.0.30_1.0.58.chk.extracted/squashfs-root/usr/sbin/lld2d
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 101
Call stack:
--------------------------------------
```

# Misuse-2 (FP)

Pattern: FP

Sum: 64

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WN604_V3.3.10.zip/WN604_V3.3.10/_wn604_v3.3.10_firmware.tar.extracted/squashfs-root/usr/local/bin/hostapd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 64
Call stack:
--------------------------------------
```

# Misuse-3 (FP)

Pattern: FP

Sum: 64

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WN604_V3.3.10.zip/WN604_V3.3.10/_wn604_v3.3.10_firmware.tar.extracted/squashfs-root/usr/local/bin/hostapd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 64
Call stack:
--------------------------------------
```

# Misuse-4 (FP)

Pattern: FP

Sum: 64

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WN604_V3.3.10.zip/WN604_V3.3.10/_wn604_v3.3.10_firmware.tar.extracted/squashfs-root/usr/local/bin/hostapd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 64
Call stack:
--------------------------------------
```

# Misuse-5 (NS)

Pattern: UNKNOWN

Sum: 60

Desc: Not sure

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WGR614v9_V1.2.32_43.0.46NA.zip/WGR614v9_V1.2.32_43.0.46NA/_WGR614v9-V1.2.32_43.0.46NA.chk.extracted/squashfs-root/usr/sbin/nas
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 60
Call stack:
--------------------------------------
```

# Misuse-6 (ITP-3)

Pattern: ITP-3

Sum: 43

Desc: getpwnam_alloc

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX6200-V1.0.3.94_1.1.128.zip/EX6200-V1.0.3.94_1.1.128/_EX6200-V1.0.3.94_1.1.128.chk.extracted/squashfs-root/usr/local/samba/smbd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 43
Call stack:
--------------------------------------
```

# Misuse-7 (NS)

Pattern: UNKNOWN

Sum: 32

Desc: Not sure

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WGR614v9_V1.2.32_43.0.46NA.zip/WGR614v9_V1.2.32_43.0.46NA/_WGR614v9-V1.2.32_43.0.46NA.chk.extracted/squashfs-root/usr/sbin/upnpd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Authors' incomprehensive understanding of cryptographic APIs
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 32
Call stack:
--------------------------------------
```

# Misuse-8 (NS)

Pattern: UNKNOWN

Sum: 30

Desc: Not Sure

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/DGN1000v3-V1.0.0.22_0.0.22.zip/DGN1000v3-V1.0.0.22_0.0.22/_DGN1000v3-V1.0.0.22_0.0.22.img.extracted/squashfs-root/usr/sbin/radvdump
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: NS
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 30
Call stack:
--------------------------------------
```

# Misuse-9 (FP)

Pattern: FP

Sum: 29

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WND930_V2.1.5.zip/WND930_V2.1.5/_wnd930_V2.1.5_firmware.tar.extracted/squashfs-root/usr/local/bin/wpa_supplicant
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: TP
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 29
Call stack:
--------------------------------------
```

# Misuse-10 (FP)

Pattern: FP

Sum: 29

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WND930_V2.1.5.zip/WND930_V2.1.5/_wnd930_V2.1.5_firmware.tar.extracted/squashfs-root/usr/local/bin/wpa_supplicant
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: TP
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 29
Call stack:
--------------------------------------
```

# Misuse-11 (FP)

Pattern: FP

Sum: 29

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WND930_V2.1.5.zip/WND930_V2.1.5/_wnd930_V2.1.5_firmware.tar.extracted/squashfs-root/usr/local/bin/wpa_supplicant
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: TP
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 29
Call stack:
--------------------------------------
```

# Misuse-12 (FP)

Pattern: FP

Sum: 29

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WND930_V2.1.5.zip/WND930_V2.1.5/_wnd930_V2.1.5_firmware.tar.extracted/squashfs-root/usr/local/bin/wpa_supplicant
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: TP
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 29
Call stack:
--------------------------------------
```

# Misuse-13 (ITP-3)

Pattern: ITP-3

Sum: 27

Desc: getpwnam_alloc

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX6200-V1.0.3.94_1.1.128.zip/EX6200-V1.0.3.94_1.1.128/_EX6200-V1.0.3.94_1.1.128.chk.extracted/squashfs-root/usr/local/samba/nmbd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 27
Call stack:
--------------------------------------
```

# Misuse-14 (ITP-3)

Pattern: ITP-3

Sum: 24

Desc: getpwnam_alloc

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/WNR3500L_V1.2.2.48_35.0.55NA.zip/WNR3500L_V1.2.2.48_35.0.55NA/_WNR3500L-V1.2.2.48_35.0.55NA.chk.extracted/squashfs-root/usr/local/samba/smb_pass
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 24
Call stack:
--------------------------------------
```

# Misuse-15 (TP) // Seeded by parent

Pattern: TP

Sum: 18

Desc: http_auth_digest_generate_nonce 

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//D-Link/DAP-1562_FIRMWARE_1.00.ZIP/DAP-1562_FIRMWARE_1.00/dap1562_FW_100/_dap1562_FW_100.bin.extracted/squashfs-root/usr/local/lib/mod_auth.so
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 18
Call stack:
--------------------------------------
```

# Misuse-16 (ITP-3)

Pattern: ITP-3

Sum: 12

Desc: getpwnam_alloc

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Linksys/FW_E3000_1.0.06.002_US_20140409_code.bin/_FW_E3000_1.0.06.002_US_20140409_code.bin.extracted/squashfs-root/lib/libbigballofmud.so
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: NS
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 12
Call stack:
--------------------------------------
```

# Misuse-17 (FP)

Pattern: FP

Sum: 12

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/openl2tpd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Authors' incomprehensive understanding of cryptographic APIs
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 12
Call stack:
--------------------------------------
```

# Misuse-18 (ITP-3)

Pattern: ITP-3

Sum: 10

Desc: Generating random time interval

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX7700-V1.0.0.222.zip/EX7700-V1.0.0.222/_EX7700-V1.0.0.222.img.extracted/squashfs-root/usr/lib/libavahi-common.so.3.5.3
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-19 (ITP-3)

Pattern: ITP-3

Sum: 10

Desc: Generating random time interval

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX7700-V1.0.0.222.zip/EX7700-V1.0.0.222/_EX7700-V1.0.0.222.img.extracted/squashfs-root/usr/lib/libavahi-core.so.7.0.2
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-20 (ITP-3)

Pattern: ITP-3

Sum: 10

Desc: Generating random cookie

```
<option>
<p><opt>add-service-cookie=</opt> Takes a boolean value ("yes"
or "no"). If set to "yes" an implicit TXT entry will be added
to all locally registered services, containing a cookie value
which is chosen randomly on daemon startup. This can be used
to detect if two services on two different
interfaces/protocols are actually identical. Defaults to
"no".</p>
</option>
```

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX7700-V1.0.0.222.zip/EX7700-V1.0.0.222/_EX7700-V1.0.0.222.img.extracted/squashfs-root/usr/lib/libavahi-core.so.7.0.2
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-21 (TP)

Pattern: TP

Sum: 10

Desc: Generating random packet ID

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX7700-V1.0.0.222.zip/EX7700-V1.0.0.222/_EX7700-V1.0.0.222.img.extracted/squashfs-root/usr/lib/libavahi-core.so.7.0.2
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-22 (ITP-3)

Pattern: ITP-3

Sum: 10

Desc: getpwnam_alloc

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/lib/libsmbclient.so
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-23 (NS)

Pattern: UNKNOWN

Sum: 10

Desc: Not Sure

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/EX7700-V1.0.0.222.zip/EX7700-V1.0.0.222/_EX7700-V1.0.0.222.img.extracted/squashfs-root/sbin/scan_result_process
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: NS
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 10
Call stack:
--------------------------------------
```

# Misuse-24 (FP)

Pattern: FP

Sum: 8

Desc: srandom is called

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/bin/cupsd
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsCrypto Irrelevant
Pattern: Authors' incomprehensive understanding of cryptographic APIs
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 8
Call stack:
--------------------------------------
```

# Misuse-25 (ITP-3)

Pattern: ITP-3

Sum: 8

Desc: Generating random time interval

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/udev/lib/udev/scsi_id
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 8
Call stack:
--------------------------------------
```

# Misuse-26 (ITP-3)

Pattern: ITP-3

Sum: 5

Desc: RAND_seed() is called to add entropy of OpenSSL's RNG

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/DC112A_V1.0.0.60_1.0.60.zip/DC112A_V1.0.0.60_1.0.60/_DC112A-V1.0.0.60_1.0.60.chk.extracted/squashfs-root/usr/sbin/email
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functionsNOT SURE
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 5
Call stack:
--------------------------------------
```

# Misuse-27 (NS)

Pattern: UNKNOWN

Sum: 5

Desc: Not Sure

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Linksys/FW_EA6700_1.1.40.176451_prod.img/_FW_EA6700_1.1.40.176451_prod.img.extracted/squashfs-root/lib/libcares.so.2.1.0
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: NS
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 5
Call stack:
--------------------------------------
```

# Misuse-28 (ITP-3)

Pattern: ITP-3

Sum: 5

Desc: Generating random time interval

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/lib/libwbclient.so.0
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 5
Call stack:
--------------------------------------
```

# Misuse-29 (ITP-3)

Pattern: ITP-3

Sum: 5

Desc: Called but not used

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract//Netgear/DM111PSPv2_v1.1.00.09_NA.zip/DM111PSPv2_v1.1.00.09_NA/_DM111PSPv2_v1.1.00.09_NA.img.extracted/squashfs-root/sbin/netgear_ntp
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Pattern: Random number generation (RNG) functions might be used in non-security contexts
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 5
Call stack:
--------------------------------------
```

5
Call stack:
--------------------------------------
```

