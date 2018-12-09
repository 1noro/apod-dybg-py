# VERSION: 20181208a
# By boot1110001. Based on the script of Josh Schreuder (2011)

import os #for home dir syntax
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import datetime #to get the time
import subprocess #to execute BASH commands

os.path.expanduser('~') #to get the home user

# time wehe this script is executed in format YYYY-mm-dd-HH-MM-SS
now=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") 

### CLASSES ############################################################
class BgImg:
	def __init__(self, name, url, loc_dir, now):
		patron = re.compile('\.(jpg|jpeg|png|gif)$')
		matcher = patron.findall(url)
		
		self.name	= name
		self.url	= url
		self.ext	= matcher[0]
		self.loc	= loc_dir+'/'+now+'-'+name+'.'+matcher[0]

	def to_string(self):
		print("My name is: "+self.name)
		print("My URL is: "+self.url)
		print("My localization is: "+self.loc)
		print("My extension is: "+self.ext)


### FUNCTIONS ##########################################################
def get_page1():
	print("Downloading the page to find the image...")
	web_content=urllib2.urlopen('http://apod.nasa.gov/apod/').read()
	patron=re.compile('.*<IMG SRC=\"(.*?)\"')
	matcher=patron.findall(web_content)
	return 'http://apod.nasa.gov/apod/'+matcher[0]
	
def get_page2():
	print("Downloading the page to find the image2...")
	web_content=urllib2.urlopen('http://www.aapodx2.com/').read()
	patron=re.compile('.*href=\"(.*?)\"><img')
	matcher=patron.findall(web_content)
	return 'http://www.aapodx2.com'+matcher[1]
	
def download_bg(bg):
	print("Downloading the image '"+bg.url+"' in '"+bg.loc+"'...")
	urllib.urlretrieve(bg.url,bg.loc)
		
def set_as_bg(bg):
	bashCommand = 'gsettings set org.gnome.desktop.background picture-uri file://'+bg.loc
	print('CMD: '+bashCommand)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def check_url(url):
	try:
		resp = urllib2.urlopen(url)
	except urllib2.URLError, e:
		if not hasattr(e,"code"):
			raise
		print "The URL '"+url+"' gave the error:", e.code, e.msg
		return False
	else:
		print "The URL '"+url+"' gave the code:", resp.code, resp.msg
		return True

### EXEC ###############################################################
url1=get_page1()
url2=get_page2()

if (check_url(url1) and check_url(url2)):
	print("The two URLs are correct and work well.")
	b1 = BgImg('apod1',url1,'/home/cosmo/00617/apod-dybg-py/tests/apod1',now)
	b1.to_string()
	b2 = BgImg('apod2',url2,'/home/cosmo/00617/apod-dybg-py/tests/apod2',now)
	b2.to_string()

	download_bg(b1)
	download_bg(b2)

	set_as_bg(b1)
	# ~ set_as_bg(b2)
else:
	print("One of the two URLs gave an error, ending...")


