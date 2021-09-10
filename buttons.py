# https://www.youtube.com/watch?v=YXPyB4XeYLA it starts are 19:38 

from  tkinter import *

root = Tk()

def myClick():

    myLabel = Label(root, text= "Look, I clicked the button", fg='red', bg='black')
    myLabel.pack()

# myButton1 = Button(root, text='Click me', state=DISABLED) 
# use state=DISABLED to keep the button inactive
# myButton1 = Button(root, text='Click me', padx=50, pady=50) # use padx/pady to set size of button

myButton1 = Button(root, text='Click me', command=myClick, fg='blue')

myButton1.pack()

root.mainloop()

