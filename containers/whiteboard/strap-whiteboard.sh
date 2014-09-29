#!/bin/bash
rtd=$PWD
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"
yum install -y java-1.6.0-openjdk
useradd --create-home whiteboard
clear
echo Copying war file...
cat whiteboard-long-polling.war > /home/whiteboard/whiteboard.war
#cat whiteboard-streaming.war > /home/whiteboard/whiteboard.war
sleep 3
cat serve.sh > /home/whiteboard/serve.sh
cat whiteboard.init > /etc/init.d/whiteboard
chmod +x /etc/init.d/whiteboard
chkconfig whiteboard on
service whiteboard start &
cd "$rtd"
#rm -rf "$DIR"
