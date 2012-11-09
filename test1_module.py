'''
Created on Oct 17, 2012

@author: isa
'''
from Tkinter import *
root = Tk()
root.title("Test GUI")

textbox=Entry(root)
listbox = Listbox(root)

def Button1():
    listbox.insert(END, "Button1 pressed!")
def Button2():
    listbox.insert(END, "Button2 pressed!")
def Button3():
    text_contents = textbox.get()
    listbox.insert(END, text_contents)
    textbox.delete(0,END)

Button1 = Button(root, text="button1", command = Button1)
Button2 = Button(root, text="button2", command = Button2)
Button3 = Button(root, text="button3", command = Button3)

textbox.delete(0,END)

Button1.pack()
Button2.pack()
Button3.pack()
textbox.pack()
listbox.pack()

root.mainloop()
