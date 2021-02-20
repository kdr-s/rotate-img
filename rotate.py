from PIL import Image
import glob
import re

files = glob.glob("*")

for file in files:
    if re.search('\.jpg|\.gif|\.png|\.jpeg', file, re.IGNORECASE):
        im = Image.open(file)
        if im.size[0] > im.size[1]:
            im = im.rotate(90, expand=True)
            im.save(file, quality=100)
