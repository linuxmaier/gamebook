#!/usr/bin/env bash

#update package list and upgrade packages
apt-get update

#install git
apt-get install -y git

#install tmux
apt-get install -y tmux

#install admin tools
apt-get install -y curl
apt-get install -y vim

#install python related packages
apt-get install -y python-mysqldb
apt-get install -y python-pip

#install packages from pip
pip install django
pip install south

#set up django project as vagrant
mkdir /home/vagrant/devel
/usr/local/bin/django-admin.py startproject devel /home/vagrant/devel
/usr/bin/git clone https://github.com/linuxmaier/gamebook.git /home/vagrant/devel/gamebook
/bin/chmod +x /home/vagrant/devel/manage.py
/bin/chown -R vagrant:vagrant /home/vagrant 


