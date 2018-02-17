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
* TBD - Printer Driver
* TBD - Scanner Driver
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
* TBD - [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community 2017.3.2)
* TBD - JBDS / Eclipse
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
 * java --version to confirm Java 1.8 is Installed
 * git --version
 * maven --version

# Manual steps still needed at the end (Make these less over time)
 * Restore non-VM files (using restore script in this repo)
 * Restore VM files (using restore script in this repo)
 * Configure InSync folder synching
 * Add Drobo shortcut
 * Add Repos shortcut
 * Add GoogleDrive shortcut
 * Add Dropbox shortcut
 * Add VMShare shortcut
 * Configure Thunderbird profile to point to restored files
 * Clone git repos for active development
 * Download and Install JBDS

# Reviewing Manual Steps
 * Start up BasicTools VM. Check files on VMShare can be accessed
 * Generate Sphinx docs for a cloned repo
 * Verify GoogleDrive synching
 * Verify Dropbox synching
