FROM ubuntu:focal as base
SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt update

WORKDIR /experiment

COPY . .

USER root

RUN apt install -y parallel

RUN apt-get install -y python3-pip

RUN apt-get install -y openjdk-8-jdk

RUN apt-get install -y curl zip git maven

RUN apt-get install -y openjdk-17-jdk

RUN curl https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip --output commandlinetools-linux-10406996_latest.zip

RUN unzip commandlinetools-linux-10406996_latest.zip

RUN yes | cmdline-tools/bin/sdkmanager "platforms;android-33" "platforms;android-32" "platforms;android-31" "platforms;android-30" "platforms;android-29" "platforms;android-28" "platforms;android-27" "platforms;android-26" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platforms;android-22" "platforms;android-21" --sdk_root="android-sdks"

RUN mkdir -p ~/.m2/repository/ && cp -r maven/* ~/.m2/repository/ 

RUN git clone https://github.com/CROSSINGTUD/CryptoAnalysis.git

RUN cd CryptoAnalysis/ && git checkout 1405ebdde9c6980084e3fa9f9de7782f80e420a4 && mv ../E2-apks . && mv ../run.sh .