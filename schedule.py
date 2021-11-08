import tkinter as T, webbrowser as W
from tkinter import *; from webbrowser import *
""" Trying to implement a schedule program for my younger.
    Still an intermediate and won't mind getting some help
"""
#The root widget
root =  Tk()
Title = root.title('TimeTable')
iconbitmap = root.iconbitmap('app.ico')

#setting a default minimum window size
size_setup = root.minsize(500,500)

#menu
menu_main = Menu(root)
cascade=menu_main.add_cascade(label='NEW')
cascade1=menu_main.add_cascade(label='EVENT')

#configuring the root widget
a = root.config(menu=menu_main)

#debug purpose
print(type(menu_main.add_cascade()))


root.mainloop()
