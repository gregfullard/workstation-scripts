#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders to the drobo using Rsync"
sudo mount -t cifs //192.168.3.253/public /mnt -o vers=1.0,username=gregf,file_mode=0777,dir_mode=0777
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/RsyncTest /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/Dev /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/Docker /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/Temp /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/Temp_Music /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Greg_OfflineData/VMShare /mnt/GregData/Greg_OfflineData
rsync -r -v --progress -s /home/gregf/Email /mnt/GregData/Greg_OfflineData/
rsync -r -v --progress -s /home/gregf/Desktop /mnt/GregData/Greg_OfflineData/
