#!/bin/bash

## Settings
continue=true
folder=/etc/nginx/ssl
cert=$folder/server.crt
key=$folder/server.key
cert=server.crt
key=server.key
csr=server.csr
pass=`tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1`


## SSL Details
country=
state=
city=
company=
section=
server=
email=
optCompany=


##- Prereqs

## Expect
if [ "`which expect`" == "" ]
then
	yum install -y expect || apt-get install -y expect
else
	if [ "`which expect`" == "" ]
	then
		continue=false
	fi
fi

## OpenSSL
if [ "`which openssl`" == "" ]
then
	yum install -y openssl || apt-get install -y openssl
else
	if [ "`which openssl`" == "" ]
	then
		continue=false
	fi
fi

## Nginx
if [ "`which nginx`" == "" ]
then
	yum install -y nginx || apt-get install -y nginx
else
	if [ "`which nginx`" == "" ]
	then
		continue=false
	fi
fi


##- Setup cert
if [ "$continue" == "true" ]
then
	cwd=$PWD
	mkdir -p "$folder"
	cd "$folder"
	rm -f "$key" "$cert"
	expect -c "spawn openssl genrsa -des3 -out $key 1024
	expect \"Enter pass phrase for\"
	send \"$pass\r\"
	expect \"Verifying\"
	send \"$pass\r\"
	expect EOF"
	expect -c "spawn openssl req -new -key $key -out $csr
	expect \"Enter pass phrase for\"
	send \"$pass\r\"
	expect \"Country\"
	send \"$country\r\"
	expect \"State or Province Name\"
	send \"$state\r\"
	expect \"Locality Name\"
	send \"$city\r\"
	expect \"Organization Name\"
	send \"$company\r\"
	expect \"Organizational Unit Name\"
	send \"$section\r\"
	expect \"Common Name\"
	send \"$server\r\"
	expect \"Email Address\"
	send \"$email\r\"
	expect \"A challenge password\"
	send \"\r\"
	expect \"An optional company name\"
	send \"$optCompany\r\"
	expect EOF"
	cat "$key" > "$key.org"
	expect -c "spawn openssl rsa -in $key.org -out $key
	expect \"Enter pass phrase for\"
	send \"$pass\r\"
	expect EOF"
	openssl x509 -req -days 365 -in $csr -signkey $key -out $cert
	cd "$cwd"
	service nginx on
	chkconfig nginx on
else
	echo "Cannot generate"
fi













































