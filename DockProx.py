import os
import sys
import json
import time
import docker


class DockProx:

	## Standard settings
	nginxConfig = "/etc/nginx/conf.d/default.conf"
	nginxTemplate = "/etc/dockprox/nginx.config.template"
	nginxTemplateHeader = "/etc/dockprox/nginx.config-header.template"
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
		name = name.replace(" ","-")
		name = name.replace(":","-")
		name = name.replace("/","-")
		name = name.replace("\\","-")
		name = name[0:63]
		return(name)


	## Parses dict for name keying
	def nameKey2Element(self, container, path):
		element = container
		try:
			for x in path.strip("/").split("/"):
				element = element.get(x)
		except:
			print("Cannot fetch element!")
		return(element)


	## Returns list of running containers
	def runningContainers(self):
		runningContainers = []
		allContainers = self.d.containers(all=True)
		for container in allContainers:
			if "Up" in container["Status"]:
				runningContainers.append(self.d.inspect_container(container))
		return(runningContainers)


	## Makes an educated guess as to what the best port to use is
	def bestPort(self,ports):
		cleanPorts = []
		port = ["80"]
		for i in ports.keys():
			cleanPorts.append(i.split("/"))
		ports = []
		for i in cleanPorts:
			test = str(i[0])
			badPorts = True
			for bad in ["22","21","25","53","161","162"]:
				if test == bad:
					badPorts = False
			if badPorts:
				ports.append(test)
		portOrder = ['80','443','8080','8000','9001','12345']
		for port in ports:
			for test in portOrder:
				if port == test:
					return(port)
		return(port[0])


	## Generates the nginx tmeplate
	def generateTemplate(self,containers):
		try:
			with open(self.nginxTemplateHeader,"r") as f:
				template = f.read()

		except:
			template = ""
		fileContents = ""
		usedNames = []
		nameCounter = 0
		for container in containers:
			try:
				ip = self.nameKey2Element(container,"NetworkSettings/IPAddress")
				ports = self.nameKey2Element(container,"NetworkSettings/Ports")
				port = self.bestPort(ports)
				name = self.safeName(self.nameKey2Element(container,self.nameKey))
				if name in usedNames:
					nameCounter += 1
					name = "%s-%s"%(name,nameCounter)
				with open(self.nginxTemplate,"r") as f:
					tmp = f.read().replace("{NAME}",name).replace("{IP}",ip).replace("{PORT}",port).replace("{CERTPATH}",self.sslCert).replace("{KEYPATH}",self.sslKey).replace("{SERVER}","%s"%(ip))
				template += tmp + "\n"
				usedNames.append(self.safeName(name))
			except:
				print("Cannot create '%s' template!"%(self.safeName(self.safeName(self.nameKey2Element(container,self.nameKey)))))
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
