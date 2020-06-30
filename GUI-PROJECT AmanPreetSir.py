from Tkinter import*
import Tkinter

import tkMessageBox
top=Tkinter.Tk()
top.geometry("1200x800")

                 #Chandigarh Academy work section

def helloCallBack():
    top.destroy()
    top1=Tkinter.Tk()
    top1.geometry("1200x800")
    var ="Hello Welcome To Chandigarh Academy"
    label=Label(top1,text=var)
    label.pack()

    bu=Tkinter.Button(top1,text="Name",height=1, width=20)
    bu.place(x=10,y=100)
    E=Entry(top1,bd=1)
    E.place(x=300,y=100)
    bu1=Tkinter.Button(top1,text="Course",height=1, width=20)
    bu1.place(x=10,y=200)
    E1=Entry(top1,bd=1)
    E1.place(x=300,y=200)
    bu2=Tkinter.Button(top1,text="Mobile No.",height=1,width=20)
    bu2.place(x=10,y=300)
    E2=Entry(top1,bd=1)
    E2.place(x=300,y=300)
    bu3=Tkinter.Button(top1,text="Place",height=1,width=20)
    bu3.place(x=10,y=400)
    E3=Entry(top1,bd=1)
    E3.place(x=300,y=400)
    bu4=Tkinter.Button(top1,text="Submit",height=3,width=20)
    bu4.place(x=100,y=500)
    bu5=Tkinter.Button(top1,text="Exit",command=rahul,height=3,width=20)
    bu5.place(x=1000,y=600)
    kk = E.get()

                       #Webtech Section Work
def rahul1():
        top2.destroy()


def helloCallBack1():
    global top2
    top.destroy()
    top2=Tkinter.Tk()
    top2.geometry("1200x800")
    var="Hello Welcome To WebTech Learning"
    label=Label(top2,text=var)
    label.pack()
    
    bu=Tkinter.Button(top2,text="Name",height=1, width=20)
    bu.place(x=10,y=100)
    E=Entry(top2,bd=1)
    E.place(x=300,y=100)
    bu1=Tkinter.Button(top2,text="Course",height=1, width=20)
    bu1.place(x=10,y=200)
    E1=Entry(top2,bd=1)
    E1.place(x=300,y=200)
    bu2=Tkinter.Button(top2,text="Mobile No.",height=1,width=20)
    bu2.place(x=10,y=300)
    E2=Entry(top2,bd=1)
    E2.place(x=300,y=300)
    bu3=Tkinter.Button(top2,text="Place",height=1,width=20)
    bu3.place(x=10,y=400)
    E3=Entry(top2,bd=1)
    E3.place(x=300,y=400)
    bu4=Tkinter.Button(top2,text="Submit",height=3,width=20)
    bu4.place(x=100,y=500)
    bu5=Tkinter.Button(top2,text="Exit",command=rahul1,height=3,width=20)
    bu5.place(x=1000,y=600)

                      #IELTS Section Work
    
def helloCallBack2():
    top.destroy()
    top3=Tkinter.Tk()
    top3.geometry("1200x800")
    var="Hello Welcome To IELTS"
    label=Label(top3,text=var)
    label.pack()

    bu=Tkinter.Button(top3,text="Name",height=1, width=20)
    bu.place(x=10,y=100)
    E=Entry(top3,bd=1)
    E.place(x=300,y=100)
    bu1=Tkinter.Button(top3,text="Course",height=1, width=20)
    bu1.place(x=10,y=200)
    E1=Entry(top3,bd=1)
    E1.place(x=300,y=200)
    bu2=Tkinter.Button(top3,text="Mobile No.",height=1,width=20)
    bu2.place(x=10,y=300)
    E2=Entry(top3,bd=1)
    E2.place(x=300,y=300)
    bu3=Tkinter.Button(top3,text="Place",height=1,width=20)
    bu3.place(x=10,y=400)
    E3=Entry(top3,bd=1)
    E3.place(x=300,y=400)
    bu4=Tkinter.Button(top3,text="Submit",height=3,width=20)
    bu4.place(x=100,y=500)
    bu5=Tkinter.Button(top3,text="Exit",command=rahul,height=3,width=20)
    bu5.place(x=1000,y=600)

    #defining a function
def rahul():
    b1=Tkinter.Button(top,text="Chandigarh Academy",command=helloCallBack, height=5, width=20)
    b1.place(x=10,y=100)
    b2=Tkinter.Button(top,text="WebTech Learning",command=helloCallBack1, height=5, width=20)
    b2.place(x=10,y=300)
    b3=Tkinter.Button(top,text="IELTS",command=helloCallBack2, height=5,width=20)
    b3.place(x=10,y=500)
    top.mainloop()
rahul()
