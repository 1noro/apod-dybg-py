#core.extra
#by boot1110001

### IMPORTS ####################################################################
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import subprocess #to execute BASH commands

from os import listdir #for list files in dir
from os.path import isfile, join #for list files in dir
from os import remove #for delete files
from random import randint #to get a rabdom integer

# For desktop notifications
import gi
gi.require_version('Notify', '0.7') #required
from gi.repository import Notify, GdkPixbuf

from utils import CmdColor

### FUNCTIONS ##################################################################
def get_page1():
	print("[DOWN] Downloading the page 'http://apod.nasa.gov/apod/' to find the image1...")
	web_content=urllib2.urlopen('http://apod.nasa.gov/apod/').read()
	patron=re.compile('.*<IMG SRC=\"(.*?)\"')
	matcher=patron.findall(web_content)
	return 'http://apod.nasa.gov/apod/'+matcher[0]

def get_page2():
	print("[DOWN] Downloading the page 'http://www.aapodx2.com/' to find the image2...")
	web_content=urllib2.urlopen('http://www.aapodx2.com/').read()
	patron=re.compile('.*href=\"(.*?)\"><img')
	matcher=patron.findall(web_content)
	return 'http://www.aapodx2.com'+matcher[1]

def check_url(url):
	try:
		resp = urllib2.urlopen(url)
		print "["+CmdColor.OKGREEN+" OK "+CmdColor.ENDC+"] The URL '"+url+"' gave the code:", resp.code, resp.msg
		return True
	except urllib2.URLError, e:
		if not hasattr(e,"code"):
			raise
		print "["+CmdColor.FAIL+"FAIL"+CmdColor.ENDC+"] The URL '"+url+"' gave the error:", e.code, e.msg
		return False
	else:
		return False

def download_bg(bg):
	print("[DOWN] Downloading the image '"+bg.url+"' in '"+bg.get_loc()+"'...")
	urllib.urlretrieve(bg.url,bg.get_loc())

def set_as_bg(fname,full_loc):
	print("[INFO] Assigning '"+fname+"' as wallpaper...")
	# The program should detect the desktop environment and select the correct command.
	if (True):
		set_as_bg_XFCE(fname,full_loc)
	else:
		set_as_bg_GNOME_SHELL(fname,full_loc)

def set_as_bg_GNOME_SHELL(fname,full_loc):
	bashCommand = 'gsettings set org.gnome.desktop.background picture-uri file://'+full_loc
	# print('CMD: '+bashCommand)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def set_as_bg_XFCE(fname,full_loc):
	bashCommand = 'xfconf-query -c xfce4-desktop -l'
	# print('CMD: '+bashCommand)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	print(output)
	patron=re.compile('\n(.*last-image$)')
	matcher=patron.findall(output)
	print(matcher)

def send_notification(icon,summary,body):
	# From: https://www.devdungeon.com/content/desktop-notifications-linux-python
	# This one is required, but should already be installed
	# sudo apt-get install python-gobject

	# Installing this will install the
	# notify-send program. Check that out
	# for sending notifications in the shell
	# sudo apt-get install libnotify-bin

	# The development headers if you
	# want to do any development in C/C++
	# sudo apt-get install libnotify-dev

	Notify.init("apod-dybg-py")
	image = GdkPixbuf.Pixbuf.new_from_file(icon)
	notification = Notify.Notification.new(summary,body)
	notification.set_icon_from_pixbuf(image)
	# notification.set_image_from_pixbuf(image)
	notification.show()

def clean_old_bgs(bg,folder):
	print("[ RM ] Cleaning the old background images from '"+folder+"':")
	folder_files = [f for f in listdir(folder) if isfile(join(folder, f))] #save the names of the files in the dir in a list
	folder_files.remove(bg.fname)
	for dfile in folder_files:
		print("[    ]  -removing: "+dfile)
		remove(folder+'/'+dfile)

def clean_tmp_files():
	print("[ RM ] Cleaning temporary files...")
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

def choose_random_file(folder):
	folder_files = [f for f in listdir(folder) if isfile(join(folder, f))]
	return folder_files[randint(0,len(folder_files)-1)]

def set_def_bg(folder):
	fname=choose_random_file(folder)
	set_as_bg(fname,folder+'/'+fname)
