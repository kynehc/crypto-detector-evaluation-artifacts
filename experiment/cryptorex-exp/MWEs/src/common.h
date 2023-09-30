#include <stdlib.h>
#include <stdint.h>
#include <time.h>

void seed(){
    srand(time(NULL));
}

uint8_t* rand_bytes(size_t n){
    static int seeded = 0;
    if(!seeded){
        seed();
        seeded = 1;
    }
    uint8_t* buf = malloc(n * sizeof(uint8_t));
    while(n--){
        buf[n] = rand() & 0xFF;
    }
    return buf;
}