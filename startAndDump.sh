IPADRESS=192.168.122.73
NUMOFDUMPS=2

for i in $(seq 1 $NUMOFDUMPS)
do
    echo Starting Dump $i of $NUMOFDUMPS

    echo Generating AutoIt Scripts
    PYTHONPATH='.' python3 ./challenges/picture.py

    echo Starting VM
    virsh snapshot-revert --domain win7 --snapshotname 7_state --running

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
    virsh dump win7 ./$i.dmp --memory-only --verbose
done
echo I am Eve