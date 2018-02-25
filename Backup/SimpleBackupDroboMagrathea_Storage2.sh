#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Drobo to Storage2 on Magrathea using Rsync"
# sudo mount -t cifs //192.168.3.253/public /mnt -o vers=1.0,username=gregf,file_mode=0777,dir_mode=0777
sudo mount /media/Drobo

rsync -r -v -t --progress -s /media/Drobo/Media/TalkShows /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/Comedy /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/Documentaries /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/Podcasts /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/Series /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/HomeVideos /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/AudioBooks /media/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Drobo/Media/Music /media/Storage2/GeneralBackup/Media
