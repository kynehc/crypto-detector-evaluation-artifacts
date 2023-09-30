/*

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/test_scenario
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x400656)
Data: "salt"
Path: ['0x40063f']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/test_scenario
Rule: Rule-1. Do not use constant salts for password-based encryption (PBE)
Function name: EVP_BytesToKey (0x0)
Data: "salt"<0>
Path: ['0x400838']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/test_scenario
Rule: Rule-2. Do not use constant encryption keys
Function name: EVP_BytesToKey (0x400652)
Data: "data"
Path: ['0x40063f']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/test_scenario
Rule: Rule-2. Do not use constant encryption keys
Function name: EVP_BytesToKey (0x0)
Data: "data"<0>
Path: ['0x400838']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/test_scenario
Rule: Rule-6. Do not use fewer than 1000 iterations for PBE
Function name: EVP_BytesToKey (0x0)
Data: 1
Path: ['0x40063f']
Count: 1
Call stack:
--------------------------------------

*/
#include <stdlib.h>
#include <stdint.h>

#include "openssl/evp.h"

void test_scenario(){
    // It's just for testing whether AES cipher works well
    // key and iv are not used elsewhere
    uint8_t key[256];
    uint8_t iv[256];
    // "salt"   [!!!] Constant salt
    // "data"   [!!!] Constant key
    //   1      [!!!] PBE iterations < 1000
    EVP_BytesToKey(EVP_aes_128_cbc(), NULL, "salt", "data", 4, 1, key, iv);
}

int main(){
    test_scenario();
}