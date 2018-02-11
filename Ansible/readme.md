Installing
----------
$ cd Software
$ git clone git://github.com/ansible/ansible.git --recursive Ansible
$ cd Ansible
$ source ./hacking/env-setup
$ sudo easy_install pip
$ sudo pip install -r ./requirements.txt

$ echo "127.0.0.1" > ~/WorkstationScripts/Ansible/ansible_hosts
$ export ANSIBLE_INVENTORY=~/WorkstationScripts/Ansible/ansible_hosts

Side Note: If you include localhost as a machine in inventory, then Ansible will try to connect to it via ssh
This will require an SSH server on your local machine.
$ sudo apt-get install openssh-server

Now you can test the installation with:
$ ansible -m ping -c local 127.0.0.1
You should get the following back:
127.0.0.1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}


Useful Links
------------
http://docs.ansible.com/ansible/intro_installation.html
