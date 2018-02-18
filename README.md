# Howzit
Scripts used on my workstation for initial setup, backup, etc.
Strongly influenced by: https://github.com/pbassiner/dev-env
Note: This set of scripts and playbooks are developed for Ubuntu ONLY

# Run it
```shell
wget -qO- https://raw.github.com/gregfullard/workstation-scripts/master/bootstrap.sh | bash
```
# Disclaimer
This is just for personal convenience. You're welcome to reuse, but it comes with no guarantees

# What happens
That script will begin the bootstrapping process, which will clone this repo to your local machine
into the home/WorkstationScripts folder and install various applications as defined in then
Ansible playbooks.

# What gets Installed (These categories align with the ansible roles)
## Base tools
* dnsutils
* apt-transport-https
* ca-certificates
* curl
* software-properties-common
* python
* tar
* unzip

## Workstation tools
* [ansible](https://www.ansible.com/)
* [Shutter](http://shutter-project.org/)
* [virtualbox](https://www.virtualbox.org/)
* [vokoscreen](https://github.com/vkohaupt/vokoscreen)
* [gscan2pdf](http://gscan2pdf.sourceforge.net/)
* [kdenlive](https://kdenlive.org/)
* [breeze-icon-theme](https://github.com/KDE/breeze-icons) (Used by kdenlive)
* [vlc](https://www.videolan.org/vlc/index.html) (Used by kdenlive)
* [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* [InSync](https://www.insynchq.com/)
* [zoom](https://zoom.us/)
* [gimp](https://www.gimp.org/)
* [wine](https://www.winehq.org/)
* [winetricks](https://wiki.winehq.org/Winetricks)
* [thunderbird](https://www.mozilla.org/en-US/thunderbird/)
* [cifs-utils](https://wiki.samba.org/index.php/LinuxCIFS_utils)
* [smbclient](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)
* TBD - [slack](https://slack.com)
* TBD - [Dropbox](https://www.dropbox.com/)
* TBD - Password manager

## Dev Tools
* [nano](https://www.nano-editor.org/)
* [git](https://git-scm.com/)
* [glogg](https://glogg.bonnefon.org/)
* [retext](https://github.com/retext-project/retext)
* [atom](https://atom.io/)
* [sphinx](http://www.sphinx-doc.org)
* [texlive-full](https://www.tug.org/texlive/)
* [texmaker](http://www.xm1math.net/texmaker/)
* TBD - [docker](https://www.docker.com/)
* TBD - [docker-compose](https://docs.docker.com/comp* TBD - Vokoscreenose/) ![Installed](https://img.shields.io/badge/current\-v1.18.0-blue.svg) [![GitHub release](https://img.shields.io/github/release/docker/compose.svg?label=latest)](https://github.com/docker/compose/releases/latest)

## Java Dev Tools
* [maven](https://maven.apache.org/)--recv-keys
* [Oracle JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* TBD - [eclipse](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/neonr) - In Progress
* TBD - [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community 2017.3.2)
* TBD - [JBDS]
* TBD - Eclipse plugin : Sling
* TBD - Eclipse plugin : rest
* TBD - Eclipse plugin : AEM

## AEM Dev tools
* TBD - OAKRun
* TBD - Vault

## Database Developer Tools
* [MySQL Workbench](https://www.mysql.com/products/workbench/)

## Test Developer Tools
* [soapui](https://www.soapui.org/)
* [JMeter](http://jmeter.apache.org/)
* TBD - Chrome Pluging - ARC

## Other utilities
* TBD - Anaconda

## Servers & Containers
* TBD - AEM
* TBD - Sling
* TBD - Jenkins
* TBD - WildFly
* TBD - ActiveMQ
* TBD - Karaf
* TBD - ELK
* TBD - ApacheDSStudio
* TBD - Felix
* TBD - JBoss BPM
* TBD - jbpm
* TBD - JBoss EAP
* TBD - JBoss Fuse
* TBD - Minishift
* TBD - OpenShift
* TBD - NodeJS
* TBD - ProM
* TBD - Unomi

# Folders and Data
The following folders are created
* ~/Email
* ~/Greg_OfflineData
* ~/GoogleDrive
* ~/Repos

# Custom configuration
* TBD - Insync folders to sync (Manual)
* TBD - Thunderbird (Manual)
* TBD - Drobo shortcut (Manual)
* TBD - GoogleDrive shortcut (Manual)
* TBD - VMShare shortcut (Manual)
* TBD - Repos shortcut (Manual)
* TBD - Launcher size (Manual)
* TBD - Printer config (Manual)
* TBD - VMs ready to open
* TBD - Folder views

# Understanding the project
You will find the following sub-folders in this repo:
 * Root folder contains the bootstrap script. It will get everthing already
 * Backup
     * Contains scripts that I use for backup and retrievals
 * Setup
     * Contains ansible hosts files. One file for each of my "setup domains"
     * Contains a set of Ansible tasks grouped into roles. These are referenced from the playbooks
     * For each setup domain, there is a playbook file which calls the roles that it needs

# Reviewing when complete
To review whether the configuration was successful, you can do the following at completion
 * Check registered repos - Step 1
  * cat /etc/apt/sources.list
  * You should see the following in the list:
  * TBD
 * Check registered repos - Step 2
  * ls /etc/apt/sources.list.d
  * You should see the following files:
  * ansible*
  * git*
  * google-chrome*
  * insync*
 * Super-key + "atom" to confirm Eclipse is installed
 * Super-key + "eclipse" to confirm Eclipse is installed
 * Super-key + "retext" to confirm Retext is installed
 * Super-key + "glogg" to confirm Glogg is installed
 * Super-key + "chrome" to confirm Chrome is installed
 * Super-key + "virtualbox" to confirm installation
 * Super-key + "vokoscreen" to confirm installation
 * Super-key + "gscan2pdf" to confirm installation
 * Super-key + "kdenlive" to confirm installation
 * Super-key + "vlc" to confirm installation
 * Super-key + "InSync" to confirm installation
 * Super-key + "zoom" to confirm installation
 * Super-key + "gimp" to confirm installation
 * java -version to confirm Java 1.8 is Installed
 * git --version
 * mvn --version
 * TBD - Docker

# Manual steps at the end :: All OSes (Make these less over time)
 * Sign-in to chrome, this will pull through bookmarks etc.
 * Configure InSync folder synching (Select GoogleDriveFolder)
 * Restore non-VM files (sudo ./SimpleRestoreFromDrobo_AllExceptVMs.sh)
 * Restore VM files (sudo ./SimpleRestoreFromDrobo_VMs.sh)
 * Clone BitBucket repos for active development
  * DigitalPlatoon/8BpUtils
  * DigitalPlatoon/C3M_Avocado
  * DigitalPlatoon/DigitalPlatoonDevOpsToolbox
  * DigitalPlatoon/8BitPlatoon_MvnArchetypes
  * DigitalPlatoon/8BitPlatoon_RandomFiles  
 * Configure VMs
  * Open virtualbox
  * Add BasicTools VM (Machine > Add. > ~/Greg_OfflineData/ActiveVMs/Win7Pro_BasicTools/Win7Pro_BasicTools.vbox)
  * Add AnsibleHomeBase VM (Machine > Add. > ~/Greg_OfflineData/ActiveVMs/AnsibleHomeBase/AnsibleHomeBase.vbox)
  * Add LCES4 VM (Machine > Add. > ~/Greg_OfflineData/ActiveVMs/Win7Ult_LCES4/Win7Ult_LCES4.vbox)
  * Add AEM JEE VM (Machine > Add. > ~/Greg_OfflineData/ActiveVMs/Win7Pro_AEMJEE2/Win7Pro_AEMJEE2.vbox)   
 * TBD - Configure Thunderbird profile to point to restored files (NOTE: Only do this for a real run)
 * TBD - Download and Install JBDS
 * TBD - Download and Install Adobe Reader
 * TBD - Download and Install Balsamiq Mockups

# Manual steps at the end :: Ubuntu 16.04 (Make these less over time)
 * Install Printer
  * Plug int printer on USB
  * Download ULD driver at http://www.samsungdrivers.net/samsung-m2070fw-driver/
  * (Also stored at Greg_ServerData/Software/Drivers/Samsung M2070FW Printer Driver)
  * Untar the tar.gz file
  * sudo ./install
  * After successful installation, super-key > Printers
  * Add printer, select Samsung and follow prompts. Print test page
  * Open gscan2pdf. Do a test scan
 * Remove unwanted Nautilus Places
  * https://askubuntu.com/questions/762591/how-to-remove-unwanted-default-bookmarks-in-nautilus
  * sudo nano ~/.config/user-dirs.dirs
  * sudo nano /etc/xdg/user-dirs.defaults
  * Comment out the unwanted lines
 * Remove unwanted Nautilus links in Home holder
  * Open Nautilus home folder
  * Trash Documents
  * Trash Music
  * Trash Pictures
  * Trash Videos
  * Trash Templates
  * Trash Examples
 * Edit Nautilus Bookmarks
  * Open Nautilus window
  * Bookmarks > Bookmarks
  * Delete all but one of the bookmarks you don't want (Can't delete the last one)
  * Rename the last one to Repos and point it to /home/gregf/Repos
  * Browse to ~/Greg_OfflineData, add bookmark (Bookmarks > Bookmark this location)
  * Browse to ~/Greg_OfflineData/VMShare, add bookmark (Bookmarks > Bookmark this location)
  * Browse to ~/GoogleDrive, add bookmark (Bookmarks > Bookmark this location)
  * Connect to Server (192.168.3.253). Open public folder, add bookmark.
  * TBD - Add Dropbox shortcut
 * Resize Launcher (Setting > Appearance > Look)
 * Add View Desktop button to launcher (Setting > Appearance > Behaviour)
 * Enable Workspaces (Setting > Appearance > Behaviour)
 * Lock apps to launcher (Terminal, Chrome, Virtualbox, Atom, Shutter)
 * Unlock Apps from launcher (LibreOffice, Amazon, System Settings)

# Reviewing Manual Steps
 * Start up BasicTools VM. Check files on VMShare can be accessed
 * Start up AEM JEE VM. Check files on VMShare can be accessed
 * Start up AnsibleHomeBase VM. Check files on VMShare can be accessed
 * Start up LCES4 VM. Check files on VMShare can be accessed
 * Generate Sphinx docs for a cloned repo
 * Verify GoogleDrive synching
 * Verify Dropbox synching
