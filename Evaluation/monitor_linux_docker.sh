#!/bin/bash
counter=0
sleeptime=10
breakAfter=180

docker-compose -f docker-compose.yml -f docker-compose.cu.yml up -d portal-webapp dm-cu-company-api dm-terminals-company-api db
sleep 10

while true; do
    if [ $counter -eq $breakAfter ]; then break; fi
    echo "At run ${counter}"
    docker stats --no-stream --all --format "{{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" cci_new_portal-webapp_1 cci_new_dm-cu-company-api_1 cci_new_dm-terminals-company-api_1 cci_new_db_1 >> stats_linux_docker.txt
    top -b -n1 | sed 1,7d >> stats_linux_docker.csv

    counter=$((counter+1))
    sleep $sleeptime
done
