#!/usr/bin/python

import os
import sys
import json
import time
import socket
import fcntl
import struct
import hashlib

class DockProxSplash:

	## Settings
	freq=5
	running=True
	ps = "/tmp/docker-prox-ps.tmp"
	inspect = "/tmp/docker-prox-inspect.tmp"
	configFile = "index.html"

	## Builds the config file
	def build(self):
		buttons = []
	
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
						#print name
						buttons.append('<a class="btn btn-default page-scroll" href="http://{{NAME}}">{{NAME}}</a>'.replace("{{NAME}}",name))
		conf = ""
		for c in config:
			conf += c
			conf += "\n\n\n"
		with open(self.configFile,"w") as f:
			f.write(conf)


	## Monitors for file change
	def monitor(self):
		while self.running:
			self.build()
			time.sleep(self.freq)
	



##- Run as a daemon
d = DockProxSplash()
d.monitor()



