/*

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract//mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/ignore_srandom
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 2
Call stack:
--------------------------------------
--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract//mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/rand_sleep
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 2
Call stack:
--------------------------------------

*/
#include <stdlib.h>
#include <time.h>

void test_ignore_srandom(){
    srandom(time(NULL));
    rand();
}

int main(){
    test_ignore_srandom();
}