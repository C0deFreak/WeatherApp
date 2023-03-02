from tkinter import *
from PIL import ImageTk, Image


def Window():
  # Setup the Window
  window = Tk()
  window.geometry('1024x576')
  frame = Frame(window, width=1024, height=576)
  frame.pack()
  frame.place(anchor='center', relx=0.5, rely=0.5)

  # Create an object of tkinter ImageTk
  img = ImageTk.PhotoImage(Image.open("bg.jpg"))

  # Create a Label Widget to display the text or Image
  label = Label(frame, image=img)
  label.pack()

  search = Entry(window)
  search.place(anchor='center', relx=0.5, rely=0.5)

  window.mainloop()