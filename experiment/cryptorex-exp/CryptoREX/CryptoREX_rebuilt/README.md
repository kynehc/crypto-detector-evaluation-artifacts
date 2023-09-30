This is a rebuilt version of [zhanglikernel/CRYPTOREX: Large-scale Analysis of Cryptographic Misuse in IoT Devices (github.com)](https://github.com/zhanglikernel/CRYPTOREX) to make it can be easily used by other researcher

# Read recommendation

- bin2vex
  - dfs_dir()
  - decompress()
  - extractfile()
  - systemconstruct()
  - loadso()
- bin2ir
  - idarun()
  - transbin2ir()

# Environment

- linux with **root** previlege, or binwalk won't work
- Python 3.9
- angr
- buildroot
- IDA Pro v6.4 Linux

# Installation

## Install angr

Download `angr`

```
apt-get install python3-dev libffi-dev build-essential virtualenvwrapper
whereis virtualenvwrapper.sh
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv --python=$(which python3) angr && pip install angr
```

Enable virtual environment

```
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

`workon`  to check available environment 

```
root@kali:~# workon
angr
```

Enter `angr` virtual environment

```
root@kali:~# workon angr
(angr) root@kali:~#
```

Exit virtual environment after the execution finished

```
(angr) root@kali:~# deactivate
root@kali:~#
```

**Angr documentation Node**: Do not attempt to solve any angr problems outside of the virtual environment

## Do not Install buildroot

This paper just use buildroot to install `ldd` under different platform to check the included libs of so file, which is very unnecessary and heavy.

Just replace `ldd` by `readelf` command line tool based on linux system

## Install IDA pro

```
dpkg --add-architecture i386
apt update
apt install libfontconfig1:i386 libXrender1:i386 libsm6:i386 libfreetype6:i386 libglib2.0-0:i386
```

## Install python requirement

```
pip install rarfile
pip install python-magic
pip install binwalk
```

# Configuration

Config your own tool path in config.py

```
home_path = "$HOME/Downloads"

buildroot_path = ""

output_path = home_path + "/CRYPTOREX/rex/rexProject"

ida_path = home_path + "/IDA_Pro_v6.4_Linux"

script_path = home_path + "/CRYPTOREX/idascript/bin2iridc.idc"

misuseprofile_path = home_path + "/CRYPTOREX/rex/misuseprofile"

excfunction_path = home_path + "/CRYPTOREX/rex/execfunction"
```

# Usage

```
python bin2vex.py <firmware_path>(input_dir) <firmware_decompressed_path>(middle_dir) <firmware_IR_PATH>(middle_dir) <detail_report_path>(output_dir) <summary_report_dir>(output_dir)
```