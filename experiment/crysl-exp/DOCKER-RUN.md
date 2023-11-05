#### Preparation

We provide a [Dockerfile](./Dockerfile) to build a docker for running our experiment on CogniCrypt_SAST. 

(The Dockerfile is based on Ubuntu 20.04. In case your apt-get source does not support fetching certain libraries for 20.04, we provide an alternative [Dockerfile](./Dockerfile-22.04) based on Ubuntu 22.04.)

```
cd crypto-detector-evaluation-artifacts/experiment/crysl-exp

docker build -t cs-exp .
```



After image build successfully, use follow command to run a container and get into the instance.

```
docker run -it --rm cs-exp
```



Set up Java 8 for use

```
update-java-alternatives --list
```
```
root@342a437d94e1:/experiment# update-java-alternatives --list
java-1.17.0-openjdk-amd64      1711       /usr/lib/jvm/java-1.17.0-openjdk-amd64
java-1.8.0-openjdk-amd64       1081       /usr/lib/jvm/java-1.8.0-openjdk-amd64
```

Use the name for java-1.8 in the output of previous command, which is `java-1.8.0-openjdk-amd64` in this case.
```
update-java-alternatives --set java-1.8.0-openjdk-amd64
```



Compile the CogniCrypt_SAST:

```
cd CryptoAnalysis/

mvn package -DskipTests=true
```



---

### Execution

The experiment is conducted on 3489 APKs. Here, we use a small set of APKs as an example to demonstrate how to run it. To reproduce the entire experiment, please replace the APKs in `E2-apks` with the complete set of 3489 APKs.

```
./run.sh
```



---

### Results

After finished running CogniCrypt_SAST on the apks, use this python script to merge the individual reported alarms into rule-based ones.

```
cd result/

python3 /experiment/logparse.py E2-apks rulebased_result
```



The result is in the `rulebased_result`.

```
ls rulebased_result

cat rulebased_result/javax.crypto.spec.IvParameterSpec
```

```
----------------------------------------------------------------------
#1
Class: net.oschina.app.common.CyptoUtils
Method: java.lang.String encode(java.lang.String,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
net.oschina.app_18.apk                                      => at statement: specialinvoke r3.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r5)

----------------------------------------------------------------------
#2
Class: net.oschina.app.common.CyptoUtils
Method: java.lang.String decode(java.lang.String,java.lang.String)

Error Type: RequiredPredicateError
Error Reason: First parameter was not properly generated as randomized
Apk Num: 1
net.oschina.app_18.apk                                      => at statement: specialinvoke r3.<javax.crypto.spec.IvParameterSpec: void <init>(byte[])>($r5)
```

