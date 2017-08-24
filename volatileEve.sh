#!/bin/bash

NUMOFDUMPS=$1
IPADRESS=$2
CHALLENGEPATH=$3


for i in $(seq -f "%05g" 1 $NUMOFDUMPS)
do
    echo Starting Dump $i of $NUMOFDUMPS

	mkdir -p ./dumps/$i
	mv ./output/extra ./dump/$i
	
    echo Generating AutoIt Scripts
    PYTHONPATH='.' python3 $CHALLENGEPATH

    echo Starting VM
    virsh snapshot-revert --domain win7 --snapshotname volatileEve --running

    echo Transfering Script Files
    scp -r ./output Eve@$IPADRESS:/home/Eve
    ssh Eve@$IPADRESS 'chmod -R 777 /home/Eve/output'

    echo
    echo Rebooting VM
    virsh reboot win7
    sleep 5s

    echo Trying to connect to VM with SSH
    ((COUNT = 100))
    while [[ $COUNT -ne 0 ]] ; do
        ssh Eve@$IPADRESS 'echo VM finished booting'
        rc=$?
        if [[ $rc -eq 0 ]] ; then
            ((COUNT = 1))
        fi
        ((COUNT = COUNT - 1))
    done

    echo Waiting for AutoIt script execution
    ssh Eve@$IPADRESS 'while [ ! -f /home/Eve/output/signal ]
    do
    sleep 2
    done'

    echo Dumping VM
    virsh suspend win7
    virsh dump win7 ./dumps/$i/dump.dmp --memory-only --verbose
done
echo I am Eve