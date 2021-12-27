import pytesseract
import datetime 
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

lines = text.splitlines()
unwanted = ['\n','\t',' ','']
for u in unwanted:
  lines = list(filter((u).__ne__, lines))

dt = datetime.datetime.today().strftime('%Y-%m-%d')
filename = dt + "-arky-notes.txt"

f = open(filename,'w')
f.write(notes)
f.close()