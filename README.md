
# ![](https://raw.githubusercontent.com/boot1110001/apod-dybg-py/master/media/icons/24x24/apod-dybg-py.png) Astronomy Picture Of the Day DYBG
The Astronomy Picture Of the Day Dynamic Background is a program to install in your PC and change daily the wallpaper of your GNOME Shell for the photo of the [Astronomy Picture of the Day](https://apod.nasa.gov) or the [Amateur Astronomy Picture of the Day](http://www.aapodx2.com) according to [your preference](https://github.com/boot1110001/apod-dybg-py#configuration).

This prject is a Python rewrite of my [previous project](https://github.com/boot1110001/apod-dybg) written in BASH.

> In the future I would like to add support for more desktop environments (starting with XFCE).

## Requirements
At the present time, this program only __works on GNU/Linux with a GNOME Shell desktop__ environment.

This one is required, but should already be installed:

```
sudo apt-get install python-gobject
```

The tests prove that it _works correctly_ on Ubuntu 18.04.01 with GNOME Shell 3.28.3 and the 2.7.15rc1 Python version, and I have not needed to install any program.

> Note that this project is still under development, so it is not yet stable enough.

## Installation :rocket:
Currently the project is at a very early stage of its development (_BETA_), you can install it on your PC, but future versions may delete previous configurations in the program.

```
git clone https://github.com/boot1110001/apod-dybg-py.git
cd apod-dybg-py
chmod u+x setup.py
./setup.py
```

## Configuration

In the file `apod-dybg-py.py` you can find this section at the beginning of the file:

```
### EDITABLE VARIABLES #########################################################
# To ensure the correct operation of the program, the variables
# APOD1_DIR and APOD2_DIR must be different routes.

# Write the path to the directory where the APOD images will be saved.
APOD1_DIR = HOME+'/.apod-dybg-py/media/apod-image'
# Write the path to the directory where the AAPOD2 images will be saved.
APOD2_DIR = HOME+'/.apod-dybg-py/media/aapod2-image'
# Select the APOD preference (1) over AAPOD2 (2). By default, APOD (1) will be used.
PREFERENCE = 1
# Write the path to the directory where the default images are saved.
DEFBG_DIR = HOME+'/.apod-dybg-py/media/bg-default'
# Extra vervose option (to see the file's information).
VERVOSE = False
```

Information to keep in mind:

- The changes made before the installation of the program on your PC will be applied in the subsequent installation.
- If you want to modify the configuration of the program once it is installed on your PC, the file `apod-dybg-py.py` will be found in the folder `~/.apod-dybg-py/apod-dybg-py.py`.
- The variable `HOME` entered before directory addresses contains the absolute path to the home folder of the user who runs the program.
- You can add your own default backgrounds by copying them to the `~/.apod-dybg-py/media/bg-default` folder of the program once it is installed on your computer.

## Uninstallation
> Currently the `utils/uninstall.py` file is not yet implemented.

## Credits

- Created, programmed and maintained by [boot1110001](https://github.com/boot1110001).
- Inspired on the [script](https://gist.github.com/JoshSchreuder/882666) of [Josh Schreuder](https://gist.github.com/JoshSchreuder).

## Licenses

- Project under the __[GNU General Public License version 3](https://www.gnu.org/licenses/gpl.txt)__.
- The icons sets are under the __[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)__ (CC BY 4.0) license .
- The default wallpapers added to the project are images taken from web page [Astronomy Picture of the Day](https://apod.nasa.gov), so their __corresponding license__ will be applied.
