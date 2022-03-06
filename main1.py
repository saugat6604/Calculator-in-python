import tkinter
from PIL import ImageTk, Image
import os
  
# creating main window
root = tkinter.Tk()
  
# loading the image
img = ImageTk.PhotoImage(Image.open("calc.gif"))
  
# reading the image
panel = tkinter.Label(root, image = img)
  
# setting the application
panel.pack(side = "bottom", fill = "both",
           expand = "yes")
  
# running the application
root.mainloop()