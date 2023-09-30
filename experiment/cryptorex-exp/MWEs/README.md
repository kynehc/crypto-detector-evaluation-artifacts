# Minimum Working Examples (MWEs) for CryptoREX

## Directory structure
- `bin/`: compiled MWE binaries (ARM32 and MIPS32)
- `include/`: dependent head files
- `lib/`: required dynamic libraries including libcrypt.so, libssl.so, and libcrypto.so.
- `src/`: source code files of MWEs
- `ail/`: AIL (Angr Intermediate Languages) files lifted from MWE binaries
- `vex/`: VEX IR files lifted from MWE binaries
- `mwe_arm.bin` and `mwe_mips.bin`: firmware-format binaries consisting of the compiled MWE binaries

## How to compile MWEs on Ubuntu?
First we install the cross-compilers on our machine:
```
sudo apt install gcc-arm-linux-gnueabihf
sudo apt install gcc-mipsel-linux-gnu
```

We have prepared all the required shared libraries and head files in [lib/](lib/) and [include/](include/). So we just need to execute [./build.sh](./build.sh). The script will generate the contents of [bin/](bin/), [ail/](ail/), [vex/](vex/), and the firmware-format binaries [mwe_arm.bin](mwe_arm.bin) and [mwe_mips.bin](mwe_mips.bin), which will then be copied into [../CryptoREX/input/](../CryptoREX/input/).

## Test cases

### ITP-1: Both AES raw block cipher and ECB are prohibited

- `AES_encrypt() as AES block cipher`: [src/aes_encrypt.c](src/aes_encrypt.c)
- `EVP_aes_128_ecb() as AES block cipher`: [src/evp_aes_ecb.c](src/evp_aes_ecb.c)

### ITP-2: Protocol standards mandate the use of weak algorithms, modes, and constants

It is difficult to simulate protocols' behavor in a few lines of code, so we simply present the links of relevant projects on GitHub.

- `NTLM - curl`: [curl_ntlm_core.c](https://github.com/curl/curl/blob/df00df1e60053886a0f4483ae9f07dabc734361c/lib/curl_ntlm_core.c#L374)
- `AFP - Netatalk`: [uams_dhx2_pam.c](https://github.com/Netatalk/Netatalk/blob/0637355487a9fd0e8c8cfb9eebad8d832a05820f/etc/uams/uams_dhx2_pam.c#L477)

### ITP-3: Usage in non-security-critical contexts

- `rand() - generate random sleep time`: [src/rand_sleep.c](src/rand_sleep.c)
- `Test scenario - generated key and iv are not used elsewhere`: [src/test_scenario.c](src/test_scenario.c)

### FP-1: Mishandling call-return edges of CFG

- `Ignore function calls during backward slicing`: [src/ignore_calls.c](src/ignore_calls.c)

### FP-2: CryptoREX ignores seeding with srandom

- `Ignore interchangable function of srand()`: [src/ignore_srandom.c](src/ignore_srandom.c)