#!/bin/bash
counter=0
sleeptime=10
breakAfter=180

docker compose -f docker-compose.yml -f docker-compose.cu.yml up -d portal-webapp dm-cu-company-api dm-terminals-company-api db
sleep 10

while true; do
    if [ $counter -eq $breakAfter ]; then break; fi
    echo "At run ${counter}"
    docker stats --no-stream --all --format "{{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" cci-portal-webapp-1 cci-dm-cu-company-api-1 cci-dm-terminals-company-api-1 cci-db-1 >> stats_win_docker.txt

    pwsh -Command Get-Process | sed -e '1,3d' | sed -e '$ d' >> stats_win_raw.csv
    sleep $sleeptime
done

# portal-webapp dm-cu-company-api dm-terminals-company-api db

# typeperf "\Prozess(*)\Prozessorzeit (%)" "\Prozess(*)\Virtuelle Größe" "\Prozess(*)\Seitenfehler/s" "\Prozess(*)\Arbeitsseiten" "\Prozess(*)\Private Bytes" "\Prozess(*)\Threadanzahl" "\Prozess(*)\Basispriorität" "\Prozess(*)\Verstrichene Zeit" "\Prozess(*)\Prozesskennung" "\Prozess(*)\Auslagerungsseiten (Bytes)" "\Prozess(*)\Nicht-Auslagerungsseiten (Bytes)" -sc 180 -si 10 -f CSV -o dev_env_docker.csv
