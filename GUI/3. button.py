from tkinter import *

#root window
root = Tk()

def myClick():
    myLabel = Label(root, text="button is clicked")
    myLabel.pack()

#create button widget
myButton = Button(root,text="Click Me", command=myClick)

#showing it onto the screen
myButton.pack()

root.mainloop()  
