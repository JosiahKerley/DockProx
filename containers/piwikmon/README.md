# docker-piwik

A nice and easy way to get a Piwik instance up and running using docker. For
help on getting started with docker see the [official getting started guide][0].
For more information on Piwik and check out it's [website][1].


## Building docker-piwik

Running this will build you a docker image with the latest version of both
docker-piwik and Piwik itself.

    docker build -t dz0ny/piwik git://github.com/dz0ny/docker-piwik.git


## Running docker-piwik

Running the first time will setup MySQL to be in your data dir shared with your
host so that you can back it up if you want to. It will also set your port to
a static port of your choice so that you can easily map a proxy to it. If this
is the only thing running on your system you can map the port to 80 and no
proxy is needed. i.e. `-p=80:80` Also be sure your mounted directory on your
host machine is already created before running this `mkdir -p /mnt/piwik`.

    sudo docker run -p=10000:80 -v=/mnt/piwik:/data dz0ny/piwik

Note that the first time you run this it sets up your piwik user and database
as well as locking down your root user. **This will echo out your database
settings for use when setting up Piwik when you connect via HTTP.** Your root
and piwik user passwords are stored in your data dir incase you need them in the
future.

From now on when you start/stop docker-piwik you should use the container id
with the following commands. To get your container id, after you initial run
type `sudo docker ps` and it will show up on the left side followed by the image
name which is `dz0ny/piwik:latest`.

    sudo docker start <container_id>
    sudo docker stop <container_id>

### Notes on the run command

 + `-v` is the volume you are mounting `-v=host_dir:docker_dir`
 + `overshard/piwik` is simply what I called my docker build of this image
 + `-d=true` allows this to run cleanly as a daemon, remove for debugging
 + `-p` is the port it connects to, `-p=host_port:docker_port`


[0]: http://www.docker.io/gettingstarted/
[1]: http://piwik.org/

