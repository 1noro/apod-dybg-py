#! /usr/bin/python
#apod-dybg
#by boot1110001

### IMPORTS ####################################################################
from os.path import expanduser #to get the HOME user dir in linux
import datetime #to get the time
from optparse import OptionParser #for exec options parser

import core.clases
import core.extra

### NON EDITABLE VARIABLES #####################################################
# To get the HOME user dir in linux.
HOME = expanduser("~")
# Time wehe this script is executed in format YYYY-mm-dd-HH-MM-SS.
NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

### EDITABLE VARIABLES #########################################################
# To ensure the correct operation of the program, the variables
# APOD1_DIR and APOD2_DIR must be different routes.

# Write the path to the directory where the APOD images will be saved.
APOD1_DIR = HOME+"/00617/apod-dybg-py-tests/apod1"
# Write the path to the directory where the AAPOD2 images will be saved.
APOD2_DIR = HOME+"/00617/apod-dybg-py-tests/apod2"
# Select the APOD preference (1) over AAPOD2 (2). By default, APOD (1) will be used.
PREFERENCE = 1
# Write the path to the directory where the default images are saved.
DEFBG_DIR = HOME+"/00617/apod-dybg-py-tests/default-bg"
# Extra vervose option (to see the file's information).
VERVOSE = False

### FUNCTIONS ##################################################################
def choose_def_bg(pre_fname, loc_dir, bg):
	out = bg
	if (pre_fname != ''):
		print("A image already exists in the directory '"+loc_dir+"'.")
		pre = core.clases.LocalBgImg(pre_fname, loc_dir)
		if VERVOSE: print(pre.to_string())
		if(pre == bg):
			print("The image has not yet been updated on the web. No need to download a new one.")
			out = pre
		else:
			print("The image of the web is more updated.")
			core.extra.download_bg(bg)
	else:
		core.extra.download_bg(bg)
	return out

### MAIN #######################################################################
def main():
	url1 = core.extra.get_page1()
	url2 = core.extra.get_page2()

	if (core.extra.check_url(url1) and core.extra.check_url(url2)):
		print("The two URLs are correct and work well.")
		bg1 = core.clases.RemoteBgImg('apod1', url1, APOD1_DIR,NOW)
		if VERVOSE: print(bg1.to_string())
		bg2 = core.clases.RemoteBgImg('apod2', url2, APOD2_DIR,NOW)
		if VERVOSE: print(bg2.to_string())

		pre_fname1 = core.extra.get_prev_bg(APOD1_DIR)
		pre_fname2 = core.extra.get_prev_bg(APOD2_DIR)

		bg1 = choose_def_bg(pre_fname1, APOD1_DIR, bg1)
		bg2 = choose_def_bg(pre_fname2, APOD2_DIR, bg2)

		if (PREFERENCE == 2):
			core.extra.set_as_bg(bg2.fname,bg2.get_loc())
		else:
			core.extra.set_as_bg(bg1.fname,bg1.get_loc())

		core.extra.clean_old_bgs(bg1, APOD1_DIR)
		core.extra.clean_old_bgs(bg2, APOD2_DIR)
	elif (core.extra.check_url(url1)):
		print("The AAPOD2 URL gave an error, ending...")
		bg1 = core.clases.RemoteBgImg('apod1', url1, APOD1_DIR, NOW)
		if VERVOSE: print(bg1.to_string())

		pre_fname1 = core.extra.get_prev_bg(APOD1_DIR)

		bg1 = choose_def_bg(pre_fname1, APOD1_DIR, bg1)

		core.extra.set_as_bg(bg1.fname,bg1.get_loc())

		core.extra.clean_old_bgs(bg1, APOD1_DIR)
	elif (core.extra.check_url(url2)):
		print("The APOD URL gave an error, ending...")
		bg2 = core.clases.RemoteBgImg('apod2', url2, APOD2_DIR, NOW)
		if VERVOSE: print(bg2.to_string())

		pre_fname2 = core.extra.get_prev_bg(APOD2_DIR)

		bg2 = choose_def_bg(pre_fname2, APOD2_DIR, bg2)

		core.extra.set_as_bg(bg2.fname,bg2.get_loc())

		core.extra.clean_old_bgs(bg2, APOD2_DIR)
	else:
		print("The two URLs gave an error, ending...")
		fname=extra.choose_random_file(DEFBG_DIR)
		extra.set_as_bg(fname,DEFBG_DIR+'/'+fname)

### EXEC #######################################################################
# CHECK IN THE FUTURE HOW IT WORKS
# parser = OptionParser()
# parser.add_option("-v", action="store_true", dest="verbose")
# parser.add_option("-q", action="store_false", dest="verbose")
# (options, args) = parser.parse_args()

main()
