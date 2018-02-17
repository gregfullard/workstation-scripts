#!/bin/sh
echo "This is a very simply restore script that will restore a bunch of folders from the drobo using Rsync"
sudo mount -t cifs //192.168.3.253/public /mnt -o vers=1.0,username=gregf,file_mode=0777,dir_mode=0777
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Active_VMs /home/gregf/Greg_OfflineData
