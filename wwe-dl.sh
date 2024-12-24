#!/bin/sh
# Author : Homer3k
# Description : Download videos from the WWE Network
# Based on WWE-Network-Downloader from freyta (https://github.com/freyta/WWE-Network-Downloader)
# /usr/local/bin/wwedl

lang=""
if [ -z $2 ]
    then
        lang="eng"
    else
        lang=$2
fi

DIR="$(dirname "$(readlink -f "$0")")"
python3 "$DIR/main.py" -f -c -st 00:00:00 -et 12:00:00 -t "$1" -l "$lang"
