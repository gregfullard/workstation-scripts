#!/bin/sh
echo "This is a very simply backup script that will send a bunch of folders from Magrathea Storage3 to Disk using Rsync"
rsync -r -v -t --progress -s /media/Storage3/GeneralBackup/Media/Movies /media/gregf/Transcend/Storage3/GeneralBackup/Media
rsync -r -v -t --progress -s /media/Storage3/GeneralBackup/RosalieData /media/gregf/Transcend/Storage3/GeneralBackup
