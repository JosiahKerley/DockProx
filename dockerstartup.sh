#!/bin/bash

while read name
do
	docker run -d "$name"
done</etc/dockerstartup
