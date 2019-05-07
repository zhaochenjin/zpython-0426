from tkinter import *

top = Tk()


# todo

def hello_callback():
    print('hello Tkinter!')


for r in range(3):
    for c in range(3):
        button = Button(top, text='', command=hello_callback, width=10, height=5)
        button.grid(row=r, column=c)

mainloop()


# https://www.tutorialspoint.com/python/python_gui_programming.htm