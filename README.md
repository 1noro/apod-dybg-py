
# Astronomy Picture Of the Day DYBG ![](https://raw.githubusercontent.com/boot1110001/apod-dybg-py/master/media/icons/32x32/apod-dybg-py.png)
Script to change daily the wallpaper of your GNOME Shell for the photo of the "Astronomy Picture of the Day" (https://apod.nasa.gov) or the "Amateur Astronomy Picture of the Day" (http://www.aapodx2.com) according to your preference.

This version is a Python rewrite of my previous project written in BASH (https://github.com/boot1110001/apod-dybg).

In the future I would like to add support for more desktop environments (starting with XFCE).

## Requirements
This program only works currently on GNU/Linux with a GNOME Shell desktop environment.

This one is required, but should already be installed:

```
sudo apt-get install python-gobject
```

The tests prove that it works correctly on Ubuntu 18.04.01 with GNOME Shell and the 2.7.15rc1 Python version, and I have not needed to install any program.

Note that this project is still under development, so it is not yet stable enough.

## Installation
Currently the project is at a very early stage of its development (BETA), you can install it on your PC, but future versions may delete previous configurations in the program.

```
git clone https://github.com/boot1110001/apod-dybg-py.git
cd apod-dybg-py
chmod u+x setup.py
./setup.py
```

## Uninstallation
Currently the ```utils/uninstall.py``` file is not yet implemented.

## Credits

- Created, programmed and maintained by boot1110001.
- Inspired on the script of Josh Schreuder (2011) https://gist.github.com/JoshSchreuder/882666.

## Licenses

- Project under the GNU General Public License version 3 (https://www.gnu.org/licenses/gpl.txt).
- The icons sets are under the Creative Commons Attribution 4.0 International (CC BY 4.0) license (https://creativecommons.org/licenses/by/4.0/).
- The default wallpapers added to the project are images taken from web page https://apod.nasa.gov/apod, so their corresponding license will be applied.
