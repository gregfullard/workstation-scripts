# GeneralBackp.py
# Author: Greg Fullard
# Date: 2015-04-27
# Simply runs some rsync commands in order. Copying from the Drobo to Magrathea
#
# TBD
# - Progress % in main terminal
# - store err logs as a file too
# - move the list of folders to backup into a config file
# - Add global log, that will output the start and end time for each run, including which were skipped

# Notes
# - Configuring Drobo SMB mount point
#	- https://help.ubuntu.com/community/Samba/SambaClientGuide
#	- Configured at /media/Drobo (NO AUTO MOUNT)
#	- sudo mount /media/Drobo, or sudo umount /media/Drobo

import subprocess, datetime, os

#
# Use this  section to mark which folders you want to backup
#
Media_AudioBooks = 1
Media_Comedy = 1
Media_Documentaries = 1
Media_HomeVideos = 1
Media_Movies = 1
Media_Music = 1
Media_Photos = 1
Media_Podcasts = 1
Media_Series = 1
Media_TalkShows = 1
Greg_OfflineData_Active_VMs = 1
Greg_OfflineData_Temp = 1
Greg_OfflineData_Email = 1
Greg_OfflineData_Dev = 1
GregServerData_Books = 1
GregServerData_Reference = 1
GregServerData_Software = 1
GregServerData_OnlineCourses = 1
GregServerData_ArchivedWork = 1
GregServerData_VMs = 1
GeneralShare = 1
RosalieData = 1


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 

#
# Create the logging folder
# 
basePath = "/home/gregf/Scripts/Python/BackupSystem/logs/"
logPath = basePath + timestamp + "/"
if not os.path.exists(logPath):
    os.makedirs(logPath)

#
# Defining the reusable function
#
def backupSubFolder(num ,subName, runFlag, source, dest):    
	if runFlag == 1:
		fileName = logPath + num + "_BackupLog_" + subName + "_" + timestamp + ".txt"
		logfile = open(fileName, "w")
		p = subprocess.Popen(["rsync", "-r", "-t", "-v", "--progress", "-s", source, dest], stdout=logfile)
		print "***********************************************"
		print "*** Folder Backup Starting"
		print "*** Number:", num
		print "*** Sub Job Name:", subName
		print "*** Source Folder:", source
		print "*** Logging to: ", fileName
		err = p.communicate()
		print "*** Folder Backup Complete: ", subName
		print "***********************************************\n"
		logfile.close()
	else:
		print "***********************************************"
		print "*** Skipping", subName
		print "***********************************************\n"

#
# Now calling the function for each folder in turn
#
#Storage1
backupSubFolder("1", "Greg_OfflineData_Active_VMs", Greg_OfflineData_Active_VMs, "/media/Drobo/GregData/Greg_OfflineData/Active_VMs", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("2", "Greg_OfflineData_Temp", Greg_OfflineData_Temp, "/media/Drobo/GregData/Greg_OfflineData/Temp", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("3", "Greg_OfflineData_Email", Greg_OfflineData_Email, "/media/Drobo/GregData/Greg_OfflineData/Email", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("4", "Greg_OfflineData_Dev", Greg_OfflineData_Dev, "/media/Drobo/GregData/Greg_OfflineData/Dev", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("5", "GregServerData_Books", GregServerData_Books, "/media/Drobo/GregData/Greg_ServerData/Books", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("6", "GregServerData_Reference", GregServerData_Reference, "/media/Drobo/GregData/Greg_ServerData/Reference", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("7", "GregServerData_Software", GregServerData_Software, "/media/Drobo/GregData/Greg_ServerData/Software", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("8", "GregServerData_OnlineCourses", GregServerData_OnlineCourses, "/media/Drobo/GregData/Greg_ServerData/OnlineCourses", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("9", "GregServerData_ArchivedWork", GregServerData_ArchivedWork, "/media/Drobo/GregData/Greg_ServerData/ArchivedWork", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("10", "GregServerData_VMs", GregServerData_VMs, "/media/Drobo/GregData/Greg_ServerData/VMs", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("11", "GeneralShare", GeneralShare, "/media/Drobo/GeneralShare", "/media/Storage1/GeneralBackup")
backupSubFolder("12", "Media_Photos", Media_Photos, "/media/Drobo/Media/Photos", "/media/Storage1/GeneralBackup/Media")

#Storage 2
backupSubFolder("13", "Media_TalkShows", Media_TalkShows, "/media/Drobo/Media/TalkShows", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("14", "Media_Comedy", Media_Comedy, "/media/Drobo/Media/Comedy", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("15", "Media_Documentaries", Media_Documentaries, "/media/Drobo/Media/Documentaries", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("16", "Media_Podcasts", Media_Podcasts, "/media/Drobo/Media/Podcasts", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("17", "Media_Series", Media_Series, "/media/Drobo/Media/Series", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("18", "Media_HomeVideos", Media_HomeVideos, "/media/Drobo/Media/HomeVideos", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("19", "Media_AudioBooks", Media_AudioBooks, "/media/Drobo/Media/AudioBooks", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("20", "Media_Music", Media_Music, "/media/Drobo/Media/Music", "/media/Storage2/GeneralBackup/Media")

#Storage 3
backupSubFolder("21", "Media_Movies", Media_Movies, "/media/Drobo/Media/Movies", "/media/Storage3/GeneralBackup/Media")
backupSubFolder("22", "RosalieData", RosalieData, "/media/Drobo/RosalieData", "/media/Storage3/GeneralBackup")






