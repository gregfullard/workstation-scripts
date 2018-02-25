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
Greg_OfflineData_Desktop = 1
Greg_OfflineData_Dev = 1
Greg_OfflineData_Docker = 1
Greg_OfflineData_Email = 1
Greg_OfflineData_Temp = 1
Greg_OfflineData_VMShare = 1
Greg_OfflineData_PEM = 1
Greg_OfflineData_SSH = 1
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
backupSubFolder("2", "Greg_OfflineData_Desktop", Greg_OfflineData_Desktop, "/media/Drobo/GregData/Greg_OfflineData/Desktop", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("3", "Greg_OfflineData_Dev", Greg_OfflineData_Dev, "/media/Drobo/GregData/Greg_OfflineData/Dev", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("4", "Greg_OfflineData_Docker", Greg_OfflineData_Docker, "/media/Drobo/GregData/Greg_OfflineData/Docker", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("5", "Greg_OfflineData_Email", Greg_OfflineData_Email, "/media/Drobo/GregData/Greg_OfflineData/Email", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("6", "Greg_OfflineData_Temp", Greg_OfflineData_Temp, "/media/Drobo/GregData/Greg_OfflineData/Temp", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("7", "Greg_OfflineData_VMShare", Greg_OfflineData_VMShare, "/media/Drobo/GregData/Greg_OfflineData/VMShare", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("8", "Greg_OfflineData_PEM", Greg_OfflineData_PEM, "/media/Drobo/GregData/Greg_OfflineData/.pem", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("9", "Greg_OfflineData_SSH", Greg_OfflineData_SSH, "/media/Drobo/GregData/Greg_OfflineData/.ssh", "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("10", "GregServerData_Books", GregServerData_Books, "/media/Drobo/GregData/Greg_ServerData/Books", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("11", "GregServerData_Reference", GregServerData_Reference, "/media/Drobo/GregData/Greg_ServerData/Reference", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("12", "GregServerData_Software", GregServerData_Software, "/media/Drobo/GregData/Greg_ServerData/Software", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("13", "GregServerData_OnlineCourses", GregServerData_OnlineCourses, "/media/Drobo/GregData/Greg_ServerData/OnlineCourses", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("14", "GregServerData_ArchivedWork", GregServerData_ArchivedWork, "/media/Drobo/GregData/Greg_ServerData/ArchivedWork", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("15", "GregServerData_VMs", GregServerData_VMs, "/media/Drobo/GregData/Greg_ServerData/VMs", "/media/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("16", "GeneralShare", GeneralShare, "/media/Drobo/GeneralShare", "/media/Storage1/GeneralBackup")
backupSubFolder("17", "Media_Photos", Media_Photos, "/media/Drobo/Media/Photos", "/media/Storage1/GeneralBackup/Media")

#Storage 2
backupSubFolder("18", "Media_TalkShows", Media_TalkShows, "/media/Drobo/Media/TalkShows", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("19", "Media_Comedy", Media_Comedy, "/media/Drobo/Media/Comedy", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("20", "Media_Documentaries", Media_Documentaries, "/media/Drobo/Media/Documentaries", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("21", "Media_Podcasts", Media_Podcasts, "/media/Drobo/Media/Podcasts", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("22", "Media_Series", Media_Series, "/media/Drobo/Media/Series", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("23", "Media_HomeVideos", Media_HomeVideos, "/media/Drobo/Media/HomeVideos", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("24", "Media_AudioBooks", Media_AudioBooks, "/media/Drobo/Media/AudioBooks", "/media/Storage2/GeneralBackup/Media")
backupSubFolder("25", "Media_Music", Media_Music, "/media/Drobo/Media/Music", "/media/Storage2/GeneralBackup/Media")

#Storage 3
backupSubFolder("26", "Media_Movies", Media_Movies, "/media/Drobo/Media/Movies", "/media/Storage3/GeneralBackup/Media")
backupSubFolder("27", "RosalieData", RosalieData, "/media/Drobo/RosalieData", "/media/Storage3/GeneralBackup")






