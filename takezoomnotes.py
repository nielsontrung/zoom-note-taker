import pyautogui
import pytesseract
import cv2 as cv
import time
import datetime

screenShotDimensions = (150, 200, 1300, 720)

def imageToText(path):
  img = cv.imread(path, cv.IMREAD_GRAYSCALE)
  _, img = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)
  config_options = "-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-' ''\n''\t'"
  text = pytesseract.image_to_string(img, config=config_options)
  return text.strip()

def screenshot(file):
    img = pyautogui.screenshot(region=screenShotDimensions)
    img.save(r"C:\Users\niels\Desktop\image-to-text\\" + file)


def formatNotes(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        whitespace = ['', ' ', '\n', '\t']
        for w in whitespace:
            lines = list(filter((w).__ne__, lines))
        text = ""
        for l in lines:
            if l[:1].islower():
                text = text.rstrip() + ' ' + l + '\n'
            else:
                text += l + '\n'
        print(text)

def takeNotes():
    slideNum = 1
    dt = datetime.datetime.today().strftime('%Y-%m-%d')
    currentSlide = dt + "-arky-slide-" + str(slideNum).zfill(2) + ".png"
    screenshot(currentSlide)
    file = dt + "-arky-notes.txt"
    f = open(file, "w")
    slideNotes = imageToText(currentSlide)
    f.write(slideNotes)
    try:
        while 1:
            time.sleep(1)
            # if the last screenshot is not on the screen take new screenshot
            if not pyautogui.locateOnScreen(currentSlide, region=screenShotDimensions, grayscale=True, confidence=0.9):
                slideNum += 1
                currentSlide = dt + "-arky-slide-" + str(slideNum).zfill(2) + ".png"
                screenshot(currentSlide)
                slideNotes = imageToText(currentSlide)
                print(slideNotes)
                f.write(slideNotes)

    except KeyboardInterrupt:
        f.close()
        print("Done")
        formatNotes(file)

if __name__ == '__main__':
    takeNotes()