#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Magrathea Storage1 to Disk using Rsync"
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/RsyncTest /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Active_VMs /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Desktop /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Dev /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Docker /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Email /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Temp /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/VMShare /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/.pem /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_OfflineData/.ssh /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/Books /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/Reference /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/Software /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/OnlineCourses /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/ArchivedWork /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GregData/Greg_ServerData/VMs /media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/GeneralShare /media/gregf/Transcend/Storage1/GeneralBackup
rsync -r -v -t --progress -s /media/Storage1/GeneralBackup/Media/Photos /media/gregf/Transcend/Storage1/GeneralBackup/Media
