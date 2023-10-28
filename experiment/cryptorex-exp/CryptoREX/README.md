# Install Modified CryptoREX

## Directory structure
- `CryptoREX_rebuilt/`: The source code of our modified CryptoREX.
- `IDA_Pro_v6.4/`: Linux version of IDA Pro. We cannot provide it in this repository as it is proprietary.
- `input/`: Input firmware images. In this repository, we already put our Minimum Working Examples (MWEs) in this directory.
- `report/`: The generated cryptographic misuse reports are stored here.
- `scripts/`: Some auxiliary Python scripts for test purposes.
- `tmp/`: Logs and intermidate files.
- `batch_test.sh`: Run it to start running CryptoREX with the firmware images in `input/`.

## Installation

Step 1: Install Ubuntu 20.04.1 or 20.04.6 LTS. CryptoREX has some issues that prevent it from working correctly on other Ubuntu versions, such as Ubuntu 22.04.3 LTS.

Step 2: Put IDA Pro 6.4 files in `IDA_Pro_v6.4` directory. Make sure `IDA_Pro_v6.4/idal` exists and works correctly. We cannot provide IDA in this repository as it is proprietary.

Step 3: Install python (>=3.8). 
```
apt-get install -y python-is-python3 python3-pip
```

It is safer to use a virtual Python environment. For example:
```
mkvirtualenv cryptorex
workon cryptorex
```
Or use miniconda. For example:
```
conda create --name cryptorex python=3.9
conda activate cryptorex
```

Step 4: Install required Python packages by `pip install -r requirements.txt`

Step 5: Install binwalk by `pip install git+https://github.com/ReFirmLabs/binwalk.git`

Finally, run `./batch_test.sh`. If everything is set up properly, you will get the reports in [report/](report/). Specifically, the overview report is located at [report/report.log](report/report.log). The expected result for our MWEs is:
```
Violation number of rule-1: 5 (5 unique)
Violation number of rule-2: 5 (5 unique)
Violation number of rule-3: 0 (0 unique)
Violation number of rule-4: 4 (4 unique)
Violation number of rule-5: 5 (3 unique)
Violation number of rule-6: 1 (1 unique)
...
```

To reproduce the entire experiment, please replace the firmwares in `input/` with the complete set of firmwares and run `./batch_test.sh` in like manner.