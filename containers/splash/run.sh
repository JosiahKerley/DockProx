#!/bin/bash
service httpd restart
if [ -f /var/www/html/index.html ]
then
  mv /var/www/html_ /var/www/html
fi
while [ 1 == 1 ]
do
  service httpd status
  sleep 3
done

