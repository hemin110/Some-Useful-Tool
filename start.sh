#!/bin/bash
# Start the dzjz_cls
nohup "python dzjz_cls.py --checkpoint_dir=/checkpoint_cls --net=mobilenet_v2 --max_workers=4 --start_type=rpc" > /tmp/dzjz_cls.log 2>&1 &
ps aux |grep dzjz_cls |grep -q -v grep
PROCESS_1_STATUS=$?
echo "dzjz_cls status..."
echo $PROCESS_1_STATUS
if [ $PROCESS_1_STATUS -ne 0 ]; then
echo "Failed to start my_first_process: $PROCESS_2_STATUS"
exit $PROCESS_1_STATUS
fi
sleep 5
# Start the dzjz_od
nohup "python dzjz_od.py --checkpoint_dir=/checkpoint_od --net=mobilenet_v2 --max_workers=4 --start_type=rpc" > /tmp/dzjz_od.log 2>&1 &
ps aux |grep dzjz_od |grep -q -v grep
PROCESS_2_STATUS=$?
echo "dzjz_od status..."
echo $PROCESS_2_STATUS
if [ $PROCESS_2_STATUS -ne 0 ]; then
echo "Failed to start dzjz_od: $PROCESS_2_STATUS"
exit $PROCESS_2_STATUS
fi
# 每隔60秒检查进程是否运行