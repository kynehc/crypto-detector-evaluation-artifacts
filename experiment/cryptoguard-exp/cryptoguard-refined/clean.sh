run_dir="./runlog"
res_dir="./fd_result"
log_dir="./fd_log"

if [ -d "$res_dir" ]; then
	rm -r "$res_dir"
fi
if [ -d "$run_dir" ]; then
	rm -r "$run_dir"
fi
if [ -d "$log_dir" ]; then
	rm -r "$log_dir"
fi
