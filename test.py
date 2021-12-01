import os
from PIL import Image
import PIL
import glob

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

arr = absoluteFilePaths(r'E:\Nasir\Project\Image Resizer\Resizer')
for files in arr:   
    fixed_width = 500 #Determine a fixed number for creating the ratio
    image = Image.open(files)
    print(image.size)
    wpercent = (fixed_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((hsize, fixed_width), PIL.Image.ANTIALIAS)
    image.save(files)

