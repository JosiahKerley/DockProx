#!/bin/bash


## Setup
docker build -t="apsd-etherpad.ngid.centurylink.net" github.com/arcus-io/docker-etherpad
docker run -d "apsd-etherpad.ngid.centurylink.net"
mkdir -p /media/docker/etherpad/
chown -R docker /media/docker

docker build -t="apsd-collab00.ngid.centurylink.net" ./containers/docker-lampstack
docker run -d --no-cache=true "apsd-collab00.ngid.centurylink.net"

docker build -t="apsd-whiteboard.ngid.centurylink.net" ./containers/whiteboard
docker run -d "apsd-whiteboard.ngid.centurylink.net"

docker build -t="apsd-meeting.ngid.centurylink.net" ./containers/bigbluebutton
docker run -d "apsd-meeting.ngid.centurylink.net"


## Display
clear
docker images
docker ps
