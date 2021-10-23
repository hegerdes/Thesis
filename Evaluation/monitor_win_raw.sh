#!/bin/bash
counter=0
sleeptime=10
breakAfter=180

while true; do
    if [ $counter -eq $breakAfter ]; then break; fi
    echo "At run ${counter}"
    pwsh -Command Get-Process | sed -e '1,3d' | sed -e '$ d' >> stats_win_raw.csv
    counter=$((counter+1))
    sleep $sleeptime
done

# typeperf "\Prozess(*)\Prozessorzeit (%)" "\Prozess(*)\Virtuelle Größe" "\Prozess(*)\Seitenfehler/s" "\Prozess(*)\Arbeitsseiten" "\Prozess(*)\Private Bytes" "\Prozess(*)\Threadanzahl" "\Prozess(*)\Basispriorität" "\Prozess(*)\Verstrichene Zeit" "\Prozess(*)\Prozesskennung" "\Prozess(*)\Auslagerungsseiten (Bytes)" "\Prozess(*)\Nicht-Auslagerungsseiten (Bytes)" -sc 180 -si 10 -f CSV -o dev_env_raw.csv
