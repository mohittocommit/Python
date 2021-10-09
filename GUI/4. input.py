from tkinter import *

#root window
root = Tk()

#input field
e = Entry(root)
e.pack()
e.insert(0,"Enter Name")

def myClick():
    
    myLabel = Label(root, text=e.get())
    myLabel.pack()

#create button widget
myButton = Button(root,text="Click Me", command=myClick)

#showing it onto the screen
myButton.pack()

root.mainloop()  
