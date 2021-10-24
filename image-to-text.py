import pytesseract
import cv2 as cv
from os import listdir
from os.path import isfile, join


def imageToText(path):
  img = cv.imread(path, cv.IMREAD_GRAYSCALE)
  _, img = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)
  config_options = "-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-' ''\n''\t'"
  text = pytesseract.image_to_string(img, config=config_options)
  return text.strip()

path = './'
files = [f for f in listdir(path) if '.png' in f]
text = ""
for f in files:
  text += imageToText(f)

lines = text.splitlines()
unwanted = ['\n','\t',' ','']
for u in unwanted:
  lines = list(filter((u).__ne__, lines))

notes = ""
for l in lines:
  if l[:1].islower():
    notes = notes.rstrip() + ' ' + l + '\n'
  else:
    notes += l + '\n'

print(notes)

f = open('notes.txt','w')
f.write(notes)
f.close()