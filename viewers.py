# https://www.youtube.com/watch?v=YXPyB4XeYLA it starts are 1:18:47 

from  tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code using Tkinter")
# root.iconbitmap("/home/bcnrao/Downloads/icon1.ico")

my_img1 = ImageTk.PhotoImage(Image.open("icon1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("/home/bcnrao/Downloads/palm-tree-icon.png"))
my_img3 = ImageTk.PhotoImage(Image.open("/home/bcnrao/Downloads/global-icon.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/home/bcnrao/Downloads/Windows-icon.png"))
my_img5 = ImageTk.PhotoImage(Image.open("/home/bcnrao/Downloads/dmd-doc-icon.png"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image=my_img1)
my_label.grid()


# /home/bcnrao/Downloads






button_quit = Button(root, text="Quit", command=root.quit)

button_quit.pack()
root.mainloop()

