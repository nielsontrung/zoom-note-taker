import cv2 as cv

import numpy as np

img = cv.imread('arky temp slides-12.png')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
_, th1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4)
cv.imshow("img", img)
cv.imshow("th1", th1)
cv.imshow("adaptive", adaptive)
cv.waitKey(0)
cv.destroyAllWindows()