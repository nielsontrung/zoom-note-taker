from os import listdir, remove
from os.path import isfile, join
from PIL import Image, ImageChops

path = './'
files = [f for f in listdir(path) if '.png' in f]

for i in files:
  for j in files:
    if i != j:
      img1 = Image.open(i)
      img2 = Image.open(j)
      diff = ImageChops.difference(img1, img2)
      if diff.getbbox():
        diff.show()
        print("removing duplicate file " + j)
        remove(j)