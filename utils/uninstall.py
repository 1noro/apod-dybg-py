#! /usr/bin/python
#uninstall
#by boot1110001

# CAUTION: The uninstall.py file that you must execute will be the one
# corresponding to the version installed on your PC.
# Implement function to check the above.

### IMPORTS ####################################################################
import os
import shutil #for copy

### NON EDITABLE VARIABLES #####################################################
# To get the HOME user dir in linux.
HOME = os.path.expanduser("~")
# The version of the program.
VERSION=''
with open('version.txt', 'r') as version_file:
    VERSION=version_file.read().replace('\n', '')

### EXEC #######################################################################
print "# APOD Dynamic Background ["+VERSION+"] by boot1110001"
print "# Function: Uninstall 'apod-dybg-py'"

print "# Removing program folder"
folder = HOME+'/.apod-dybg-py'
shutil.rmtree(folder)
print " -"+folder+"/*"

print "# Removing program icons"
file = HOME+'/.icons/apod-dybg-py.png'
os.remove(file)
print " -"+file

print "# Removing program .desktop file from applications"
file = HOME+'/.local/share/applications/apod-dybg-py.desktop'
os.remove(file)
print " -"+file

print "# Removing program .desktop file from autostart"
file = HOME+'/.config/autostart/apod-dybg-py.desktop'
os.remove(file)
print " -"+file

print "# FINALIZED"
# print "### END"
