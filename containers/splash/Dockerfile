FROM centos:centos6
MAINTAINER Josiah Kerley <josiahkerley@gmail.com>

RUN mkdir -p /var/www/html/
RUN mkdir -p /var/www/html_/
ADD html /var/www/html_
ADD run.sh /run.sh
RUN yum install -y httpd
#VOLUME ["/var/www/html"]

EXPOSE 80 22

ENTRYPOINT ["/bin/bash","/run.sh"]
CMD ["/bin/bash","/run.sh"]

