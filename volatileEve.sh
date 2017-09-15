#!/bin/bash

NUMOFDUMPS=$1
IPADRESS=$2
CHALLENGEPATH=$3


for i in $(seq -f "%02g" 1 "$NUMOFDUMPS")
do
    rm -rf ./output
    rm -rf ./dumps

    echo Starting Dump "$i" of "$NUMOFDUMPS"
	
    echo Generating AutoIt Scripts
    PYTHONPATH='.' python3 "$CHALLENGEPATH"
    
    mkdir -p ./dumps/"$i"
    chmod 777 ./dumps/"$i"
    mv ./output/extra ./dumps/"$i"

    echo Starting VM
    virsh snapshot-revert --domain win7 --snapshotname volatileEve --running

    echo Transfering Script Files
    scp -r ./output Eve@"$IPADRESS":/home/Eve
    ssh Eve@"$IPADRESS" 'chmod -R 777 /home/Eve/output'

    echo
    echo Rebooting VM
    virsh reboot win7
    sleep 30s

    echo Trying to connect to VM with SSH

    RETVAL=1
    while [ $RETVAL -ne 0 ]
    do
        sleep 1s
        ssh Eve@"$IPADRESS" 'echo VM finished booting'
        RETVAL=$?
    done

    echo 'Waiting for AutoIt script execution'
    ssh Eve@"$IPADRESS" 'while [[ ! -f /home/Eve/output/signal ]]
    do
        sleep 2
    done'

    echo Dumping VM
    virsh suspend win7
    virsh dump win7 ./dumps/"$i"/dump.dmp --memory-only --verbose
done
echo I am Eve
