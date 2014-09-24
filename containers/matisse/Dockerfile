#FROM ubuntu:latest
FROM turnkeylinux/nodejs-13.0
MAINTAINER Josiah Kerley <josiahkerley@gmail.com>
RUN apt-get update
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-client mysql-server apache2 libapache2-mod-php5 pwgen python-setuptools vim-tiny php5-mysql git
RUN git clone https://github.com/Imaginea/matisse
EXPOSE 80
CMD ["/bin/bash", "/start.sh"]



