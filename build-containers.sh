#!/bin/bash

## Setup
docker build -t="ejabberd" github.com/rroemhild/docker-ejabberd
docker run -d "ejabberd"

docker build -t="ushahidi" github.com/ushahidi/docker-ushahidi-platform
docker run -d "ushahidi"

docker build -t="limesurvey" github.com/domachine/docker-limesurvey-nginx
docker run -d "limesurvey"

docker build -t="jenkins" github.com/aespinosa/docker-jenkins
docker run -d "jenkins"

docker pull turnkeylinux/bambooinvoice-13.0
docker run -d "bambooinvoice"

docker pull turnkeylinux/observium-13.0
docker run -d "observium"


docker build -t="etherpad" github.com/arcus-io/docker-etherpad
docker run -d "etherpad"

docker build -t="icinga" github.com/Icinga/icinga-docker
docker run -d "icinga"

docker build -t="elgg" github.com/tixel/docker-elgg
docker run -d "elgg"

docker build -t="collabtive" github.com/ChristianKniep/docker-collabtive
docker run -d "collabtive"

docker build -t="icescrum" github.com/grams/docker-icescrum
docker run -d "icescrum"

docker build -t="owncloud" github.com/spiroid/docker-owncloud
docker run -d "owncloud"

docker build -t="gitlab" github.com/sameersbn/docker-gitlab
docker run -d "gitlab"

docker build -t="redmine" github.com/sameersbn/docker-redmine
docker run -d "redmine"

docker build -t="otrs" github.com/tommyblue/docker-otrs
docker run -d "otrs"

docker build -t="moodle" github.com/sergiogomez/docker-moodle
docker run -d "moodle"

docker build -t="dokuwiki" github.com/egguy/docker-php5-nginx-dokuwiki
docker run -d "dokuwiki"

docker build -t="observium" github.com/wbouzane/observium
docker run -d "observium"














## Display
clear
docker images
docker ps
