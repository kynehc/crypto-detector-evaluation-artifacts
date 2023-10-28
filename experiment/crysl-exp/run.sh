echo "this is for analyzing apk..."
starttime=`date +'%Y-%m-%d %H:%M:%S'`
echo "start time:"$starttime

run_dir="./runlog"
if [ ! -d "$run_dir" ]; then
	mkdir -p "$run_dir"
fi

res_dir="./result/E2-apks"
if [ ! -d "$res_dir" ]; then
	mkdir -p "$res_dir"
fi

apk_dir="E2-apks"
log_dir="./runlog/run.log"

find $apk_dir -name '*.apk'| parallel --resume --joblog $log_dir --jobs 3 "java -cp CryptoAnalysis-Android/build/CryptoAnalysis-Android-2.8.0-SNAPSHOT-jar-with-dependencies.jar -Xmx16g -Xss60m de.fraunhofer.iem.crypto.CogniCryptAndroidAnalysis {}  /experiment/android-sdks/platforms  ../Repo-JCA-rules/ output/ > ./result/{}.log"

endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "end time:"$endtime
