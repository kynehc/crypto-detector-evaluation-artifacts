libs="-lcrypt -lcrypto -lssl"
common_options="-Iinclude -Wno-deprecated-declarations"

for src in src/*.c
do
    bin=$(echo $(basename $src) | cut -d . -f1)
    
    arm-linux-gnueabihf-gcc $src -o bin/arm/$bin -Llib/arm $libs $common_options
    mipsel-linux-gnu-gcc $src -o bin/mips/$bin -Llib/mips $libs $common_options

    python gen_ir.py bin/arm/$bin
    python gen_ir.py bin/mips/$bin
done

rm -f mwe_arm.bin mwe_mips.bin
mksquashfs bin/arm mwe_arm.bin -quiet
mksquashfs bin/mips mwe_mips.bin -quiet

cp -f mwe_arm.bin ../CryptoREX/input/mwe_arm.bin
cp -f mwe_mips.bin ../CryptoREX/input/mwe_mips.bin