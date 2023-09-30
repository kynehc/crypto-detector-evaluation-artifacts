/*
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/evp_aes_ecb
Rule: Rule-4. Do not use electronic code book (ECB) mode for encryption
Function name: EVP_aes_128_ecb (0x0)
Data: 
Path: ['0x40083f']
Count: 1
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_mips.bin/_mwe_mips.bin.extracted/squashfs-root/evp_aes_ecb
Rule: Rule-4. Do not use electronic code book (ECB) mode for encryption
Function name: EVP_aes_128_ecb (0x0)
Data: 
Path: ['0x400abc']
Count: 1
Call stack:
--------------------------------------
*/
#include "openssl/evp.h"
#include "common.h"

void test_evp_aes_ecb(){
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_128_ecb(), NULL, rand_bytes(16), NULL);
    uint8_t out[16];
    int outl;
    EVP_EncryptUpdate(ctx, out, &outl, rand_bytes(16), 16);
    EVP_EncryptFinal_ex(ctx, out, &outl);
    EVP_CIPHER_CTX_free(ctx);
}

int main(){
    test_evp_aes_ecb();
}