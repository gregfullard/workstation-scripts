#!/bin/bash
# This script should be run as the first step on a fresh Ubuntu OS install.
# It does all the bootstrapping that will allow the rest of the work to be
# handled by Ansible

# Get started
echo This script will set up your machine in the standard way that Greg likes

# Create some base folders in the home directory
if [ -d "~/Software" ]
then
    echo "Directory ~/Software exists already"
else
    echo "Creating directory ~/Software"
    mkdir ~/Software
fi

# Install some base Software
# git
sudo apt-get install git
# openssh server (needed by Ansible to connecto localhost via ssh)
sudo apt-get install openssh-server

# Set up Ansible
cd ~/Software
git clone git://github.com/ansible/ansible.git --recursive Ansible
cd Ansible
source ./hacking/env-setup
sudo easy_install pip
sudo pip install -r ./requirements.txt
echo "127.0.0.1" > ~/WorkstationScripts/Ansible/ansible_hosts
export ANSIBLE_INVENTORY=~/WorkstationScripts/Ansible/ansible_hosts
ansible -m ping -c local 127.0.0.1
