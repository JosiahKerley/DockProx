#!/bin/bash


## Setup
rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum update -y
yum install -y docker-io python-pip
service docker start
chkconfig docker on
pip install docker-py
bash nginx-ssl-setup.sh
#bash build-containers.sh &

mkdir -p /etc/dockprox
cp ./*.template /etc/dockprox/

bash build-containers-ngid.sh &
#python DockProx.py &

cat DockProx.py > /usr/bin/dockprox
chmod +x /usr/bin/dockprox

cat dockprox.init > /etc/init.d/dockprox
chmod +x /etc/init.d/dockprox
