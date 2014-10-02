#FROM base
FROM ubuntu
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget gzip git-core curl python libssl-dev pkg-config build-essential supervisor
RUN (cd /tmp && wget http://nodejs.org/dist/v0.10.12/node-v0.10.12.tar.gz -O nodejs.tar.gz && tar zxf nodejs.tar.gz && cd node-* && ./configure && make install && rm -rf /tmp/node*)
RUN (cd /opt && git clone git://github.com/ether/etherpad-lite.git etherpad)
RUN (cd /opt/etherpad && ./bin/installDeps.sh)
ADD settings.json /opt/etherpad/settings.json
ADD supervisor.conf /etc/supervisor/supervisor.conf
#RUN touch /opt/etherpad/var/dirty.db

EXPOSE 9001
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf", "-n"]
