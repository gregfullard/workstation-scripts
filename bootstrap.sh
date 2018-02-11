#!/bin/bash
# This script should be run as the first step on a fresh Ubuntu OS install.
# It does all the bootstrapping that will allow the rest of the work to be
# handled by Ansible

# Get started
echo '****************'
echo '**************** This script will set up your machine in the standard way that Greg likes'
echo '****************'

# Add all repos needed for bootstrapping
echo '****************'
echo '**************** Ensure Repositories are available'
sudo apt-add-repository ppa:ansible/ansible
sudo apt-add-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get -y upgrade

# Install git
echo '****************'
echo '**************** Install Git'
sudo apt-get -y install git

# Clone the workstation scripts folder
echo '****************'
echo '**************** Clone the workstation scripts folder'
homefolder=~
if [ -d "$homefolder/WorkstationScripts" ]
then
    echo 'Directory '$homefolder'/WorkstationScripts exists already. We will back it up and create a new one from git'
    now=$(date +"%Y%m%d_%H%M%S")
    cp -r ./WorkstationScripts ./zzzWorkstationScripts_$now
    echo 'Existing '$homefolder'/WorkstationScripts folder backed up to'./zzzWorkstationScripts_$now
    sudo rm ./WorkstationScripts -R
fi
git clone https://github.com/gregfullard/workstation-scripts.git WorkstationScripts

# Install Ansible
echo '****************'
echo '**************** Install Ansible'
sudo apt-get -y install ansible

# openssh server (needed by Ansible to connecto localhost via ssh)
echo '****************'
echo '**************** Install OpenSSH server'
sudo apt-get -y install openssh-server

echo '****************'
echo '**************** Done'
echo '****************'



# Create some base folders in the home directory
#if [ -d "~/Software" ]
#then
#    echo "Directory ~/Software exists already"
#else
#    echo "Creating directory ~/Software"
#    mkdir ~/Software
#fi

# TBD - Now time to run the ansible playbook



# Set up Ansible
#cd ~/Software
#git clone git://github.com/ansible/ansible.git --recursive Ansible
#cd Ansible
#source ./hacking/env-setup
#sudo easy_install pip
#sudo pip install -r ./requirements.txt
#echo "127.0.0.1" > ~/WorkstationScripts/Ansible/ansible_hosts
#export ANSIBLE_INVENTORY=~/WorkstationScripts/Ansible/ansible_hosts
#ansible -m ping -c local 127.0.0.1
