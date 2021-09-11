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
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    # if image_number > 5:
    #     image_number = image_number-1
    global my_label
    global button_for
    global button_back  

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])


    button_for = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number==5:
        button_for = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_for.grid(row=1, column=2)



def back(image_number):
    global my_label
    global button_for
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_for = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number==1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_for.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_for = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1, column=1)
button_for.grid(row=1, column=2)


# /home/bcnrao/Downloads
root.mainloop()

# it ends at 1:49:37 