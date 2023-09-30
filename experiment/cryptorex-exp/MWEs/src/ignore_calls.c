/*

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract/mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/ignore_calls
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: srand (0x4005ca)
Data: 123
Path: ['0x4005d1', '0x4005c5']
Count: 1
Call stack:
-> test_ignore_calls (0x4005c5)
--------------------------------------

*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include "openssl/evp.h"

int get_random_seed(int fake_arg){
    return time(NULL);
}

void test_ignore_calls(){
    int seed = get_random_seed(123);    // [!!!] Static seed
    srand(seed);
}

int main(){
    EVP_aes_128_cbc();  // To let CryptoREX not ignore this binary
    test_ignore_calls();
}