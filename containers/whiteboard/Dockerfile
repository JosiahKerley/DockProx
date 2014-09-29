#FROM ubuntu:latest
FROM centos:centos6
MAINTAINER Josiah Kerley <josiahkerley@gmail.com>
ADD whiteboard.tar /whiteboard
RUN bash /whiteboard/strap-whiteboard.sh
EXPOSE 8080
ENTRYPOINT ["/bin/bash", "/home/whiteboard/serve.sh"]
