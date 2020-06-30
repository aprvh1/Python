from Tkinter import*
import Tkinter

import tkMessageBox

top=Tkinter.Tk()
top.geometry("1200x800")
top.title("Amanpreet")

       

def manager():
    top1=Tkinter.Tk()
    top1.geometry("1200x800")
    top1.title("Manager")

    lable=Label(top1,text="Username: ")
    lable.place(x=10,y=100)

    E1=Entry(top1,bd=1)
    E1.place(x=200, y=100)

    lable=Label(top1,text="Password: ")
    lable.place(x=10,y=300)

    E2=Entry(top1,bd=1)
    E2.place(x=200, y=300)


    def sub():
        a=E1.get()
        b=E2.get()

        if(a=="Aman" and b=="1234"):
            top1.destroy()
            top2=Tkinter.Tk()
            top2.geometry("300x100")
            label=Label(top2,text="Logged In")
            label.pack()

        else:
            top2=Tkinter.Tk()
            top2.geometry("300x100")
            label=Label(top2,text="Invalid Username or Password")
            label.pack()

    submit=Tkinter.Button(top1,text="Submit",command=sub ,height=5,width=20)
    submit.place(x=10,y=600)
               

    
    

def customer():
    top1=Tkinter.Tk()
    top1.geometry("1200x800")
    top1.title("Customer")

    lable=Label(top1,text="Username: ")
    lable.place(x=10,y=100)

    E1=Entry(top1,bd=1)
    E1.place(x=200, y=100)

    lable=Label(top1,text="Password: ")
    lable.place(x=10,y=300)

    E2=Entry(top1,bd=1)
    E2.place(x=200, y=300)

    def sub():
        a=E1.get()
        b=E2.get()

        if(a=="Aman" and b=="1234"):
            top1.destroy()
            top2=Tkinter.Tk()
            top2.geometry("300x100")
            label=Label(top2,text="Logged In")
            label.pack()

        else:
            top2=Tkinter.Tk()
            top2.geometry("300x100")
            label=Label(top2,text="Invalid Username or Password")
            label.pack()

    submit=Tkinter.Button(top1,text="Submit",command=sub ,height=5,width=20)
    submit.place(x=10,y=600)

       

button1=Tkinter.Button(top,text="Manager",command= manager,height=5,width=20)
button1.place(x=10,y=100)

button2=Tkinter.Button(top,text="Customer",command= customer,height=5,width=20)
button2.place(x=10,y=400)

top.mainloop()
