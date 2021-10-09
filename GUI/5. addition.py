from tkinter import *

#root window
root = Tk()


e1 = Entry(root)
e1.pack()
e1.insert(0,"Enter First Number:")

e2 = Entry(root)
e2.pack()
e2.insert(1,"Enter Second Number:")

def myClick():
    result = int(e1.get())+int(e2.get())
    resultLabel = Label(root, text=result)
    resultLabel.pack()

#create button widget
myButton = Button(root,text="Addition", command=myClick)

#showing it onto the screen
myButton.pack()

root.mainloop()  



