#!/bin/bash


##- Setup

## Etherpad
name=apsd-etherpad.ngid.centurylink.net
startup=/etc/dockerstartup-persistant
share=/media/docker/etherpad/var
docker build -t="$name" --no-cache github.com/arcus-io/docker-etherpad
mkdir -p "$share"
if ! grep -qe "$name" "$startup" ; then echo "$name,$share:/opt/etherpad/var" >> "$startup"


## Splash
name=apsd-collab00.ngid.centurylink.net
startup=/etc/dockerstartup-persistant
share=/media/docker/splash/html
docker build -t="$name" --no-cache ./containers/docker-lampstack
mkdir -p "$share"
if ! grep -qe "$name" "$startup" ; then echo "$name,$share:/var/www/html" >> "$startup"


## Whiteboard
name=apsd-whiteboard.ngid.centurylink.net
startup=/etc/dockerstartup
docker build -t="$name" --no-cache ./containers/whiteboard
docker run -d "$name"


## Meeting
#docker build -t="apsd-meeting.ngid.centurylink.net" ./containers/bigbluebutton



## Display
clear
docker images
docker ps
