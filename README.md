# QR-Code-Image-Scanner-using-Python
This Python project will scan QR Code from an image using opencv module.


Install the required libraries using the following commands.

For OpenCV: pip install opencv-python

For pyzbar: pip install pyzbar

For Numpy: pip install numpy

On Line 11, I use ANSI escape codes to change the color of the text output in the python program.
ANSI escape code will set the text color to bright green. The format is;
\033[ = Escape code, this is always the same
1 = Style, 1 for normal
32 = Text colour, 32 for bright green
