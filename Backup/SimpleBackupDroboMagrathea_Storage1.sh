#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Drobo to Stage1 on Magrathea using Rsync"
# sudo mount -t cifs //192.168.3.253/public /mnt -o vers=1.0,username=gregf,file_mode=0777,dir_mode=0777
sudo mount /media/Drobo

rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/RsyncTest /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Active_VMs /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Desktop /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Dev /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Docker /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Email /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/Temp /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/VMShare /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/.pem /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_OfflineData/.ssh /media/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/Books /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/Reference /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/Software /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/OnlineCourses /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/ArchivedWork /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GregData/Greg_ServerData/VMs /media/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Drobo/GeneralShare /media/Storage1/GeneralBackup
rsync -r -v -t --progress -s /media/Drobo/Media/Photos /media/Storage1/GeneralBackup/Media
