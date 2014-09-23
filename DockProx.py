import os
import sys
import json
import time
import docker


class DockProx:

	## Standard settings
	nginxConfig = "/etc/nginx/conf.d/default.conf"
	nginxTemplate = "nginx.config.template"
	sslCert = "/etc/nginx/ssl/server.crt"
	sslKey = "/etc/nginx/ssl/server.key"
	nameKey = "Config/Image"
	nginxReloadCommand = "service nginx reload"

	## Daemon Settings
	running = True
	pollFreq = 5


	## Pre-flight check
	def flightCheck(self):
		greenLight = True
		pile = ""
		for i in self.nginxConfig.split("/"):
			pile += "%s/"%(i)
			test = pile.rstrip("/")
			if os.path.exists(test) or test == "":
				greenLight = True
			else:
				print("Path %s does not exist!"%(test))
				greenLight = False
				exit()


	## Startup method
	def __init__(self):
		print("Starting...")
		self.flightCheck()
		self.d = docker.Client(base_url='unix://var/run/docker.sock')


	## Created a json string from dict
	def dump(self,data):
		data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
		return(data)

	## Returns a safe name for use as hostname
	def safeName(self,name):
		name = name.replace(":","-")
		name = name.replace("/","-")
		name = name.replace("\\","-")
		return(name)


	## Parses dict for name keying
	def nameKey2Element(self, container, path):
		element = container
		try:
			for x in path.strip("/").split("/"):
				element = element.get(x)
		except:
			pass
		return(element)


	## Returns list of running containers
	def runningContainers(self):
		runningContainers = []
		allContainers = self.d.containers(all=True)
		for container in allContainers:
			if "Up" in container["Status"]:
				runningContainers.append(self.d.inspect_container(container))
		return(runningContainers)


	## Generates the nginx tmeplate
	def generateTemplate(self,containers):
		template = ""
		fileContents = ""
		usedNames = []
		nameCounter = 0
		for container in containers:
			try:
				ip = self.nameKey2Element(container,"NetworkSettings/IPAddress")
				name = self.nameKey2Element(container,self.nameKey)
				if name in usedNames:
					nameCounter += 1
					name = "%s-%s"%(name,nameCounter)
				with open(self.nginxTemplate,"r") as f:
					tmp = f.read().replace("{NAME}",self.safeName(name)).replace("{IP}",ip).replace("{CERTPATH}",self.sslCert).replace("{KEYPATH}",self.sslKey).replace("{SERVER}","%s:%s"%(ip,"80"))
				template += tmp + "\n"
				usedNames.append(self.safeName(name))
			except:
				print("Cannot create '%s' template!"%(self.safeName(name)))
		return(template)


	## Checks to see if the config has changed
	def templateUpdated(self,template):
		with open(self.nginxConfig,"r") as f:
			current = f.read()
		if current == template:
			return(False)
		else:
			return(True)

	## Writes the template to the config file
	def writeConfig(self,template):
		with open(self.nginxConfig,"w") as f:
			f.write(template)
		os.system(self.nginxReloadCommand)


	## Runs and periodically checks for changes
	def daemon(self):
		while self.running:
			template = self.generateTemplate(self.runningContainers())
			if self.templateUpdated(template):
				self.writeConfig(template)
			time.sleep(self.pollFreq)


D = DockProx()
D.daemon()
#print D.generateTemplate(D.runningContainers())
#print D.nameKey2Element(D.runningContainers()[0],D.nameKey)
#print D.dump(D.runningContainers())
