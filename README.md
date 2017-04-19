# simpleRenderer

## Installation and Dependencies

This project depends on both PyGame and PyOpenGL meaning these need to be
installed in order for the test.py script to run as expected.

Installation of these on a Linux based machine is simple and is explained [here](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)
for PyGame and [here](http://pyopengl.sourceforge.net/) for PyOpenGL.

For a Windows based machine, Pygame provides instructions for installation,
while PyOpenGL is best handled [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
 for windows.


## Running The Program

The program requires a .obj file to run. Simply execute from the command line
from within the home directory of the project as such:

  python test.py [objfile]

## Basic Controls

The program has some basic functionality for manipulation of the object that
is rendered. This includes positioning the camera further from and closer to
the object, rotating the object about any axis, and translating the object.

Left-Click + MouseMotion causes translation of the object.

Right-Click + MouseMotion causes rotation of the object.

MouseWheel causes zooming in and out of the camera.
