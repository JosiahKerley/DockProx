#!/bin/bash
rm -rf /var/www/html/*
cp -r ./html/* /var/www/html/
chkconfig httpd on
service httpd restart
