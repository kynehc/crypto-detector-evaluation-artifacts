This experiment is to validate the refined CryptoGuard can reduce false positives cause by variable reassignment (Pattern #1).

### Preparation

Follow below steps to compile [refined CryptoGuard](./experiment/cryptoguard-exp/cryptoguard-refined) and [original CryptoGuard](./experiment/cryptoguard-exp/cryptoguard-92551ee). We recommend using Ubuntu 20.04.1 or 20.04.6 LTS as the system version, as our evaluations are conducted on these two versions.

0. miniconda for python environments

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

activate conda

```
conda activate
```



1. Java JDK versions

openjdk-17-jdk for android sdkmanager

```
sudo apt-get install openjdk-17-jdk
```

openjdk-8-jdk 

```
sudo apt-get install openjdk-8-jdk
```

Download Openjdk-7-jdk from https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html.

```
tar -xvf jdk-7u80-linux-x64.tar.gz
```

```
sudo mv jdk1.7.0_80 /usr/lib/jvm/
```



2. install sdkman and gradle

```
curl -s "https://get.sdkman.io" | bash
```

```
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

```
sdk version
```



```
sdk list gradle
```

```
sdk install gradle 4.6
```

```
sdk use gradle 4.6
```

```
gradle --version
```



if you encounter jvm problem, please make sure you are using jdk8. To select jdk-8 as default:

```
update-java-alternatives --list
```

```
update-alternatives --config java
```





2. install Android sdk platforms:

Download android sdk command line tools:

```
curl https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip --output commandlinetools-linux-10406996_latest.zip
```

extract the command line tools

```
unzip commandlinetools-linux-10406996_latest.zip
```

Choose jdk-17 to use

```
update-java-alternatives --list
```

```
update-alternatives --config java
```

Install the required sdk versions:

```
cmdline-tools/bin/sdkmanager "platforms;android-33" "platforms;android-32" "platforms;android-31" "platforms;android-30" "platforms;android-29" "platforms;android-28" "platforms;android-27" "platforms;android-26" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platforms;android-22" "platforms;android-21" --sdk_root="android-sdks"
```



2. build refined cryptoguard and original cryptoguard

```sh
cd experiment/cryptoguard-exp/cryptoguard-refined
```

Create a file to setup environments for android sdk, jdk8, jdk7.

```
vim _cryptoguard.source
```

write the following content including corresponding paths to the file:

```
export ANDROID_HOME=/home/android-sdks/platforms
export JAVA7_HOME=/usr/lib/jvm/jdk1.7.0_80
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

```
source _cryptoguard.source
```

install required python packages

```
pip install nbformat
```

build the refiend cryptoguard

```
make
```



### Execution

For a scale-down version of the experiment comparing refined cryptoguard and original cryptoguard, we select one batch of verified alarms, #2 in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule3-analysis.md`, caused by Pattern #1 (in paper).

We choose the apks violated for this #2 in `rule3-analysis.md`. The apks are located at [here](./experiment/cryptoguard-exp/E2-apks/) (Two apps have been excluded from this experiment due to long analysis time with both original and refined cryptoguard, which would time out.) 

After build successfully for refined cryptoguard and original cryptoguard, then we can run them on the same batch of apks.

We provide script to parallel running:

```sh
sudo apt install parallel
```

```sh
./run.sh
```

It can also use the below command to run on one App.

```
java -jar -Xmx16g -Xss60m cryptoguard.jar -in apk -s APP_NAME -t -H -m L -st -depth 1 -o ./fd_result/APP_NAME.txt &> ./fd_log/APP_NAME.log
```

After finished parallel running, use this python script to merge the individual reported alarms into rule-based ones.

```
python logparse.py fd_result rulebased_result
```


### Results

Compare the merged rule3 alarms obtained from refined cryptoguard and original cryptoguard.

Refined cryptoguard:
```
Rule: 3 Used constant keys in code

------------------------------------------------
#1
Class: org.apache.commons.httpclient.auth.NTLM
Method: byte[] hashPassword(java.lang.String,byte[])
Apk Num:3

Apk:net.oschina.app_18.apk
Err: Found: Constant "0"
Err: Found: Constant "0"

Apk:org.aykit.MyOwnNotes_11.apk
Err: Found: Constant "0"
Err: Found: Constant "0"

Apk:org.documentfoundation.libreoffice_11.apk
Err: Found: Constant "0"
Err: Found: Constant "0"

Misuse Num:6
------------------------------------------------

rule 3 count overall 6 misuses
rule 3 count unique 6 misuses
unique methods 1
unique apks 1
```

original cryptoguard (commit 92551ee)
```
Rule: 3 Used constant keys in code

------------------------------------------------
#1
Class: org.apache.commons.httpclient.auth.NTLM
Method: byte[] hashPassword(java.lang.String,byte[])
Apk Num:9

Apk:com.bytesforge.linkasanote_30499.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:net.oschina.app_18.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Apk:org.aykit.MyOwnNotes_11.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Apk:com.averi.worldscribe_27.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.spisoft.quicknote_241.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:nl.mpcjanssen.simpletask.nextcloud_10009003.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:com.mendhak.gpslogger_120.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Apk:org.documentfoundation.libreoffice_11.apk
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "75"
Err: Found: Constant "36"
Err: Found: Constant "64"
Err: Found: Constant "37"
Err: Found: Constant "83"
Err: Found: Constant "35"
Err: Found: Constant "0"
Err: Found: Constant "33"

Apk:theakki.synctool_100.apk
Err: Found: Constant "33"
Err: Found: Constant "36"
Err: Found: Constant "37"
Err: Found: Constant "0"
Err: Found: Constant "71"
Err: Found: Constant "83"
Err: Found: Constant "0"
Err: Found: Constant "35"
Err: Found: Constant "64"
Err: Found: Constant "75"

Misuse Num:90
------------------------------------------------

rule 3 count overall 90 misuses
rule 3 count unique 90 misuses
unique methods 1
unique apks 1
```