# VERSION: 20181208a
# By boot1110001.

### IMPORTS ############################################################
import os #for a lot of things
from os.path import expanduser #to get the HOME user dir in linux
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import datetime #to get the time
import subprocess #to execute BASH commands


### NON EDITABLE VARIABLES #############################################
HOME = expanduser("~") #to get the HOME user dir in linux
# time wehe this script is executed in format YYYY-mm-dd-HH-MM-SS
NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


### EDITABLE VARIABLES #################################################
# Write the path to the directory where the APOD images will be saved.
APOD1_DIR = HOME+"/00617/apod-dybg-py/tests/apod1"
# Write the path to the directory where the AAPOD2 images will be saved.
APOD2_DIR = HOME+"/00617/apod-dybg-py/tests/apod2"


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
	
def download_bg(bg):
	print("Downloading the image '"+bg.url+"' in '"+bg.loc+"'...")
	urllib.urlretrieve(bg.url,bg.loc)
		
def set_as_bg(bg):
	# The program should detect the desktop environment and select the correct command.
	bashCommand = 'gsettings set org.gnome.desktop.background picture-uri file://'+bg.loc
	print('CMD: '+bashCommand)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def clean_old_bgs():
	print("Cleaning the old background images...")
	
def clean_tmp_files():
	print("Cleaning temporary files...")
	# Temporary files are not yet saved.
	
def clean_all():
	clean_tmp_files()
	clean_old_bgs()
	

### MAIN ###############################################################
url1=get_page1()
url2=get_page2()

if (check_url(url1) and check_url(url2)):
	print("The two URLs are correct and work well.")
	b1 = BgImg('apod1',url1,APOD1_DIR,NOW)
	b1.to_string()
	b2 = BgImg('apod2',url2,APOD2_DIR,NOW)
	b2.to_string()

	download_bg(b1)
	download_bg(b2)

	set_as_bg(b1)
	# ~ set_as_bg(b2)
elif (check_url(url1):
	print("The AAPOD2 URL gave an error, ending...")
elif (check_url(url2)):
	print("The APOD URL gave an error, ending...")
else:
	print("The two URLs gave an error, ending...")


