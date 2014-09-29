#FROM ubuntu:10.04
#FROM ubuntu
FROM centos:centos6
MAINTAINER josiahkerley@gmail.com

#RUN apt-get -y update
#RUN mkdir -p /var/www/html/
#ADD html /var/www/html
#RUN apt-get install -y apache2

RUN mkdir -p /var/www/html/
ADD html /var/www/html
ADD run.sh /run.sh
RUN yum install -y httpd

EXPOSE 80 22
#CMD ["/bin/bash"]
#ENTRYPOINT ["/bin/bash"]

#ENTRYPOINT ["/etc/init.d/apache2","start"]
ENTRYPOINT ["/bin/bash","/run.sh"]
CMD ["/bin/bash","/run.sh"]

