#!/usr/bin/env bash

#update package list and upgrade packages
apt-get update

#install git
apt-get install -y git

#install tmux
apt-get install -y tmux

#install python related packages
apt-get install -y python-mysqldb
apt-get install -y python-pip

#install packages from pip
pip install django
pip install south


