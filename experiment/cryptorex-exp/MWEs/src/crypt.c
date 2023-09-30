/*

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/crypt
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x40054a)
Data: XX
Path: ['0x400543']
Count: 1
Call stack:
-> sub_400543 (0x400543)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/crypt
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x40054a)
Data: XX
Path: ['0x400545']
Count: 1
Call stack:
-> test_crypt (0x400545)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/crypt
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: crypt (0x0)
Data: XX
Path: ['0x400730']
Count: 1
Call stack:
-> test_crypt (0x400730)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/crypt
Rule: Rule-2. Do not use constant encryption keys
Function name: crypt (0x400550)
Data: "admin"
Path: ['0x400543']
Count: 1
Call stack:
-> sub_400543 (0x400543)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/crypt
Rule: Rule-2. Do not use constant encryption keys
Function name: crypt (0x400550)
Data: "admin"
Path: ['0x400545']
Count: 1
Call stack:
-> test_crypt (0x400545)
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/crypt
Rule: Rule-2. Do not use constant encryption keys
Function name: crypt (0x0)
Data: "admin"<0>
Path: ['0x400730']
Count: 1
Call stack:
-> test_crypt (0x400730)
--------------------------------------

*/
#include <unistd.h>

void test_crypt(){
    crypt("admin", "XX");   // <- constant key and constant salt
}

int main(){
    test_crypt();
}