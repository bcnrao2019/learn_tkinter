# https://www.youtube.com/watch?v=YXPyB4XeYLA it starts are 1:18:47 

from  tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code using Tkinter")
# root.iconbitmap("/home/bcnrao/Downloads/icon1.ico")
my_img1 = ImageTk.PhotoImage(Image.open("icon1.png"))

my_label = Label(image=my_img1)
my_label.pack()


# /home/bcnrao/Downloads






button_quit = Button(root, text="Quit", command=root.quit)

button_quit.pack()
root.mainloop()

