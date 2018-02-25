#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Magrathea Storage2 to Disk using Rsync"
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/TalkShows /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/Comedy /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/Documentaries /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/Podcasts /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/Series /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/HomeVideos /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/AudioBooks /media/gregf/Transcend/Storage2/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage2/GeneralBackup/Media/Music /media/gregf/Transcend/Storage2/GeneralBackup/Media
