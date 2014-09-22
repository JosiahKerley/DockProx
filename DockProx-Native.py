#!/usr/bin/python

import os
import sys
import json
import time
import socket
import fcntl
import struct
import hashlib

class DockProx:

	##- Settings
	iface = "eth0"
	pollFreq = 5
	configFile = "/etc/nginx/conf.d/default.conf"
	ps = "/tmp/docker-ps.tmp"
	inspect = "/tmp/docker-inspect.tmp"
	lastHash = "0"
	running = True
	template = '''
## Clients going to http://{NAME} or https://{NAME} will hit the Docker container {NAME}.
upstream {NAME} {
  server {SERVER};
}
server {
  listen 80;
  server_name {NAME};
  rewrite ^ https://$server_name$request_uri? permanent;
}
server {
  server_name {NAME};
  listen 443 ssl;
  ssl_certificate /etc/nginx/ssl/server.crt;
  ssl_certificate_key /etc/nginx/ssl/server.key; 
  gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
  location / {
    proxy_pass http://{NAME};
  }
}\n\n\n
'''


	##- Methods
	
	## Gets hash of file
	def hashfile(self, file_path):
		if os.path.exists(file_path) == False:
			return None
		md5 = hashlib.md5()
		f = open(file_path)
		for line in f:
			md5.update(line)
		f.close()
		return (str(md5.hexdigest()))

	## Gets ip of iface
	def ipAddr(self,ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
		)[20:24])

	## Builds the config file
	def build(self):
		## Gets ids
		os.system("docker ps -q >%s"%(self.ps))
		with open(self.ps,"r") as f:
			ids_ = f.read().split("\n")
		
		ids_.remove('')
		ids = ids_
		
		## Gets info
		data = []
		for id in ids:
			os.system("docker inspect %s > %s"%(id,self.inspect))
			with open(self.inspect,"r") as f:
				data.append(json.loads(f.read()))
			#os.remove(self.inspect)
			#os.remove(self.ps)		
		hostip = self.ipAddr(self.iface)
		config = []
		for item_ in data:
			for item in item_:
				ports = []
				name = item["Config"]["Image"]
				for i in item["Config"]["ExposedPorts"]:
					ports.append(i.split("/")[0])
					ip = item["NetworkSettings"]["IPAddress"]		
				for port in ports:
					if port == "80":
						tmp = self.template.replace("{INCOMING}","%s:%s"%(hostip,port))
						tmp = tmp.replace("{NAME}",name)
						tmp = tmp.replace("{SERVER}","%s:%s"%(ip,port))
						config.append(tmp)
		conf = ""
		for c in config:
			conf += c
			conf += "\n\n\n"
		with open(self.configFile,"w") as f:
			f.write(conf)

	## Reloads the proxy
	def reload(self):
		os.system("service nginx reload")

	## Monitors for file change
	def monitor(self):
		while self.running:
			self.build()
			#print self.lastHash
			#print self.hashfile(self.configFile)
			if not self.lastHash == self.hashfile(self.configFile):
				#print "Reloading"
				self.reload()
				self.lastHash = self.hashfile(self.configFile)
			time.sleep(self.pollFreq)
	



##- Run as a daemon
d = DockProx()
d.monitor()



