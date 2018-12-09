# VERSION: 20181208a
# By boot1110001. Based on the script of Josh Schreuder (2011)

import os #for home dir syntax
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import datetime

os.path.expanduser('~') #to get the home user

now=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") #time wehe this script is executed in format YYYY-mm-dd-HH-MM-SS

#CLASES
class BgImg:
	def __init__(self, name, url, loc_dir, now):
		self.name = name
		self.url = url
		patron = re.compile('\.jpg|\.png')
		matcher = patron.findall(url)
		self.ext = matcher[0]
		self.loc = loc_dir+'/'+now+'-'+name+matcher[0]

	def to_string(self):
		print("My name is: "+self.name)
		print("My URL is: "+self.url)
		print("My localization is: "+self.loc)
		print("My extension is: "+self.ext)

# FUNCTIONS
def get_page1():
	print("Downloading the page to find the image...")
	web_content=urllib2.urlopen('http://apod.nasa.gov/apod/').read()
	patron = re.compile('.*<IMG SRC=\"(.*?)\"')
	matcher = patron.findall(web_content)
	return 'http://apod.nasa.gov/apod/'+matcher[0]
	
def get_page2():
	print("Downloading the page to find the image2...")
	web_content=urllib2.urlopen('http://www.aapodx2.com/').read()
	patron = re.compile('.*href=\"(.*?)\"><img')
	matcher = patron.findall(web_content)
	return 'http://www.aapodx2.com'+matcher[1]
	
def download_bg(bg):
	try:
		resp = urllib2.urlopen(bg.url)
	except urllib2.URLError, e:
		if not hasattr(e, "code"):
			raise
		print "The URL '"+bg.url+"' gave the error:", e.code, e.msg
		print("The background image won't be downloaded.")
	else:
		print("Downloading the image '"+bg.url+"' in '"+bg.loc+"'...")
		urllib.urlretrieve(bg.url,bg.loc)

b1 = BgImg('apod1',get_page1(),'.',now)
b1.to_string()
b2 = BgImg('apod2',get_page2(),'.',now)
b2.to_string()

download_bg(b1)
download_bg(b2)



