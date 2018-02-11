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

# What gets Installed
## Dev Tools
* [git](https://git-scm.com/)
* TBD - Password manager
* TBD - JBDS
* TBD - Glogg

## SDKs & Runtimes
* TBD - [maven](https://maven.apache.org/) ![Installed](https://img.shields.io/badge/current\-v3.5.2-blue.svg)
* TBD - [docker](https://www.docker.com/)
* TBD - [docker-compose](https://docs.docker.com/compose/) ![Installed](https://img.shields.io/badge/current\-v1.18.0-blue.svg) [![GitHub release](https://img.shields.io/github/release/docker/compose.svg?label=latest)](https://github.com/docker/compose/releases/latest)
* TBD - [virtualbox](https://www.virtualbox.org/)

## Editors & IDEs
* TBD - Nano
* TBD - Atom
* TBD - Eclipse
* TBD - [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community 2017.3.2)
* TBD - [MySQL Workbench](https://www.mysql.com/products/workbench/)
* TBD - ReText
* TBD - Eclipse plugin : Sling
* TBD - Eclipse plugin : rest
* TBD - Eclipse plugin : AEM

## Other utilities
* TBD - [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* TBD - [Dropbox](https://www.dropbox.com/)
* TBD - Shutter
* TBD - Chrome Pluging - ARC
* TBD - SOAPUI
* TBD - Zoom
* TBD - Thunderbird
* TBD - InSync
* TBD - Kdenlive
* TBD - Anaconda
* TBD - Slack
* TBD - Tex
* TBD - Printer Driver
* TBD - Scanner Driver
* TBD - Vokoscreen
* TBD - Gscan2Pdf

## Servers & Dockers
* TBD -

# Folders and Data
The following folders are created
* TBD - ~/Email
* TBD - ~/Greg_OfflineData
* TBD - ~/GoogleDrive
* TBD - ~/Repos

The following data needs to be synched for a fully operational Environment
* TBD - Email from Drobo Backup
* TBD - Greg_OfflineData from Drobo Backup
* TBD - GoogleDrive folders via InSync
* TBD - Some repos via Git

# Custom configuration
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
 * Ansible
  * Not sure if I'll still use these
 * Backup
  * Contains scripts that I use for backup and retrievals
 * Setup
  * Contains sub folders for each of the setups that I do
  * For each setup, there is a hosts file, along with ansiblie roles and tasks
