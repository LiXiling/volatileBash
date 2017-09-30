#!/bin/bash

virsh define volatileEve-domain.xml
virsh snapshot-create --redefine volatileEve volatileEve-snapshot.xml


