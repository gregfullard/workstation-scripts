# workstation-scripts
Scripts used on my workstation for initial setup, backup, etc.

After your OS installation is complete, run this command:
wget -qO- https://raw.github.com/gregfullard/workstation-scripts/master/bootstrap.sh | bash

That script will begin the bootstrapping process, which will clone this repo to your local machine
into the home/WorkstationScripts folder and install various applications as defined in then
Ansible playbooks.

You will find the following sub-folders in this repo:
 * Ansible
  * Contains Ansible playbooks for various things I might want to do on the machine
 * Backup
  * Contains scripts that I use for backup and retrievals
 * Setup
  * Contains bash scripts for initial setup of the machine
