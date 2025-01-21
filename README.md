# Zoom Note Taker
An automated note taker for your zoom lectures!
## Implementation
This project was inspired by the need for courses that do not upload lecture materials or content without text highlighting, as well as for open-book assignments or exams. It was implemented using Python and the libraries listed below to capture screenshots of Zoom lectures and convert the screenshots into text.
- cv2
- tesseract
# Getting Started
To use the Zoom note taker, run get-screenshot-coords.py and adjust the region size and starting position until the screenshot region matches the area of your lecture video.
```python
import pyautogui
#change these numbers below the x and y offset start from the top left of your monitor screen
img = pyautogui.screenshot(region=(150,200,1300,700)) #(x-offset, y-offset, screenshot-width, screenshot-height)
img.save(r"C:\Users\niels\Desktop\image-to-text\img.png")
```
After the appropriate region has been found also update the screenshot region in the takezoomnotes.py.
```python
#change the region according to the coordinates found from the previous program
screenShotDimensions = (150, 200, 1300, 720)
```
After updating the screenshot region, run takezoomnotes.py before your lecture starts. The program will automatically capture screenshots during the lecture. You can also change the location where your screenshots are saved, which can be configured in the takezoomnotes.py file.
```python
def screenshot(file):
    img = pyautogui.screenshot(region=screenShotDimensions)
    img.save(r"C:\Users\niels\Desktop\image-to-text\\" + file)#change the file location inbetween the ""
```
After manually terminating the program, your folder should contain screenshots of your lecture. The program currently does not detect duplicates, so be sure to delete any duplicate slides that may appear. Once you've removed the duplicates, run image-to-text.py to convert the slides into text-based notes.

Disclaimer: The image-to-text conversion is raw, so make sure to review your notes to ensure they are consistent with your slides.
