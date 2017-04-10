#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders to the drobo using Rsync"
sudo mount -t cifs //192.168.3.253/public /mnt -o username=gregf,file_mode=0777,dir_mode=0777
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/Active_VMs /mnt/GregData/Greg_OfflineData



