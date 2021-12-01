import PIL
import os
import os.path
from PIL import Image

f = r'Resizer'

width  = int( input( "Please enter the width: " ) )
height = int( input( "Please enter the height: " ) )

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((width,height))
    img.save(f_img)
