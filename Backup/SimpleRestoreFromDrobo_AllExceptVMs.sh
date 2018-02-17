#!/bin/sh
echo "This is a very simply restore script that will send retrieve a bunch of folders from the drobo using Rsync"
sudo mount -t cifs //192.168.3.253/public /mnt -o username=gregf,file_mode=0777,dir_mode=0777
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/RsyncTest /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Dev /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Docker /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Temp /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Temp_Music /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/VMShare /home/gregf/Greg_OfflineData
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Email /home/gregf/
rsync -r -v --progress -s /mnt/GregData/Greg_OfflineData/Desktop /home/gregf
