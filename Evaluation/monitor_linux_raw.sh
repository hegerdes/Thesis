#!/bin/bash
counter=0
sleeptime=10
breakAfter=180

while true; do
    if [ $counter -eq $breakAfter ]; then break; fi
    echo "At run ${counter}"
    top -b -n1 | sed 1,7d >> stats_linux_raw.csv
    counter=$((counter+1))
    sleep $sleeptime
done
