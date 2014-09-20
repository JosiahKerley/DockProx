#!/bin/bash

## Setup
docker build -t="etherpad" github.com/arcus-io/docker-etherpad
docker run -d "etherpad"

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
