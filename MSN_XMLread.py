#! usr/bin/env python
# -*- coding: UTF-8 -*-

#The code below makes a old MSN register readable in a .txt file
#I guess have something in the internet that do it very well
#But I make this for my self in python
#For fun, for learn and for save a talk between me and my best friend at the High School times
#Enjoy and make changes if you think necessary :)
#Thiago Borges

#need the ElementTree to run
import xml.etree.ElementTree as ET
import io

#class containing the message need structure
#class variables in portuguese to differ from enters
class message:
	def __init__(self,hour,date,sender,recipient,text):
		self.data = date
		self.hora = hour
		self.rem = sender
		self.des = recipient
		self.texto = text

	def __str__(self):
		return u'{self.rem}\n{self.data} / {self.hora}\n\t{self.texto}\n'.format(self=self)

#Function that read the file and call the out function
def read(fileName,outName):
	allMsg = []
	i = 0
	tree = ET.parse(fileName)
	root = tree.getroot()
	
	for mens in root.findall('Message'):
		i = 1
		newMsg = message(mens.get("Time"),mens.get("Date"),excludeHTML(mens.find("From").find("User").get("FriendlyName")),excludeHTML(mens.find("To").find("User").get("FriendlyName")),mens.find("Text").text)
		allMsg.append(newMsg)
	save(allMsg,outName)
		
#Function that generate the out file
def save(list,outName):
	if(len(list) > 0):
		file = io.open(outName,"w",encoding="utf8")
		for l in list:
			file.write(unicode(l))
		file.close()

#The function below erase all HTML tags from names (generated by MSN Plus!)
def excludeHTML(s):
	b = [x for x in s]
	exclude = False
	for c in s:
		if(c=='['):
			exclude = True
		if(exclude == True):
			if(c == ']'):
				exclude = False
			b.remove(c)
	name = "".join(b)
	return name

#Main
if __name__ == "__main__":
	arq = raw_input("Type the name of the out file with the '.xml' extension:")
	out = raw_input("Type the name of the out file with the '.txt' extension:")
	read(arq,out)

		