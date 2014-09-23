#FROM ubuntu:10.04
FROM ubuntu
MAINTAINER josiahkerley@gmail.com

RUN apt-get -y update
RUN mkdir -p /var/www/html/
ADD html /var/www/html
RUN apt-get install -y apache2

EXPOSE 80 22
ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["/usr/sbin/httpd"]
