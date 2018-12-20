# Howzit
Scripts used on my workstation for initial setup, backup, etc.
Strongly influenced by: https://github.com/pbassiner/dev-env
Note: This set of scripts and playbooks are developed for Ubuntu ONLY
Also Note: I'm still having issues running the installation of Wine on 17.10, so I'm only installing Wine on 16.04
Currently using for 18.04.1

# Prerequisite
This script will connect to your github account using SSH. So you will first need to manually copy your ssh keys
into the ~/.ssh folder. Additionally, make sure that the key files are given apprpriate permissions with
* chmod 600 id_rsa
* chmod 600 id_rsa.pub

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
* python3
* python3-pip
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
* [keepassx](https://www.keepassx.org/)
* [onedrive](https://launchpad.net/ubuntu/bionic/+package/onedrive)
* [xdotool](http://manpages.ubuntu.com/manpages/bionic/man1/xdotool.1.html)
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
* [vagrant](https://www.vagrantup.com/)
* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose)

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
* TBD - [JMeter](http://jmeter.apache.org/)
* TBD - Chrome Pluging - ARC
* TBD - Postman

## Python Developer tools
* TBD - Anaconda
* TBD - Pandas
* TBD - Jupyter Notebook

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
* ~/OneDrive
* ~/Repos
* ~/Software

# Custom configuration
* TBD - Insync folders to sync (Manual)
* TBD - Thunderbird (Manual)
* TBD - Drobo shortcut (Manual)
* TBD - GoogleDrive shortcut (Manual)
* TBD - VMShare shortcut (Manual)
* TBD - Repos shortcut (Manual)
* TBD - Launcher size (Manual)
* TBD - Printer config (Manual)
* TBD - VMs ready to open (Manual)
* TBD - Folder views (Manual)

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
 * Super-key + "atom" to confirm Atom is installed
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
 * java -version to confirm Java 1.8 Runtime is Installed
 * java -version to confirm Java 1.8 SDK is Installed
 * git --version to confirm Git is installed
 * mvn --version to confirm Maven is installed
 * docker --version to confirm Docker is installed
 * docker-compose --version to confirm Docker Compose is installed

# Manual steps at the end :: All OSes (Make these less over time)
 * Sign-in to chrome, this will pull through bookmarks etc.
 * Configure InSync folder synching (Select GoogleDriveFolder)
 * Restore non-VM files (sudo ./SimpleRestoreFromDrobo_AllExceptVMs.sh)
 * Restore VM files (sudo ./SimpleRestoreFromDrobo_VMs.sh)
 * Clone BitBucket repos for active development
     * Digital/8BpUtils
     * Digital/C3M_Avocado
     * Digital/DigitalPlatoonDevOpsToolbox
     * Digital/8BitPlatoon_MvnArchetypes
     * Digital/8BitPlatoon_RandomFiles
     * And any other repos of projects you're currently working on
 * Configure Git Global .gitignore
 * Install Maven Archetypes
 * Configure VMs
     * Open virtualbox
     * Add BasicTools VM (Machine > Add. > ~/Greg_OfflineData/ActiveVMs/Win7Pro_BasicTools/Win7Pro_BasicTools.vbox)
 * Configure Thunderbird profile to point to restored files (NOTE: Only do this for a real run)
     * Start thunderbird once, this will create a folder ~/.thunderbird
     * Close it immediately
     * Now edit the file ~/.thunderbird/profiles.ini
     * Content should be:

        ```    
        [General]
        StartWithLastProfile=1

        [Profile0]
        Name=default
        IsRelative=0
        Path=/home/gregf/Email/Thunderbird/Profiles/Thunderbird.default
        Default=1
        ```

     * Now you can open Thunderbird again and all accounts will be ready for you to download
 * Download and Install JBDS
     * Download the latest JBoss Developer Studio install
     * Run the installer
     * Once installed, start up JBDS and select one of the clones Repos as your default Workspace
 * Configure JBDS Update Sites
     * Add the following update sites to JBDS (Help > Install new Software > Add...:
     * Adobe Dev Tools, https://eclipse.adobe.com/aem/dev-tools/
     * RestEditor, http://resteditor.sourceforge.net/eclipse/
 * Download and Install Adobe Reader
     * TODO
 * Download and Install Balsamiq Mockups
     * TODO
     * https://support.balsamiq.com/installation/linux/
 * Download and Install Apache Directory Studio
     * Download from a suitable Apache Mirror (Be sure to grab the Studio download, not the ApacheDS one)
     * Extract to ~/Software/ApacheDirectoryStudio
 * Download and Install AEM
     * Drop AEM Quickstart JAR and Licence file at ~/Software/<YourChosenName>/author
     * Open terminal
     * Run java -jar aem-author-6.3.0-p4502.jar -nointeractive -gui
     * Once AEM starts up, log in with admin:admin
     * Open Package Share
     * Install all the available service packs
     * Stop AEM
     * Create an aemstart.sh shell script with the following content:

        ```       
        #!/bin/bash
        echo "Starting up AEM 6.3"
        crx-quickstart/bin/start
        ```

     * Create an aemstop.sh shell script with the following content:

        ```
        #!/bin/bash
        echo "Stopping AEM 6.3"
        crx-quickstart/bin/stop
        ```

     * chmod 755 both files, to ensure they are executable
     * Start up AEM using the start script
     * Open Package Share
     * Find the latest Forms package for Linux. Download and install it. (Search for "AEM-FORMS-6.3")
     * The forms install will cause a BouncyCastle error
     * Stop your AEM instance
     * Open your file system (not CRX) and edit the sling.properties file under the quickstart/conf folder

        ```
        sling.bootdelegation.class.com.rsa.jsafe.provider.JsafeJCE=com.rsa.*
        sling.bootdelegation.class.org.bouncycastle.jce.provider.BouncyCastleProvider= org.bouncycastle.*
        ```

     * Restart AEM
 * Download and Install Sling
     * Download the latest sling jar from https://sling.apache.org
     * Drop the jar at ~/Software/Sling/<Your_Downloaded_Version>
     * Start it up with java -jar <your_jar_name>
 * TBD - OneDrive client
     * http://skilion.github.io/onedrive/
     * https://medium.com/@glmdev/onedrive-sync-for-linux-ubuntu-2bcbf6777ee4
     * https://www.modmy.com/how-sync-onedrive-linux

# Manual steps at the end :: Ubuntu 16.04 (Make these less over time)
 * Double-check PDF generation from Sphinx
 * Install Printer
     * Plug in printer on USB
     * Download ULD driver at http://www.samsungdrivers.net/samsung-m2070fw-driver/
     * (Also stored at Greg_ServerData/Software/Drivers/Samsung M2070FW Printer Driver)
     * Untar the tar.gz file
     * sudo ./install
     * After successful installation, super-key > Printers
     * Add printer, select Samsung and follow prompts. Print test page
     * Open gscan2pdf. Do a test scan
 * Remove unwanted Nautilus Places
     * https://askubuntu.com/questions/762591/how-to-remove-unwanted-default-bookmarks-in-nautilus

        ```
        sudo nano ~/.config/user-dirs.dirs
        sudo nano /etc/xdg/user-dirs.defaults
        ```

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
 * TBD - Folder views (Set to list view as default)

# Manual steps at the end :: Ubuntu 18.04 (Make these less over time)
 * Double-check PDF generation from Sphinx
    * TODO
 * Install Printer
    * TODO
 * Remove unwanted Nautilus Places
    * TODO
 * Remove unwanted Nautilus links in Home holder
    * TODO   
 * Edit Nautilus Bookmarks  
    * TODO  
 * Resize Launcher (super key > dock)
 * Add View Desktop button to dock
    * gedit ~/.local/share/applications/show-desktop.desktop

        ```
        [Desktop Entry]
        Type=Application
        Name=Show Desktop
        Icon=desktop
        Exec=xdotool key --clearmodifiers Super+d
        ```

    * Super Key "Desktop" > Add to Favourites
 * Lock apps to dock (Terminal, Chrome, Virtualbox, Atom, Shutter)  
 * Unlock apps from dock (LibreOffice, Amazon, System Settings)  
 * Folder views (Set to list view as default)  
    * TODO

# Reviewing Manual Steps
 * Start up BasicTools VM. Check files on VMShare can be accessed
 * Generate Sphinx docs for a cloned repo
 * Verify GoogleDrive synching
 * Verify Dropbox synching
