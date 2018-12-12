#! /usr/bin/python
#setup
# Package required to improve the experience (notify-osd)

### IMPORTS ####################################################################
import os
import shutil #for copy
import stat #for change permissions

### NON EDITABLE VARIABLES #####################################################
# To get the HOME user dir in linux.
HOME = os.path.expanduser("~")
# The version of the program.
VERSION=''
with open('version.txt', 'r') as version_file:
    VERSION=version_file.read().replace('\n', '')

### EXEC #######################################################################
print "# APOD Dynamic Background ["+VERSION+"] by boot1110001"
print "# Function: Install or update 'apod-dybg-py'"
print ""

# PREVIOUS CHECKS
print "# Checking if there is already a version of this program installed"
folder=HOME+'/.apod-dybg-py'
if os.path.exists(folder):
    print "# Yes, there is another version installed"
    try:
        with open(folder+'/version.txt', 'r') as version_file:
            installed_version=version_file.read().replace('\n', '')
            if (VERSION != installed_version):
                print "# The version is different, deleting and starting again"
                shutil.rmtree(folder)
            else:
                print "# It is the same version, only the updated files are replaced"
        pass
    except IOError:
        print "# The version file was not found, deleting and starting again"
        shutil.rmtree(folder)
        pass
else:
    print "# No, there is no other version installed"
print ""

# FOLDER STRUCTURE
print "### Creating the folder structure"
print "# Creating the folders for the program (if it does not already exist)"
folder=HOME+'/.apod-dybg-py'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/core'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/bg-default'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/apod-image'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/aapod2-image'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/8x8'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/16x16'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/22x22'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/24x24'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/32x32'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/48x48'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/256x256'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
folder=HOME+'/.apod-dybg-py/media/icons/512x512'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder

print "# Creating the folder for the .desktop file (if it does not already exist)"
folder=HOME+'/.local/share/applications'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder

print "# Creating the folder for the autostar .desktop file (if it does not already exist)"
folder=HOME+'/.config/autostart'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder

print "# Creating the folder for the app icon (if it does not already exist)"
folder=HOME+'/.icons'
if not os.path.exists(folder): os.makedirs(folder)
print " + "+folder
print ""

# COPYING FILES
print "### Copying files"
print "# Copying the program version file"
orig_file='version.txt'
dest_file=HOME+'/.apod-dybg-py/version.txt'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file

print "# Copying the main script"
orig_file='apod-dybg-py.py'
dest_file=HOME+'/.apod-dybg-py/apod-dybg-py.py'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
print "# Changing script permissions"
st = os.stat(dest_file)
# os.chmod(dest_file, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
os.chmod(dest_file, st.st_mode | 0111) #the same as avove.

print "# Copiyin the core modules"
orig_file='core/__init__.py'
dest_file=HOME+'/.apod-dybg-py/core/__init__.py'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='core/clases.py'
dest_file=HOME+'/.apod-dybg-py/core/clases.py'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='core/extra.py'
dest_file=HOME+'/.apod-dybg-py/core/extra.py'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file

print "# Copying all the default backgrounds"
orig_folder='media/bg-default'
dest_folder=HOME+'/.apod-dybg-py/media/bg-default'
src_files = os.listdir(orig_folder)
for file_name in src_files:
    full_file_name = os.path.join(orig_folder, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest_folder)

print "# Copying all the icons"
orig_file='media/icons/8x8/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/8x8/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/16x16/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/16x16/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/22x22/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/22x22/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/24x24/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/24x24/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/32x32/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/32x32/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/48x48/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/48x48/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/256x256/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/256x256/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
orig_file='media/icons/512x512/apod-dybg-py.png'
dest_file=HOME+'/.apod-dybg-py/media/icons/512x512/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file

print "# Copying the selected icon to the corresponding folder"
orig_file='media/icons/256x256/apod-dybg-py.png'
dest_file=HOME+'/.icons/apod-dybg-py.png'
shutil.copyfile(orig_file,dest_file)
print " cp "+dest_file
print ""

# Creating the script Gnome shell launcher (.desktop)
print "### Creating the script Gnome Shell launcher (.desktop)"
desktoptxt  = "[Desktop Entry]\n"
desktoptxt += "Type=Application\n"
desktoptxt += "Version="+VERSION+"\n"
desktoptxt += "Name=apod-dybg-py\n"
desktoptxt += "Comment=Astronomy Picture of the Day Dynamic Background.\n"
desktoptxt += "Path="+HOME+"/.apod-dybg-py\n"
desktoptxt += "Exec="+HOME+"/.apod-dybg-py/apod-dybg-py.py\n"
desktoptxt += "Icon=apod-dybg-py\n"
desktoptxt += "Terminal=false"
#desktoptxt += "Name[gl_ES]=apod-dybg"
print "# Result:"
print "-"*80
print desktoptxt
print "-"*80

print "# Copying the apod-dybg-py.desktop to the ~/.local/share/applications folder"
file=HOME+'/.local/share/applications/apod-dybg-py.desktop'
f = open(file, 'w')
f.write(desktoptxt)
f.close()

print "# Copying the apod-dybg-py.desktop to the ~/.config/autostart folder"
file=HOME+'/.config/autostart/apod-dybg-py.desktop'
f = open(file, 'w')
f.write(desktoptxt)
f.close()
print ""

print "### FINALIZED"
# print "### END"
