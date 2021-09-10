# https://www.youtube.com/watch?v=YXPyB4XeYLA it starts are 29:34

from  tkinter import *

root = Tk()

e = Entry(root, width=40, bg='pink', fg='white', borderwidth=4)
e.pack()
e.insert(0, "Enter your name")

def myClick():

    myLabel = Label(root, text= e.get(), fg='red', bg='black')
control

# myButton1 = Button(root, text='Click me', state=DISABLED) 
# use state=DISABLED to keep the button inactive
# myButton1 = Button(root, text='Click me', padx=50, pady=50) # use padx/pady to set size of button

myButton1 = Button(root, text='Enter Name', command=myClick, fg='blue')

myButton1.pack()

root.mainloop()

