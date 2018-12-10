# VERSION: 20181210a
# By boot1110001.

### IMPORTS ############################################################
import os #for a lot of things
from os.path import expanduser #to get the HOME user dir in linux
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import datetime #to get the time
import subprocess #to execute BASH commands
from os import listdir #for list files in dir
from os.path import isfile, join #for list files in dir

### NON EDITABLE VARIABLES #############################################
HOME = expanduser("~") #to get the HOME user dir in linux
# time wehe this script is executed in format YYYY-mm-dd-HH-MM-SS
NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


### EDITABLE VARIABLES #################################################
# To ensure the correct operation of the program, the variables 
# APOD1_DIR and APOD2_DIR must be different routes.

# Write the path to the directory where the APOD images will be saved.
APOD1_DIR = HOME+"/00617/apod-dybg-py/tests/alpha/apod1"
# Write the path to the directory where the AAPOD2 images will be saved.
APOD2_DIR = HOME+"/00617/apod-dybg-py/tests/alpha/apod2"
# Select the APOD preference (1) over AAPOD2 (2). By default, APOD (1) will be used.
PREFERENCE = 1


### CLASSES ############################################################
class BgImg:
	def __init__(self, distinct, url, loc_dir, now):
		patron = re.compile('\.(jpg|jpeg|png|gif)$')
		matcher = patron.findall(url)
		
		remote_file = urllib.urlopen(url)
		meta = remote_file.info()
		
		self.url = url
		self.distinct = distinct
		self.dir = loc_dir
		self.exdate = now
		self.ext = matcher[0]
		self.fsize = meta.getheaders("Content-Length")[0]
		self.fname = now+'-'+distinct+'.'+matcher[0]
		
	def get_loc(self):
		return self.dir+'/'+self.fname
		
	def get_date(self):
		fname_list=self.fname.split('-')
		return fname_list[0]+'-'+fname_list[1]+'-'+fname_list[2]

	def to_string(self):
		string="="*80+"\n"
		string+="My file name is: "+self.fname+"\n"
		string+="My URL is: "+self.url+"\n"
		string+="My localization is: "+self.get_loc()+"\n"
		string+="My directory is: "+self.dir+"\n"
		string+="My execution date is: "+self.exdate+"\n"
		string+="My date is: "+self.get_date()+"\n"
		string+="My distinct is: "+self.distinct+"\n"
		string+="My extension is: "+self.ext+"\n"
		string+="My size in bytes is: "+self.fsize+"\n"
		string+="="*80+""
		return string
		
	def __eq__(self,other):
		out=False
		if (other.dir and other.distinct and other.ext and other.fsize and other.get_date()):
			if (other.dir==self.dir and other.distinct==self.distinct and other.ext==self.ext and other.fsize==self.fsize and other.get_date() == self.get_date()):
				out=True
		return out
		
	def __ne__(self, other):
		#Overrides the default implementation (unnecessary in Python 3)
		return not self.__eq__(other)

class LocalBgImg:
	def __init__(self, fname, loc_dir):
		patron = re.compile('\.(jpg|jpeg|png|gif)$')
		matcher = patron.findall(fname)
		fname_list=fname.split('-')
		
		local_file = open(loc_dir+'/'+fname, "rb")
		self.fsize=str(len(local_file.read()))
		local_file.close()
		
		self.dir = loc_dir
		self.fname = fname
		self.ext = matcher[0]
		self.exdate = fname.replace('-'+fname_list[-1],'')
		self.distinct = fname_list[-1].replace('.'+matcher[0],'')
		
	def get_loc(self):
		return self.dir+'/'+self.fname
		
	def get_date(self):
		fname_list=self.fname.split('-')
		return fname_list[0]+'-'+fname_list[1]+'-'+fname_list[2]

	def to_string(self):
		string="="*80+"\n"
		string+="My file name is: "+self.fname+"\n"
		string+="My localization is: "+self.get_loc()+"\n"
		string+="My directory is: "+self.dir+"\n"
		string+="My execution date is: "+self.exdate+"\n"
		string+="My date is: "+self.get_date()+"\n"
		string+="My distinct is: "+self.distinct+"\n"
		string+="My extension is: "+self.ext+"\n"
		string+="My size in bytes is: "+self.fsize+"\n"
		string+="="*80+""
		return string

	def __eq__(self,other):
		out=False
		if (other.dir and other.distinct and other.ext and other.fsize and other.get_date()):
			if (other.dir==self.dir and other.distinct==self.distinct and other.ext==self.ext and other.fsize==self.fsize and other.get_date() == self.get_date()):
				out=True
		return out
		
	def __ne__(self, other):
		#Overrides the default implementation (unnecessary in Python 3)
		return not self.__eq__(other)


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
	print("Downloading the image '"+bg.url+"' in '"+bg.get_loc()+"'...")
	urllib.urlretrieve(bg.url,bg.get_loc())
		
def set_as_bg(bg):
	print("Assigning '"+bg.fname+"' as wallpaper...")
	# The program should detect the desktop environment and select the correct command.
	bashCommand = 'gsettings set org.gnome.desktop.background picture-uri file://'+bg.get_loc()
	# ~ print('CMD: '+bashCommand)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def clean_old_bgs(bg1,bg2):
	print("Cleaning the old background images from '"+APOD1_DIR+"':")
	apod1_files = [f for f in listdir(APOD1_DIR) if isfile(join(APOD1_DIR, f))] #save the names of the files in the dir in a list
	apod1_files.remove(bg1.fname)
	for dfile in apod1_files:
		print(" -removing: "+dfile)
		os.remove(APOD1_DIR+'/'+dfile)

	print("Cleaning the old background images from '"+APOD2_DIR+"':")
	apod2_files = [f for f in listdir(APOD2_DIR) if isfile(join(APOD2_DIR, f))] #save the names of the files in the dir in a list
	apod2_files.remove(bg2.fname)
	for dfile in apod2_files:
		print(" -removing: "+dfile)
		os.remove(APOD2_DIR+'/'+dfile)
	
def clean_tmp_files():
	print("Cleaning temporary files...")
	# Temporary files are not yet saved.

def get_prev_bg(folder):
	fname=""
	patron = re.compile('^\d{4}(?:-\d\d){5}-.*\.jpg|jpeg|png|gif$')
	folder_files = [f for f in listdir(folder) if isfile(join(folder, f))]
	for dfile in folder_files:
		if (patron.search(dfile)):
			fname=dfile #if there is a more recent file that matches the pattern but for some reason is further back in the list it will be ignored
			break
	return fname
	
def choose_def_bg(pre_fname,loc_dir,bg):
	out=bg
	if (pre_fname!=''):
		print("A image already exists in the directory '"+loc_dir+"'.")
		pre=LocalBgImg(pre_fname,loc_dir)
		print(pre.to_string())
		if(pre==bg):
			print("The image has not yet been updated on the web. No need to download a new one.")
			out=pre
		else:
			print("The image of the web is more updated.")
			download_bg(bg)
	else:
		download_bg(bg)
	return out
	

### MAIN ###############################################################
def main():
	url1=get_page1()
	url2=get_page2()

	if (check_url(url1) and check_url(url2)):
		print("The two URLs are correct and work well.")
		bg1 = BgImg('apod1',url1,APOD1_DIR,NOW)
		print(bg1.to_string())
		bg2 = BgImg('apod2',url2,APOD2_DIR,NOW)
		print(bg2.to_string())

		pre_fname1=get_prev_bg(APOD1_DIR)
		pre_fname2=get_prev_bg(APOD2_DIR)
		
		bg1=choose_def_bg(pre_fname1,APOD1_DIR,bg1)
		bg2=choose_def_bg(pre_fname2,APOD2_DIR,bg2)
		
		if (PREFERENCE == 2):
			set_as_bg(bg2)
		else:
			set_as_bg(bg1)
		
		clean_old_bgs(bg1,bg2)
	elif (check_url(url1)):
		print("The AAPOD2 URL gave an error, ending...")
		bg1 = BgImg('apod1',url1,APOD1_DIR,NOW)
		print(bg1.to_string())

		pre_fname1=get_prev_bg(APOD1_DIR)
		
		bg1=choose_def_bg(pre_fname1,APOD1_DIR,bg1)
		
		set_as_bg(bg1)
		
		# ~ clean_old_bgs(bg1,bg2) #MOD THIS
	elif (check_url(url2)):
		print("The APOD URL gave an error, ending...")
		bg2 = BgImg('apod2',url2,APOD2_DIR,NOW)
		print(bg2.to_string())

		pre_fname2=get_prev_bg(APOD2_DIR)
		
		bg2=choose_def_bg(pre_fname2,APOD2_DIR,bg2)
		
		set_as_bg(bg2)
		
		# ~ clean_old_bgs(bg1,bg2) #MOD THIS
	else:
		print("The two URLs gave an error, ending...")


### EXEC ###############################################################
main()













