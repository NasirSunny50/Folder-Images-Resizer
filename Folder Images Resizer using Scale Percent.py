import os
from PIL import Image
import PIL
import cv2
import glob

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

arr = absoluteFilePaths(r'E:\Nasir\Project\Image Resizer\Resizer')
scale_percent = int( input( "Please the Scale Percent: " ) )

for files in arr:   
    image = Image.open(files)
    print(image.size)
    width = int(image.size[0] * scale_percent / 100)
    height = int(image.size[1] * scale_percent / 100)
    dim = (width, height)
    r = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    r.size(image)
    image.save(files)

