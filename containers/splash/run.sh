#!/bin/bash
service httpd restart
while [ 1 == 1 ]
do
  service httpd status
  sleep 3
done

