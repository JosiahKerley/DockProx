#!/bin/bash


## Setup
yum install -y docker
bash nginx-ssl-setup.sh
bash build-containers.sh
python DockProx.py &