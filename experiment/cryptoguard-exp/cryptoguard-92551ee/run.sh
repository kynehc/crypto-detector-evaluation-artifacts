echo "this is for analyzing apk..."
starttime=`date +'%Y-%m-%d %H:%M:%S'`
echo "start time:"$starttime

apk_dir="./../E2-apks/"
run_file="./runlog/run.log"
run_dir="./runlog"
res_dir="./fd_result"
log_dir="./fd_log"

if [ ! -d "$res_dir" ]; then
	mkdir -p "$res_dir"
fi
if [ ! -d "$run_dir" ]; then
	mkdir -p "$run_dir"
fi
if [ ! -d "$log_dir" ]; then
	mkdir -p "$log_dir"
fi

ls $apk_dir | parallel --resume --joblog $run_file --jobs 6 "java -jar -Xmx16g -Xss60m cryptoguard.jar -in apk -s $apk_dir{} -t -H -m L -st -depth 1 -o ./fd_result/{}.txt &> ./fd_log/{}.log"

endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "end time:"$endtime
