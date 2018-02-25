#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Drobo to Storage2 on Magrathea using Rsync"
# sudo mount -t cifs //192.168.3.253/public /mnt -o vers=1.0,username=gregf,file_mode=0777,dir_mode=0777
sudo mount /media/Drobo
rsync -r -v -t --progress -s /media/Drobo/Media/Movies /media/Storage3/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/RosalieData /media/Storage3/GeneralBackup/Media

