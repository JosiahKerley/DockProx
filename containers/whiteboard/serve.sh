#!/bin/bash
clear
ip=`/sbin/ifconfig eth0|grep 'inet addr'|cut -d':' -f2|awk '{print $1}'`
echo ""
echo " Serving from:"
echo "   $ip:8080"
echo ""
echo ""
sleep 3
cd /home/whiteboard
java -jar whiteboard.war
