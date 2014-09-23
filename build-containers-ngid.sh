#!/bin/bash


## Setup
docker build -t="apsd-etherpad.ngid.centurylink.net" github.com/arcus-io/docker-etherpad
docker run -d "apsd-etherpad.ngid.centurylink.net"


## Display
clear
docker images
docker ps
