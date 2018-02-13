# Howzit
Scripts used on my workstation for initial setup, backup, etc.
Strongly influenced by: https://github.com/pbassiner/dev-env

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
* TBD - [wine](https://www.winehq.org/)
* TBD - WineTricks
* TBD - Thunderbird
* TBD - [Dropbox](https://www.dropbox.com/)
* TBD - Printer Driver
* TBD - Scanner Driver
* TBD - Slack
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
* TBD - [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community 2017.3.2)
* TBD - JBDS / Eclipse
* TBD - Eclipse plugin : Sling
* TBD - Eclipse plugin : rest
* TBD - Eclipse plugin : AEM

## Database Developer Tools
* [MySQL Workbench](https://www.mysql.com/products/workbench/)

## Test Developer Tools
* [soapui](https://www.soapui.org/)
* TBD - Chrome Pluging - ARC

## Other utilities
* TBD - Anaconda

## Servers & Containers
* TBD -

# Folders and Data
The following folders are created
* ~/Email
* ~/Greg_OfflineData
* ~/GoogleDrive
* ~/Repos

The following data needs to be synched for a fully operational Environment
* TBD - Email from Drobo Backup
* TBD - Greg_OfflineData from Drobo Backup
* TBD - GoogleDrive folders via InSync
* TBD - Some repos via Git

# Custom configuration
* TBD - Insync folders to sync
* TBD - Thunderbird
* TBD - Drobo shortcut
* TBD - GoogleDrive shortcut
* TBD - VMShare shortcut
* TBD - Repos shortcut
* TBD - VMs ready to open
* TBD - Folder views
* TBD - Launcher size
* TBD - Printer config

# Understanding the project
You will find the following sub-folders in this repo:
 * Root folder contains the bootstrap script. It will get everthing already
 * Backup
  * Contains scripts that I use for backup and retrievals
 * Setup
  * Contains ansible hosts files. One file for each of my "setup domains"
  * Contains a set of Ansible tasks grouped into roles. These are referenced from the playbooks
  * For each setup domain, there is a playbook file which calls the roles that it needs
 * Ansible
  * Not sure if I'll still use this folder
