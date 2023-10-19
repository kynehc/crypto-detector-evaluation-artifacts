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

RUN pip install nbformat

RUN apt-get install -y openjdk-8-jdk

RUN apt-get install -y openjdk-17-jdk

RUN tar -xvf jdk-7u80-linux-x64.tar.gz

RUN cp -r jdk1.7.0_80 /usr/lib/jvm/

RUN apt-get install -y curl zip

RUN curl -s "https://get.sdkman.io" | bash

RUN source "$HOME/.sdkman/bin/sdkman-init.sh"

RUN curl https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip --output commandlinetools-linux-10406996_latest.zip

RUN unzip commandlinetools-linux-10406996_latest.zip

RUN yes | cmdline-tools/bin/sdkmanager "platforms;android-33" "platforms;android-32" "platforms;android-31" "platforms;android-30" "platforms;android-29" "platforms;android-28" "platforms;android-27" "platforms;android-26" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platforms;android-22" "platforms;android-21" --sdk_root="android-sdks"

RUN update-java-alternatives --set java-1.8.0-openjdk-amd64


# RUN sdk install gradle 4.6
# RUN cd cryptoguard-exp/cryptoguard-92551ee
# RUN source _cryptoguard.source
# RUN make
# RUN ./run.sh
# RUN python3 logparse.py fd_result rulebased_result
# RUN cat rulebased_result/rule3