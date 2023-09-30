/*

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/aes_encrypt
Rule: Rule-4. Do not use electronic code book (ECB) mode for encryption
Function name: AES_encrypt (0x0)
Data: 
Path: ['0x40076f']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/aes_encrypt
Rule: Rule-4. Do not use electronic code book (ECB) mode for encryption
Function name: AES_encrypt (0x0)
Data: 
Path: ['0x400a48']
Count: 1
Call stack:
--------------------------------------

*/
#include "openssl/aes.h"
#include "common.h"

void test_aes_encrypt(){
    AES_KEY key;
    AES_set_encrypt_key(rand_bytes(16), 16 * 8, &key);
    char *in = rand_bytes(16);
    uint8_t out[16];
    AES_encrypt(in, out, &key);   // [!!!] ECB encryption
}

int main(){
    test_aes_encrypt();
}