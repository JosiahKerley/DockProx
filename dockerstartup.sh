#!/bin/bash

while read entry
do
	name=`echo $entry | cut -d , -f1`
	data=`echo $entry | cut -d , -f2`
	docker run -d -v $data "$name"
done</etc/dockerstartup-persistant


while read name
do
	docker run -d "$name"
done</etc/dockerstartup
