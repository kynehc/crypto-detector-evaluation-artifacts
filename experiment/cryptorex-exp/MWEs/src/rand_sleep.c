/* 

--------------------------------------
File: /home/xx/CRYPTOREX/crypto-detectors-evaluation-artifacts/experiment/cryptorex-exp/CryptoREX/tmp/extract//mwe_arm.bin/_mwe_arm.bin.extracted/squashfs-root/rand_sleep
Rule: Rule-5. Do not use static seeds for random number generation (RNG) functions
Function name: rand
Data: rand() without srand()
Path: ['0x0']
Count: 2    <- MIPS's and ARM's reports are merged
Call stack:
--------------------------------------

*/
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

void rand_sleep(){
    sleep(60 + rand() % 60);    // [!!!] rand without srand
}

int main(){
    rand_sleep();
}