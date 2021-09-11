# https://www.youtube.com/watch?v=YXPyB4XeYLA it starts are 38.555

from  tkinter import *
from typing import overload

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# e.insert(0, "Enter your name")

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_num = e.get()
    global f_num
    global action 
    action = 'add'
    f_num = float(first_num)
    e.delete(0, END)


def button_sub():
    first_num = e.get()
    global f_num
    global action 
    action = 'sub'
    f_num = float(first_num)
    e.delete(0, END)


def button_mul():
    first_num = e.get()
    global f_num
    global action 
    action = 'mul'
    f_num = float(first_num)
    e.delete(0, END)


def button_div():
    first_num = e.get()
    global f_num
    global action 
    action = 'div'
    f_num = float(first_num)
    e.delete(0, END)


def button_equal():
    second_num = e.get()
    e.delete(0, END)    
    if action == 'add':
        e.insert(0, str( f_num + float(second_num)))
    elif action == 'sub':
        e.insert(0, str( f_num - float(second_num)))    
    elif action == 'mul':
        e.insert(0, str( f_num * float(second_num)))    
    elif action == 'div':
        e.insert(0, str( f_num / float(second_num)))    

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20,command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20,command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20,command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20,command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20,command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20,command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20,command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20,command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=50,command=lambda: button_click(0))
button_ad = Button(root, text='+', padx=40, pady=20,command= button_add)
button_su = Button(root, text='-', padx=40, pady=20,command= button_sub)
button_mu = Button(root, text='x', padx=40, pady=20,command= button_mul)
button_di = Button(root, text='/', padx=40, pady=20,command= button_div)
button_eq = Button(root, text='=', padx=90, pady=20,command=button_equal)
button_cl = Button(root, text='Clear', padx=79, pady=20,command= button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, rowspan=2)

button_eq.grid(row=5, column=1, columnspan=2)
button_cl.grid(row=4, column=1, columnspan=2)


button_ad.grid(row=1, column=3)
button_su.grid(row=2, column=3)
button_mu.grid(row=3, column=3)
button_di.grid(row=4, column=3)

# myButton.pack()

root.mainloop()

