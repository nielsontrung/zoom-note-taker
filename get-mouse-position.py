from tkinter import *

def getMousePos(event):
  print("x: " + str(event.x) + " y: " + str(event.y))

window = Tk()

window.bind("<Button-1>", getMousePos)
window.mainloop()