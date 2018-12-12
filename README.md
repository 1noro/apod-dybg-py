
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
> The configurations are implemented but not yet explained.

## Uninstallation
> Currently the `utils/uninstall.py` file is not yet implemented.

## Credits

- Created, programmed and maintained by [boot1110001](https://github.com/boot1110001).
- Inspired on the [script](https://gist.github.com/JoshSchreuder/882666) of [Josh Schreuder](https://gist.github.com/JoshSchreuder).

## Licenses

- Project under the __[GNU General Public License version 3](https://www.gnu.org/licenses/gpl.txt)__.
- The icons sets are under the __[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)__ (CC BY 4.0) license .
- The default wallpapers added to the project are images taken from web page [Astronomy Picture of the Day](https://apod.nasa.gov), so their __corresponding license__ will be applied.
