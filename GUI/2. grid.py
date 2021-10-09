from tkinter import *

#root window
root = Tk()

#create label widget
myLabel1 = Label(root,text="hello world")
myLabel2 = Label(root,text="hello py")

#showing it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()  
