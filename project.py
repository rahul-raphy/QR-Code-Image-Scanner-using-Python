import cv2
import numpy
from pyzbar.pyzbar import decode

img = cv2.imread('code.jpg')
code = decode(img)
print(code)

for qrCode in code:
    myText = qrCode.data.decode('utf-8')
    print("\033[1;32m Click on this Link:", myText)