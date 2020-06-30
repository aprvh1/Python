from Tkinter import*
import Tkinter

import tkMessageBox

top=Tkinter.Tk()
top.geometry("1200x800")


def func1():
    top.destroy()
    top1=Tkinter.Tk()
    top1.geometry("1200x800")
    label=Label(top1,text="Hello Manager")
    label.pack()
    
def func2():
    top.destroy()
    top1=Tkinter.Tk()
    top1.geometry("1200x800")
    label=Label(top1,text="Hello Customer")
    label.pack()


    
button1=Tkinter.Button(top,text="Manager",command=func1,height=1,width=20)
button1.place(x=10,y=200)

button2=Tkinter.Button(top,text="Customer",command=func2,height=1,width=20)
button2.place(x=10,y=500)

top.mainloop() #this is for main window and put at end only
