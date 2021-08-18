#!/bin/bash

splite="_"
basePath="/home/pc001/e/lcn/stream"

# ip_list.config 需要在文件末尾留一空行
cat ip_list.config |

while read line
do
    ip=$line
    a=$(($a+1))
    date_time=`date "+%Y_%m_%d"`
    SAVE_PATH="$basePath/$a/${date_time}"
    if [ ! -d ${SAVE_PATH} ];then mkdir -p ${SAVE_PATH}; fi
    
    # 录制视频，软件编码，视频码率768kbps，15FPS，1280x720分辨率，持续时间60s
    ffmpeg -i $ip -rtsp_transport http -codec:a libopus -b:a 64k -codec:v libx264 -b:v 768k -r 15 -t 60 -s 1280x720 ${SAVE_PATH}/$a${splite}`date +%Y%m%d-%H%M`.mkv >/dev/null 2>&1 &
done

exit