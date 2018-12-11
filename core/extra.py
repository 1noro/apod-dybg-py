#core.extra
#by boot1110001

### IMPORTS ####################################################################
#import os #for a lot of things
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import subprocess #to execute BASH commands

from os import listdir #for list files in dir
from os.path import isfile, join #for list files in dir
from os import remove #for delete files

import clases

### FUNCTIONS ##################################################################
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

def clean_old_bgs(bg,folder):
	print("Cleaning the old background images from '"+folder+"':")
	folder_files = [f for f in listdir(folder) if isfile(join(folder, f))] #save the names of the files in the dir in a list
	folder_files.remove(bg.fname)
	for dfile in folder_files:
		print(" -removing: "+dfile)
		remove(folder+'/'+dfile)

def clean_tmp_files():
	print("Cleaning temporary files...")
	# Temporary files are not yet saved.

def get_prev_bg(folder):
	fname=""
	patron = re.compile('^\d{4}(?:-\d\d){5}-.*\.jpg|jpeg|png|gif$')
	folder_files = [f for f in listdir(folder) if isfile(join(folder, f))]
	for dfile in folder_files:
		if (patron.search(dfile)):
			fname=dfile #if there is a more recent file that matches the pattern but for some reason is further back in the list it will be ignored (FIX IT!!!)
			break
	return fname

def choose_def_bg(pre_fname,loc_dir,bg):
	out=bg
	if (pre_fname!=''):
		print("A image already exists in the directory '"+loc_dir+"'.")
		pre=clases.LocalBgImg(pre_fname,loc_dir)
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