This experiment is to validate the refined CryptoGuard can reduce false positives cause by variable reassignment (Pattern #1).



### Preparation

We provider a [Dockerfile](./experiment/cryptoguard-exp/Dockerfile) to build a docker for running our scale-down experiment, to validate the refined CryptoGuard can reduce false positives than the original CryptoGuard.

Since we have a large file in the repo, git has to be equipped with [lfs](https://git-lfs.com/). To equip the lfs in your git, use below commands:
```
sudo apt-get install git-lfs

git lfs install
```



After installing lfs into git, then we can clone the repo.
```
git clone https://github.com/kynehc/crypto-detector-evaluation-artifacts.git

cd experiment/cryptoguard-exp

docker build -t cg-exp .
```

After image build successfully, use follow command to run a container and get into the instance.
```
docker run -it --rm cg-exp
```


Install the gradle-4.6
```
sdk install gradle 4.6
```


We respectively compile [cryptoguard-92551ee](./experiment/cryptoguard-exp/cryptoguard-92551ee/) and [refined-cryptoguard](./experiment/cryptoguard-exp/cryptoguard-refined/).

For original cryptoguard:
```
cd cryptoguard-92551ee

source _cryptoguard.source

make
```


For refined cryptoguard:
```
cd cryptoguard-refined

source _cryptoguard.source

make
```


---

### Execution

For a scale-down version of the experiment comparing refined cryptoguard and original cryptoguard, we select one batch of verified alarms, #2 in `crypto-detectors-evaluation-artifacts/experiment/cryptoguard-exp/verified_alarms/rule3-analysis.md`, caused by Pattern #1 (in paper).

We choose the apks violated for this #2 in [rule3-analysis.md](./experiment/cryptoguard-exp/verified_alarms/rule3-analysis.md). The apks are located at [here](./experiment/cryptoguard-exp/E2-apks/) (Two apps have been excluded from this experiment due to long analysis time with both original and refined cryptoguard, which would time out.) 

After build successfully for refined cryptoguard and original cryptoguard, then we can run them on the same batch of apks.

We provide script to parallel running:

```sh
cd cryptoguard-refined 
# or cd cryptoguard-92551ee

./run.sh
```


These two scale-down experiments need 10 minutes on our machine. After finished running cryptoguard on the apks, use this python script to merge the individual reported alarms into rule-based ones.
```
python3 logparse.py fd_result rulebased_result
```


Show the result.
```
cat rulebased_result/rule3
```



---

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



Original cryptoguard (commit 92551ee):
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