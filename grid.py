# https://www.youtube.com/watch?v=yQSEXcf6s2I

from  tkinter import *

root = Tk()

myLabel1 = Label(root, text='Hello world')
myLabel2 = Label(root, text='My name is Bhalchandra')
myLabel3 = Label(root, text='Hello world2')
myLabel4 = Label(root, text='My name is Varade')

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=0, column=1)
myLabel4.grid(row=1, column=1)

root.mainloop()

# https://www.youtube.com/watch?v=YXPyB4XeYLA