# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Generic config

# OS/Box
VAGRANT_BOX = 'ubuntu/bionic64' # 18.04
# VM User — 'vagrant' by default
VM_USER = 'vagrant'


# Master config params
VM_NAME = 'ubuntu-python3-dev'
VM_ADDRESS = '192.168.56.50'
VM_HOSTNAME = "ubuntu-python3-dev.everlab.local"


Vagrant.configure(2) do |config|

  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
  # Configuration definitions for the "Master" kube VM
  config.vm.define "ubuntu-python3-dev" do |ubuntu|
    
    # Configure box type
    ubuntu.vm.box = VAGRANT_BOX
    ubuntu.vm.hostname = VM_HOSTNAME

    # Configure the Network
    ubuntu.vm.network "private_network", ip: VM_ADDRESS

    ubuntu.vm.provider "virtualbox" do |v|
      v.name = VM_NAME
      v.memory = 2048
    end
    
    # Script provisioner for Master
    $script = <<-SCRIPT
    sudo apt-add-repository --yes --update ppa:ansible/ansible
    apt update
    sudo apt install --yes \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    unzip \
    netcat \
    python3-pip \
    python3-venv \
    software-properties-common

    sudo pip3 install virtualenvwrapper

    echo "export WORKON_HOME=$HOME/.virtualenvs" >> /home/vagrant/.bashrc
    echo "export VIRTUALENVWRAPPER_PYTHON=$(which python3)" >> /home/vagrant/.bashrc
    echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '" >> /home/vagrant/.bashrc
    echo "export PROJECT_HOME=$HOME/Devel" >> /home/vagrant/.bashrc
    echo "source $(which virtualenvwrapper.sh)" >> /home/vagrant/.bashrc

    source ~/.bashrc

    SCRIPT
  
    ubuntu.vm.provision "shell", inline: $script
  end
end
 
 
 
