#!/bin/bash

NUMOFDUMPS=$1
IPADRESS=$2
CHALLENGEPATH=$3
VMDOMAIN="volatileEve"
VMSNAPSHOT="volatileEve"
VMUSER="Eve"

generateDump () {
    i=$1
    echo Starting Dump "$i" of "$NUMOFDUMPS"
	
    # Call the python script that generates all necessary files for this round.
    echo Generating AutoIt Scripts
    PYTHONPATH='.' python3 "$CHALLENGEPATH" || exit 1
    
    # Prepare the output directory.
    # Contents of the "extra" directory are not supposed to end up on the VM.
    mkdir -p ./dumps/"$i"
    chmod 777 ./dumps/"$i"
    mv ./output/extra ./dumps/"$i"
    cp ./output/* ./dumps/"$i"/extra

    # Revert the VM to stable snapshot, then transfer the generated files and reboot.
    # The file main.au3 will then be automatically executed after boot.
    # Destroy is silenced because it will only succeed and is only needed when the VM is running.
    echo Starting VM
    virsh -q destroy "$VMDOMAIN" > /dev/null 2>&1
    virsh snapshot-revert --force --domain "$VMDOMAIN" --snapshotname "$VMSNAPSHOT" --running || exit 1

    echo Transfering Script Files
    scp -r ./output "$VMUSER"@"$IPADRESS":/home/"$VMUSER"
    ssh "$VMUSER"@"$IPADRESS" "chmod -R 777 /home/$VMUSER/output" || exit 1

    echo Rebooting VM
    virsh reboot $VMDOMAIN || exit 1
    # Wait to get past the time window during shutdown, where ssh connections are still accepted. 
    sleep 10s

    # Reconnect to VM and wait for signal file.
    echo Trying to connect to VM with SSH
    RETVAL=1
    while [ $RETVAL -ne 0 ]
    do
        sleep 1s
        ssh -q "$VMUSER"@"$IPADRESS" 'echo VM finished booting'
        RETVAL=$?
    done

    echo 'Waiting for AutoIt script execution'
    ssh "$VMUSER"@"$IPADRESS" "while [[ ! -f /home/$VMUSER/output/signal ]]
    do
        sleep 2
    done"
    
    # If there is an additional script generated by the python script, execute it now.
    if [ -f ./dumps/"$1"/extra/additional.sh ]; then
        (
            echo Executing additional script.
            cd ./dumps/"$1"/extra || exit
            bash ./additional.sh "$IPADRESS" || exit 1
        )
    else
        echo No additional script.
    fi

    # Dump time!
    echo Dumping VM
    virsh suspend "$VMDOMAIN"
    virsh dump "$VMDOMAIN" ./dumps/"$i"/dump.dmp --memory-only --verbose
}

rm -rf ./dumps

for i in $(seq -f "%02g" 1 "$NUMOFDUMPS")
do
    rm -rf ./output
    generateDump "$i"    
done

rm -rf ./output
echo I am Eve
