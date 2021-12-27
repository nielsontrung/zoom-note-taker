# Zoom Note Taker
An automated note taker for your zoom lectures.
## Implementation
This project was inspired for courses that do not upload lecture material, or content without text highlighting, and for open book assignments or exams.
This project was implemented using Python and the following Python libraries to screenshot lectures and image preprocessing to extract text content from the screenshots.
- cv2
- tesseract
# Getting Started
To use the zoom note taker first format the screen shot region by changing the region size and starting position in the get-screenshot-coords.py.
```python
import pyautogui
#change these numbers below the x and y offset start from the top left of your monitor screen
img = pyautogui.screenshot(region=(150,200,1300,700)) #(x-offset, y-offset, screenshot-width, screenshot-height)
img.save(r"C:\Users\niels\Desktop\image-to-text\img.png")
```
After the appropriate region has been found also update the screenshot region in the takezoomnotes.py while your zoom lecture starts.
```python
#change the region according to the coordinates found from the previous program
screenShotDimensions = (150, 200, 1300, 720)
```
You can also change the location of where your screenshots get saved also found in the takezoomnotes.py.
```python
def screenshot(file):
    img = pyautogui.screenshot(region=screenShotDimensions)
    img.save(r"C:\Users\niels\Desktop\image-to-text\\" + file)#change the file location inbetween the ""
```
After the program terminates your folder should contain screenshots of your lecture. 
The program currently does not detect duplicates in the folder so make sure you delete any duplicates slides that appear.
After deleting any duplicates run the image-to-text.py to convert the slides to text based notes.
Disclaimer the image to text conversion is raw so make sure your read over your notes 
