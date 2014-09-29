FROM centos:centos6
MAINTAINER Josiah Kerley <josiahkerley@gmail.com>

RUN mkdir -p /var/www/html/
ADD html /var/www/html
ADD run.sh /run.sh
RUN yum install -y httpd

EXPOSE 80 22

ENTRYPOINT ["/bin/bash","/run.sh"]
CMD ["/bin/bash","/run.sh"]

