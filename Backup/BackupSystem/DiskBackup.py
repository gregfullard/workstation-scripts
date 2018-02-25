# DiskBackup.py
# Author: Greg Fullard
# Date: 2015-04-27
# Simply runs some rsync commands in order. Copying from Magrathea to External disks
#
# TBD

# Notes

import subprocess, datetime, os

#
# Use this  section to mark which folders you want to backup
#
#Storage 1
Greg_OfflineData_Active_VMs = 1
Greg_OfflineData_Temp = 1
Greg_OfflineData_Email = 1
Greg_OfflineData_Dev = 1
Greg_OfflineData_Desktop = 1
Greg_OfflineData_Docker = 1
GregServerData_Books = 1
GregServerData_Reference = 1
GregServerData_Software = 1
GregServerData_OnlineCourses = 1
GregServerData_ArchivedWork = 1
GregServerData_VMs = 1
GeneralShare = 1
Media_Photos = 1

#Storage 2
Media_AudioBooks = 0
Media_Comedy = 0
Media_Documentaries = 0
Media_HomeVideos = 0
Media_Music = 0
Media_Podcasts = 0
Media_Series = 0
Media_TalkShows = 0

#Storage 3
Media_Movies = 0
RosalieData = 0


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 

#
# Create the logging folder
# 
basePath = "/home/gregf/Scripts/Python/BackupSystem/logs/disk/"
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
backupSubFolder("1", "Greg_OfflineData_Active_VMs", Greg_OfflineData_Active_VMs, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Active_VMs", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("2", "Greg_OfflineData_Temp", Greg_OfflineData_Temp, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Temp", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("3", "Greg_OfflineData_Email", Greg_OfflineData_Email, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Email", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("4", "Greg_OfflineData_Dev", Greg_OfflineData_Dev, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Dev", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("5", "Greg_OfflineData_Desktop", Greg_OfflineData_Desktop, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Desktop", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("6", "Greg_OfflineData_Docker", Greg_OfflineData_Docker, "/media/Storage1/GeneralBackup/GregData/Greg_OfflineData/Docker", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_OfflineData")
backupSubFolder("7", "GregServerData_Books", GregServerData_Books, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/Books", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("8", "GregServerData_Reference", GregServerData_Reference, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/Reference", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("9", "GregServerData_Software", GregServerData_Software, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/Software", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("10", "GregServerData_OnlineCourses", GregServerData_OnlineCourses, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/OnlineCourses", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("11", "GregServerData_ArchivedWork", GregServerData_ArchivedWork, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/ArchivedWork", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("12", "GregServerData_VMs", GregServerData_VMs, "/media/Storage1/GeneralBackup/GregData/Greg_ServerData/VMs", "/media/gregf/Transcend/Storage1/GeneralBackup/GregData/Greg_ServerData")
backupSubFolder("13", "GeneralShare", GeneralShare, "/media/Storage1/GeneralBackup/GeneralShare", "/media/gregf/Transcend/Storage1/GeneralBackup")
backupSubFolder("14", "Media_Photos", Media_Photos, "/media/Storage1/GeneralBackup/Media/Photos", "/media/gregf/Transcend/Storage1/GeneralBackup/Media")

#Storage 2
backupSubFolder("15", "Media_TalkShows", Media_TalkShows, "/media/Storage2/GeneralBackup/Media/TalkShows", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("16", "Media_Comedy", Media_Comedy, "/media/Storage2/GeneralBackup/Media/Comedy", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("17", "Media_Documentaries", Media_Documentaries, "/media/Storage2/GeneralBackup/Media/Documentaries", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("18", "Media_Podcasts", Media_Podcasts, "/media/Storage2/GeneralBackup/Media/Podcasts", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("19", "Media_Series", Media_Series, "/media/Storage2/GeneralBackup/Media/Series", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("20", "Media_HomeVideos", Media_HomeVideos, "/media/Storage2/GeneralBackup/Media/HomeVideos", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("21", "Media_AudioBooks", Media_AudioBooks, "/media/Storage2/GeneralBackup/Media/AudioBooks", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")
backupSubFolder("22", "Media_Music", Media_Music, "/media/Storage2/GeneralBackup/Media/Music", "/media/gregf/Transcend/Storage2/GeneralBackup/Media")

#Storage 3
backupSubFolder("23", "Media_Movies", Media_Movies, "/media/Storage3/GeneralBackup/Media/Movies", "/media/gregf/Transcend/Storage3/GeneralBackup/Media")
backupSubFolder("24", "RosalieData", RosalieData, "/media/Storage3/GeneralBackup/RosalieData", "/media/gregf/Transcend/Storage3/GeneralBackup")






