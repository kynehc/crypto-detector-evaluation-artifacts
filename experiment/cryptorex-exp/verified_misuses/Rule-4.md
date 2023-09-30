# Summary

| Pattern | # of Raw Misuses | # of Reported Misuses | # of Grouped Misuses |
| ------- | ---------------- | --------------------- | -------------------- |
| ITP-1   | 0                | 0                     | 0                    |
| ITP-2   | 0                | 0                     | 0                    |
| ITP-3   | 8                | 5                     | 1                    |
| TP      | 136              | 89                    | 7                    |
| FP      | 28               | 12                    | 2                    |
| Total   | 172              | 106                   | 10                   |

# Misuse-1 (FP)

Pattern: FP

Sum: 24

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6200-V1.0.3.94_1.1.128.zip/EX6200-V1.0.3.94_1.1.128/_EX6200-V1.0.3.94_1.1.128.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd60c)
Data: "ADMIN_PASS",0
Path: ['0xd6d0', '0xd6cc', '0xd634', '0xd700', '0xd6fc', '0xd62c', '0xd614', '0xd5f8']
Count: 4
Call stack:
-> sub_d6d0 (0xd6d0)
-> sub_d700 (0xd700)
-> sub_d5f8 (0xd5f8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6200-V1.0.3.94_1.1.128.zip/EX6200-V1.0.3.94_1.1.128/_EX6200-V1.0.3.94_1.1.128.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd60c)
Data: "ADMIN_PASS",0
Path: ['0xd640', '0xd634', '0xd700', '0xd6fc', '0xd62c', '0xd614', '0xd5f8']
Count: 4
Call stack:
-> sub_d700 (0xd700)
-> sub_d5f8 (0xd5f8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DC112A_V1.0.0.60_1.0.60.zip/DC112A_V1.0.0.60_1.0.60/_DC112A-V1.0.0.60_1.0.60.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd6ac)
Data: "ADMIN_PASS",0
Path: ['0xd770', '0xd76c', '0xd6d4', '0xd7a0', '0xd79c', '0xd6cc', '0xd6b4', '0xd698']
Count: 2
Call stack:
-> sub_d770 (0xd770)
-> sub_d7a0 (0xd7a0)
-> sub_d698 (0xd698)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DC112A_V1.0.0.60_1.0.60.zip/DC112A_V1.0.0.60_1.0.60/_DC112A-V1.0.0.60_1.0.60.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd6ac)
Data: "ADMIN_PASS",0
Path: ['0xd6e0', '0xd6d4', '0xd7a0', '0xd79c', '0xd6cc', '0xd6b4', '0xd698']
Count: 2
Call stack:
-> sub_d7a0 (0xd7a0)
-> sub_d698 (0xd698)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/AC1450-V1.0.0.36_10.0.17.zip/AC1450-V1.0.0.36_10.0.17/_AC1450-V1.0.0.36_10.0.17.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd750)
Data: "ADMIN_PASS",0
Path: ['0xd814', '0xd810', '0xd778', '0xd844', '0xd840', '0xd770', '0xd758', '0xd73c']
Count: 4
Call stack:
-> sub_d814 (0xd814)
-> sub_d844 (0xd844)
-> sub_d73c (0xd73c)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/AC1450-V1.0.0.36_10.0.17.zip/AC1450-V1.0.0.36_10.0.17/_AC1450-V1.0.0.36_10.0.17.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd750)
Data: "ADMIN_PASS",0
Path: ['0xd784', '0xd778', '0xd844', '0xd840', '0xd770', '0xd758', '0xd73c']
Count: 4
Call stack:
-> sub_d844 (0xd844)
-> sub_d73c (0xd73c)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/R7300-V1.0.0.74_1.0.29.zip/R7300-V1.0.0.74_1.0.29/_R7300-V1.0.0.74_1.0.29.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd754)
Data: "ADMIN_PASS",0
Path: ['0xd818', '0xd814', '0xd77c', '0xd848', '0xd844', '0xd774', '0xd75c', '0xd740']
Count: 2
Call stack:
-> sub_d818 (0xd818)
-> sub_d848 (0xd848)
-> sub_d740 (0xd740)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/R7300-V1.0.0.74_1.0.29.zip/R7300-V1.0.0.74_1.0.29/_R7300-V1.0.0.74_1.0.29.chk.extracted/squashfs-root/usr/sbin/bftpd
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd754)
Data: "ADMIN_PASS",0
Path: ['0xd788', '0xd77c', '0xd848', '0xd844', '0xd774', '0xd75c', '0xd740']
Count: 2
Call stack:
-> sub_d848 (0xd848)
-> sub_d740 (0xd740)
--------------------------------------
```

# Misuse-2 (FP)

Pattern: FP

Sum: 4

Desc: Bug caused by ignoring call-return edges

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DG834GT_V1.03.23.zip/DG834GT_V1.03.23/_DG834GT_V1.03.23.img.extracted/squashfs-root-0/usr/sbin/cfm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x4393a8)
Data: "admin"
Path: ['0x4392a8', '0x4393b4', '0x439398']
Count: 1
Call stack:
-> pw_encrypt (0x4392a8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DG834GT_V1.03.23.zip/DG834GT_V1.03.23/_DG834GT_V1.03.23.img.extracted/squashfs-root-0/usr/sbin/cfm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x439420)
Data: "support"
Path: ['0x4392a8', '0x43942c', '0x439414']
Count: 1
Call stack:
-> pw_encrypt (0x4392a8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DG834GT_V1.03.23.zip/DG834GT_V1.03.23/_DG834GT_V1.03.23.img.extracted/squashfs-root-0/usr/sbin/cfm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x43947c)
Data: "user"
Path: ['0x4392a8', '0x439488', '0x439470']
Count: 1
Call stack:
-> pw_encrypt (0x4392a8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DG834GT_V1.03.23.zip/DG834GT_V1.03.23/_DG834GT_V1.03.23.img.extracted/squashfs-root-0/usr/sbin/cfm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x4394d8)
Data: "nobody"
Path: ['0x4392a8', '0x4394e4', '0x4394cc']
Count: 1
Call stack:
-> pw_encrypt (0x4392a8)
--------------------------------------
```

# Misuse-3 (TP)

Pattern: TP

Sum: 14

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/boa
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x424310']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/boa
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x4245b4']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D6000_V1.0.0.80_1.0.1.zip/D6000_V1.0.0.80_1.0.1/_D6000-V1.0.0.80_1.0.1.bin.extracted/squashfs-root/userfs/bin/boa
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Pattern: TP
Data: "$1$"<0>
Path: ['0x4243d0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D6000_V1.0.0.80_1.0.1.zip/D6000_V1.0.0.80_1.0.1/_D6000-V1.0.0.80_1.0.1.bin.extracted/squashfs-root/userfs/bin/boa
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x42467c']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/cfg_manager
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x45b074']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/cfg_manager
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x45af58)
Data: "$1$"
Path: ['0x45af50']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/cfg_manager
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x45b088)
Data: "$1$"
Path: ['0x45b084']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/cfg_manager
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x45b2c4']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/D3600_V1.0.0.76_1.0.1.zip/D3600_V1.0.0.76_1.0.1/_D3600-V1.0.0.76_1.0.1.bin.extracted/squashfs-root/userfs/bin/cfg_manager
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: "$1$"<0>
Path: ['0x45af44']
Count: 2
Call stack:
--------------------------------------
```

# Misuse-4 (ITP-3)

Pattern: ITP-3

Sum: 8

Desc: Cryptographic misuses in testing context

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Linksys/FW_EA6200_1.1.41.188556_prod.img/_FW_EA6200_1.1.41.188556_prod.img.extracted/squashfs-root/usr/sbin/eurl
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x9114)
Data: "openssl.c",0
Path: ['0x9100']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Linksys/FW_EA3500_1.1.40.162464_prod.zip/FW_EA3500_1.1.40.162464_prod/_FW_EA3500_1.1.40.162464_prod.SSA.extracted/jffs2-root/usr/sbin/eurl
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x9d18)
Data: "openssl.c",0
Path: ['0x9cf4']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Linksys/FW_EA6900v2_2.0.3.186963_prod.img/_FW_EA6900v2_2.0.3.186963_prod.img.extracted/jffs2-root/usr/sbin/eurl
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x0)
Data: "openssl.c"<0>
Path: ['0x401770']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Linksys/FW_WRT1200ACV2_2.0.6.191786_prod.img/_FW_WRT1200ACV2_2.0.6.191786_prod.img.extracted/jffs2-root/usr/sbin/eurl
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x1152c)
Data: "openssl.c",0
Path: ['0x1150c']
Count: 3
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Linksys/FW_EA2700_1.1.40.189581_prod.img/_FW_EA2700_1.1.40.189581_prod.img.extracted/squashfs-root/usr/sbin/eurl
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x402784)
Data: "openssl.c"
Path: ['0x402754']
Count: 1
Call stack:
--------------------------------------
```

# Misuse-5 (TP)

Pattern: TP

Sum: 41

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21f74)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21f74']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21f98)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21f98']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x220d4)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x220d0']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x22094)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x22094']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x223ec)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x223ec']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x2335c)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x23358']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x23380)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x2337c']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000-V1.0.1.6.zip/PLW1000-V1.0.1.6/_PLW1000-V1.0.1.6.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x2339c)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x2339c']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x209c0)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x209c0']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x209e4)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x209e4']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x20b20)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x20b1c']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x20ae0)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x20ae0']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x20e38)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x20e38']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21e58)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21e54']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21e7c)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21e78']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21e98)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21e98']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.14.zip/PLW1000v2-V1.0.0.14/_PLW1000v2-V1.0.0.14.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x214f4)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x214f0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.18.zip/PLW1000v2-V1.0.0.18/_PLW1000v2-V1.0.0.18.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21da8)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21da4']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.18.zip/PLW1000v2-V1.0.0.18/_PLW1000v2-V1.0.0.18.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21dcc)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21dc8']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.18.zip/PLW1000v2-V1.0.0.18/_PLW1000v2-V1.0.0.18.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21de8)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x21de8']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/PLW1000v2-V1.0.0.18.zip/PLW1000v2-V1.0.0.18/_PLW1000v2-V1.0.0.18.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x374a0)
Data: 0x24,"1",0x24,"TW",0
Path: ['0x374a0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x42f4d0)
Data: "$1$TW"
Path: ['0x42f4c0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x431130)
Data: "$1$TW"
Path: ['0x431120']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x43119c)
Data: "$1$TW"
Path: ['0x43118c']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x431204)
Data: "$1$TW"
Path: ['0x4311f8']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x431230)
Data: "$1$TW"
Path: ['0x43122c']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x4311d0)
Data: "$1$TW"
Path: ['0x4311c4']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/EX6110_EX3110_EX5000_EX2800-V1.0.1.80.zip/EX6110_EX3110_EX5000_EX2800-V1.0.1.80/_EX6110_EX3110_EX5000_EX2800-V1.0.1.80.img.extracted/squashfs-root/usr/bin/logic
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x431164)
Data: "$1$TW"
Path: ['0x431158']
Count: 1
Call stack:
--------------------------------------
```

# Misuse-6 (TP)

Pattern: TP

Sum: 1

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DVG-3104MS_FIRMWARE_VOICECENTER_DEVICE_UPDATE_1.0.2.0.3.ZIP/DVG-3104MS_FIRMWARE_VOICECENTER_DEVICE_UPDATE_1.0.2.0.3/VoiceCenter_Device_Update_11-19-2008/DVG-3104MS/1.02.03/_DVG-3104MS_SP1_01.02.03.flash.extracted/squashfs-root/bin/login
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x401114)
Data: "xx"
Path: ['0x401198', '0x401180', '0x401164', '0x401148', '0x401138', '0x40110c']
Count: 1
Call stack:
--------------------------------------
```

# Misuse-7 (TP)

Pattern: TP

Sum: 3

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DGN3500-V1.1.00.37NA.zip/DGN3500-V1.1.00.37NA/_DGN3500-V1.1.00.37_1.00.37NA.img.extracted/squashfs-root/usr/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41c534)
Data: "sc"
Path: ['0x41c524']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DGN3500-V1.1.00.37NA.zip/DGN3500-V1.1.00.37NA/_DGN3500-V1.1.00.37_1.00.37NA.img.extracted/squashfs-root/usr/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41c534)
Data: "sc"
Path: ['0x41c56c', '0x41c55c', '0x41c544', '0x41c524']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/DGN3500-V1.1.00.37NA.zip/DGN3500-V1.1.00.37NA/_DGN3500-V1.1.00.37_1.00.37NA.img.extracted/squashfs-root/usr/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41c534)
Data: "sc"
Path: ['0x41c52c']
Count: 1
Call stack:
--------------------------------------
```

# Misuse-8 (TP)

Pattern: TP

Sum: 10

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x2405c)
Data: 0x24,"1",0x24,0
Path: ['0x2405c']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-RT-AC3200-ARM--140-AIO-64K.zip/tomato-RT-AC3200-ARM--140-AIO-64K/image/_tomato-RT-AC3200-ARM--140-AIO-64K.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x23f3c)
Data: 0x24,"1",0x24,0
Path: ['0x23f38']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-K26USB-1.28.RT-MIPSR2-140-AIO.zip/tomato-K26USB-1.28.RT-MIPSR2-140-AIO/image/_tomato-K26USB-1.28.RT-MIPSR2-140-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41bd54)
Data: "$1$"
Path: ['0x41bd44']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-K26USB-1.28.RT-MIPSR2-140-AIO.zip/tomato-K26USB-1.28.RT-MIPSR2-140-AIO/image/_tomato-K26USB-1.28.RT-MIPSR2-140-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41beec)
Data: "$1$"
Path: ['0x41bed8']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/tomato-K26USB-1.28.RT-MIPSR2-140-AIO.zip/tomato-K26USB-1.28.RT-MIPSR2-140-AIO/image/_tomato-K26USB-1.28.RT-MIPSR2-140-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x41beec)
Data: "$1$"
Path: ['0x41bedc']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x21254)
Data: 0x24,"1",0x24,0
Path: ['0x21254']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.zip/freshtomato-RT-AC3200-ARM-2022.5-AIO-64K/_freshtomato-RT-AC3200-ARM-2022.5-AIO-64K.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x2111c)
Data: 0x24,"1",0x24,0
Path: ['0x21118']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.zip/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO/_freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x418cc0)
Data: "$1$"
Path: ['0x418cb0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.zip/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO/_freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x418e9c)
Data: "$1$"
Path: ['0x418e84']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Tomato/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.zip/freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO/_freshtomato-K26USB-NVRAM32K_RT-MIPSR2-2022.5-AIO.trx.extracted/squashfs-root/sbin/rc
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x418e9c)
Data: "$1$"
Path: ['0x418e88']
Count: 1
Call stack:
--------------------------------------
```

# Misuse-9 (TP)

Pattern: TP

Sum: 59

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1eb20)
Data: "$1$mldcsfp$"
Path: ['0x1eb18']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1ae6c)
Data: "$1$mldcsfp$"
Path: ['0x1ae64']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1f72c)
Data: "$1$mldcsfp$"
Path: ['0x1f728']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1f6a0)
Data: "$1$mldcsfp$"
Path: ['0x1f69c']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x2696c)
Data: "$1$mldcsfp$"
Path: ['0x26968']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1fb00)
Data: "$1$mldcsfp$"
Path: ['0x1fafc']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1fa78)
Data: "$1$mldcsfp$"
Path: ['0x1fa74']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1ef30)
Data: "$1$mldcsfp$"
Path: ['0x1ef28']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1b288)
Data: "$1$mldcsfp$"
Path: ['0x1b280']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x10016c40)
Data: "$1$mldcsfp$"
Path: ['0x10016c30']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001b200)
Data: "$1$mldcsfp$"
Path: ['0x1001b1f8']
Count: 1
Call stack:
-> sub_1001b1f8 (0x1001b1f8)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001bf4c)
Data: "$1$mldcsfp$"
Path: ['0x1001bf3c']
Count: 1
Call stack:
-> sub_1001bf3c (0x1001bf3c)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001bff4)
Data: "$1$mldcsfp$"
Path: ['0x1001bfe4']
Count: 1
Call stack:
-> sub_1001bfe4 (0x1001bfe4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001d2e0)
Data: "$1$mldcsfp$"
Path: ['0x1001d2d4']
Count: 1
Call stack:
-> sub_1001d2d4 (0x1001d2d4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x10024040)
Data: "$1$mldcsfp$"
Path: ['0x10024038']
Count: 1
Call stack:
-> sub_10024038 (0x10024038)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x100241ac)
Data: "$1$mldcsfp$"
Path: ['0x100241a0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-150_A1_FIRMWARE_1.08B29.ZIP/DSR-150_A1_FIRMWARE_1.08B29/_DSR-150_A1_FW1.08B29_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x205c8)
Data: "$1$mldcsfp$"
Path: ['0x205c4']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-150_A1_FIRMWARE_1.08B29.ZIP/DSR-150_A1_FIRMWARE_1.08B29/_DSR-150_A1_FW1.08B29_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x20540)
Data: "$1$mldcsfp$"
Path: ['0x2053c']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-150_A1_FIRMWARE_1.08B29.ZIP/DSR-150_A1_FIRMWARE_1.08B29/_DSR-150_A1_FW1.08B29_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1f9f8)
Data: "$1$mldcsfp$"
Path: ['0x1f9f0']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-150_A1_FIRMWARE_1.08B29.ZIP/DSR-150_A1_FIRMWARE_1.08B29/_DSR-150_A1_FW1.08B29_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1bb1c)
Data: "$1$mldcsfp$"
Path: ['0x1bb14']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x10016ee0)
Data: "$1$mldcsfp$"
Path: ['0x10016ed0']
Count: 4
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001b96c)
Data: "$1$mldcsfp$"
Path: ['0x1001b964']
Count: 3
Call stack:
-> sub_1001b964 (0x1001b964)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001c6f0)
Data: "$1$mldcsfp$"
Path: ['0x1001c6e0']
Count: 3
Call stack:
-> sub_1001c6e0 (0x1001c6e0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001c798)
Data: "$1$mldcsfp$"
Path: ['0x1001c788']
Count: 3
Call stack:
-> sub_1001c788 (0x1001c788)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001da88)
Data: "$1$mldcsfp$"
Path: ['0x1001da7c']
Count: 3
Call stack:
-> sub_1001da7c (0x1001da7c)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW.ZIP/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW/_DSR-1000N_A1_FW1.09B61_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001b95c)
Data: "$1$mldcsfp$"
Path: ['0x1001b954']
Count: 1
Call stack:
-> sub_1001b954 (0x1001b954)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW.ZIP/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW/_DSR-1000N_A1_FW1.09B61_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001c6e0)
Data: "$1$mldcsfp$"
Path: ['0x1001c6d0']
Count: 1
Call stack:
-> sub_1001c6d0 (0x1001c6d0)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW.ZIP/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW/_DSR-1000N_A1_FW1.09B61_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001c788)
Data: "$1$mldcsfp$"
Path: ['0x1001c778']
Count: 1
Call stack:
-> sub_1001c778 (0x1001c778)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW.ZIP/DSR-1000N_REVA_FIRMWARE_1.09.B61_WW/_DSR-1000N_A1_FW1.09B61_WW.extracted/squashfs-root/sslvpn/bin/smm
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1001da30)
Data: "$1$mldcsfp$"
Path: ['0x1001da24']
Count: 1
Call stack:
-> sub_1001da24 (0x1001da24)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/bin/sslvpnConfig
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xde3c)
Data: "$1$mldcsfp$"
Path: ['0xde34']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/bin/sslvpnConfig
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xf228)
Data: "$1$mldcsfp$"
Path: ['0xf220']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DWC-1000_FIRMWARE_4.1.0.2.ZIP/DWC-1000_FIRMWARE_4.1.0.2/_DWC-1000_A1_FW_v4.1.0.2_10222W.extracted/squashfs-root/bin/sslvpnConfig
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x1000ed88)
Data: "$1$mldcsfp$"
Path: ['0x1000ed80']
Count: 1
Call stack:
-> sub_1000ed80 (0x1000ed80)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-150_A1_FIRMWARE_1.08B29.ZIP/DSR-150_A1_FIRMWARE_1.08B29/_DSR-150_A1_FW1.08B29_WW.extracted/squashfs-root/bin/sslvpnConfig
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xf390)
Data: "$1$mldcsfp$"
Path: ['0xf388']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-1000_A1_FIRMWARE_v2.13_WW.zip/DSR-1000_A1_FIRMWARE_v2.13_WW/_DSR-1000_A1_FW2.13_WW.extracted/squashfs-root/bin/sslvpnConfig
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x10006c30)
Data: "$1$mldcsfp$"
Path: ['0x10006c28']
Count: 4
Call stack:
-> sub_10006c28 (0x10006c28)
--------------------------------------
```

# Misuse-10 (TP)

Pattern: TP

Sum: 8

Desc: Using constant salt for encrypting passwords

```
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318G_V3.1.1-18.zip/FVS318G_V3.1.1-18/_fvs318g_v3.1.1-18.img.extracted/squashfs-root/pfrm1.0/tinylogin
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xd17c)
Data: 0x24,"1",0x24,0
Path: ['0xe234', '0xd178']
Count: 1
Call stack:
-> sub_e234 (0xe234)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/Netgear/FVS318N_V4.3.5-3.zip/FVS318N_V4.3.5-3/_FVS318N_v4.3.5-3.img.extracted/squashfs-root/bin/tinylogin
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xc900)
Data: 0x24,"1",0x24,0
Path: ['0xe154', '0xc900']
Count: 2
Call stack:
-> sub_e154 (0xe154)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DES-1210-08P_REVA_FIRMWARE_2.03.B016_BETA_WW.ZIP/DES-1210-08P_REVA_FIRMWARE_2.03.B016_BETA_WW/_DES-1210-08P_A1_2_03_B016_BETA.hex.extracted/squashfs-root/bin/tinylogin
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x408870)Misconception about Cryptographic APIs
Path: ['0x404494', '0x409768', '0x4097dc', '0x409754', '0x409744', '0x409714', '0x4096e4', '0x408868']
Count: 2
Call stack:
-> pw_encrypt (0x404494)
-> sub_4096e4 (0x4096e4)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/CRYPTOREX_criticism/tmp/extract/D-Link/DSR-250N_FIRMWARE_1.05B20.ZIP/DSR-250N_FIRMWARE_1.05B20/dsr250n_105B20/_DSR-250N_FW_1.05B20_WW.extracted/squashfs-root/bin/tinylogin
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0xc6fc)
Data: 0x24,"1",0x24,0
Path: ['0xde78', '0xc6fc']
Count: 3
Call stack:
-> sub_de78 (0xde78)
--------------------------------------
```nstant salts for password-based encryption (PBE)
Function name: crypt (0xc6fc)
Data: 0x24,"1",0x24,0
Path: ['0xde78', '0xc6fc']
Count: 3
Call stack:
-> sub_de78 (0xde78)
--------------------------------------
```