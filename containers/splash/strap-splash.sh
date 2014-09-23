#!/bin/bash
apt-get install -y apache2 || yum install -y httpd
#rm -rf /var/www/html/*
#cp -r ./html/* /var/www/html/
chkconfig httpd on
service httpd restart
