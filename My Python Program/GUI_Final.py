from Tkinter import*
import Tkinter
import tkMessageBox
import mysql.connector

db = mysql.connector.connect(host="localhost",database="Institute",user="root",password="12345")
cursor=db.cursor()



top = Tkinter.Tk()
top.geometry("600x700")
top.title("Institute Portal")
lab1=Label(top, text="Institute Portal",fg="RED")
lab1.config(font=("Courier",44))
lab1.pack()

#WEBTECH

def registerstudent():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Register Student") 
    lab31=Label(top3,text="Register Student",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()
    
    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=100)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=100)
    
    lab33=Label(top3,text="Name")
    lab33.place(x=100,y=150)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=150)
    
    lab34=Label(top3,text="Course")
    lab34.place(x=100,y=200)
    E34=Tkinter.Entry(top3,bd=2)
    E34.place(x=325,y=200)
 
    lab35=Label(top3,text="Mobile Number")
    lab35.place(x=100,y=250)
    E35=Tkinter.Entry(top3,bd=2)
    E35.place(x=325,y=250)

    lab36=Label(top3,text="Course Fees")
    lab36.place(x=100,y=300)
    E36=Tkinter.Entry(top3,bd=2)
    E36.place(x=325,y=300)
    
    lab37=Label(top3,text="Fees Paid")
    lab37.place(x=100,y=350)
    E37=Tkinter.Entry(top3,bd=2)
    E37.place(x=325,y=350)    

    def sub11():
        roll_no= E32.get()
        name= E33.get()
        course= E34.get()
        amount= E36.get()
        amt= E37.get()
        mob= E35.get()
        try:
            cursor.execute("insert into Web_Tech (roll,name,course,totalfees,mob,feespaid) values('%s','%s','%s','%s','%s','%s');" %(roll_no,name,course,amount,mob,amt))
            db.commit()
            sublab=Label(top3,text="Succesfully Registered",fg="GREEN")
            sublab.place(x=100,y=550)
            
        except Exception as e:
            sublab=Label(top3,text="Could not be Registered:'%s'" %(e),fg="RED")
            sublab.place(x=100,y=550)
            db.rollback()

    def exit():
        top3.destroy()
    
    
    busub1=Tkinter.Button(top3,text="Submit",command=sub11,height=2,width=10)
    busub1.place(x=100,y=450)

    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=450)



    

def depositfees():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Deposit Fees") 
    lab31=Label(top3,text="Deposit Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    lab33=Label(top3,text="Money")
    lab33.place(x=100,y=300)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=300)

    def view():
        try:
            cursor.execute("select feespaid from web_tech where roll='%s'"%(E32.get()))
            data=cursor.fetchall()
            tup=data[0]
            add=tup[0]+ int(E33.get())
            cursor.execute("update web_tech set feespaid='%d' where roll='%s'"%(add,E32.get()))
            labv=Label(top3,text="Successfully Updated")
            labv.place(x=100,y=550)
            db.commit()

        except Exception as e:
            labv=Label(top3,text="Could not be Updated: '%s'"%(e))
            labv.place(x=100,y=550)
            db.rollback()
            

    def exit():
        top3.destroy()
            

    busub1=Tkinter.Button(top3,text="Deposit",command=view,height=2,width=10)
    busub1.place(x=100,y=400)
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=400)

def balfees():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Balance Fees") 
    lab31=Label(top3,text="Check Balance Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        roll_no=E32.get()
        
        try:
            cursor.execute("select feespaid from Web_Tech where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]
            cursor.execute("select totalfees from Web_Tech where roll='%s'" %(roll_no))
            data1=cursor.fetchall()
            tup1=data1[0]
            labview=Label(top3,text="Remaining Fees to be paid: '%d'"%(tup1[0]-tup[0]),fg="RED")
            labview.config(font=("TIMES NEW ROMAN",16))
            labview.place(x=100,y=400)
        except Exception as e:
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

def studentdata():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from Web_Tech where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    

    

    
    

    
def webtechman1():    
    top1.destroy()
    global top2
    top2=Tkinter.Tk()
    top2.geometry("600x700")
    lab21=Label(top2,text="Welcome Manager")
    lab21.config(font=("TIMES NEW ROMAN",22))
    lab21.pack()
    bu11=Tkinter.Button(top2,text="Register Student",command=registerstudent,height=5,width=50)
    bu11.place(x=100,y=100)
    bu22=Tkinter.Button(top2,text="Deposit Fees",command=depositfees,height=5,width=50)
    bu22.place(x=100,y=250)
    bu33=Tkinter.Button(top2,text="Balance Fees",command=balfees,height=5,width=50)
    bu33.place(x=100,y=400)
    bu44=Tkinter.Button(top2,text="Student Data",command=studentdata,height=5,width=50)
    bu44.place(x=100,y=550)
    
    
    
    

def webtechman():
    
    lab11=Label(top1,text="Web Tech Learning Manager Login",fg="BLUE")
    lab11.place(x=100,y=400)
    lab12=Label(top1,text="Username")
    lab12.place(x=100,y=450)
    E12=Entry(top1,bd=1)
    E12.place(x=300,y=450)
    lab13=Label(top1,text="Password")
    lab13.place(x=100,y=480)
    E13=Entry(top1,bd=1,show='*')
    E13.place(x=300,y=480)

    def sub():
        a=E12.get()
        b=E13.get()

        if(a=="apoorv" and b=="1234"):
            lab14=Label(top1,text="Logging In. Redirecting in few seconds...")
            lab14.place(x=100,y=580)
            webtechman1()

        else:
            lab15=Label(top1,text="Invalid Username or Password")
            lab15.place(x=100,y=580)

    submit=Tkinter.Button(top1,text="Submit",command=sub ,height=2,width=10)
    submit.place(x=100,y=520)


def customer():
    top1.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from Web_Tech where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    
    

    
    

def webtech():
    global top1
    top1 = Tkinter.Tk()
    top1.geometry("600x700")
    top1.title("Web Tech Learning")
    lab11=Label(top1,text="Welcome \nWeb Tech Learning Portal")
    lab11.pack()
    bu1=Tkinter.Button(top1,text="Manager",command=webtechman,height=5,width=50)
    bu1.place(x=100,y=100)
    bu2=Tkinter.Button(top1,text="Student",command=customer,height=5,width=50)
    bu2.place(x=100,y=250)
    def info():
        topinfo=Tkinter.Tk()
        topinfo.geometry("600x700")
        topinfo.title("WebTech Info")
        textinfotitle="WebTech Learning"
        textinfo= """Webtech learning- ISO certified Web Education
                    \nacademy founded in 2010 by Surjeet.Now WebTech
                    \nLearning Growing steadily in teaching Web
                    \nDesigning, Digital Marketing,App Development
                    \nand Web Development to students from Indian
                    \nand Abroad. We started from Home Office and
                    \ngrowing ever since with support of our trainers,
                    \nstudents and associates.We are thankful to
                    \neveryone.
                    \nwww.webtechlearning.com"""
        info2=Label(topinfo,text=textinfotitle,fg="BLUE")
        info2.config(font=("Caliber",18))
        info2.pack()


        info1=Label(topinfo,text= textinfo)
        info1.config(font=("Caliber",16))
        info1.place(x=50,y=100)
    buinfo=Tkinter.Button(top1,text="About",command=info,height=2,width=10)
    buinfo.place(x=100,y=50)

#WEBTECH

#CIIM

def registerstudent1():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Register Student") 
    lab31=Label(top3,text="Register Student",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()
    
    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=100)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=100)
    
    lab33=Label(top3,text="Name")
    lab33.place(x=100,y=150)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=150)
    
    lab34=Label(top3,text="Course")
    lab34.place(x=100,y=200)
    E34=Tkinter.Entry(top3,bd=2)
    E34.place(x=325,y=200)
 
    lab35=Label(top3,text="Mobile Number")
    lab35.place(x=100,y=250)
    E35=Tkinter.Entry(top3,bd=2)
    E35.place(x=325,y=250)

    lab36=Label(top3,text="Course Fees")
    lab36.place(x=100,y=300)
    E36=Tkinter.Entry(top3,bd=2)
    E36.place(x=325,y=300)
    
    lab37=Label(top3,text="Fees Paid")
    lab37.place(x=100,y=350)
    E37=Tkinter.Entry(top3,bd=2)
    E37.place(x=325,y=350)    

    def sub11():
        roll_no= E32.get()
        name= E33.get()
        course= E34.get()
        amount= E36.get()
        amt= E37.get()
        mob= E35.get()
        try:
            cursor.execute("insert into ciim (roll,name,course,totalfees,mob,feespaid) values('%s','%s','%s','%s','%s','%s');" %(roll_no,name,course,amount,mob,amt))
            db.commit()
            sublab=Label(top3,text="Succesfully Registered",fg="GREEN")
            sublab.place(x=100,y=550)
            
        except Exception as e:
            sublab=Label(top3,text="Could not be Registered:'%s'" %(e),fg="RED")
            sublab.place(x=100,y=550)
            db.rollback()

    def exit():
        top3.destroy()
    
    
    busub1=Tkinter.Button(top3,text="Submit",command=sub11,height=2,width=10)
    busub1.place(x=100,y=450)

    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=450)



    

def depositfees1():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Deposit Fees") 
    lab31=Label(top3,text="Deposit Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    lab33=Label(top3,text="Money")
    lab33.place(x=100,y=300)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=300)

    def view():
        try:
            cursor.execute("select feespaid from ciim where roll='%s'"%(E32.get()))
            data=cursor.fetchall()
            tup=data[0]
            add=tup[0]+ int(E33.get())
            cursor.execute("update ciim set feespaid='%d' where roll='%s'"%(add,E32.get()))
            labv=Label(top3,text="Successfully Updated")
            labv.place(x=100,y=550)
            db.commit()

        except Exception as e:
            labv=Label(top3,text="Could not be Updated: '%s'"%(e))
            labv.place(x=100,y=550)
            db.rollback()
            

    def exit():
        top3.destroy()
            

    busub1=Tkinter.Button(top3,text="Deposit",command=view,height=2,width=10)
    busub1.place(x=100,y=400)
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=400)

def balfees1():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Balance Fees") 
    lab31=Label(top3,text="Check Balance Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        roll_no=E32.get()
        
        try:
            cursor.execute("select feespaid from ciim where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]
            cursor.execute("select totalfees from ciim where roll='%s'" %(roll_no))
            data1=cursor.fetchall()
            tup1=data1[0]
            labview=Label(top3,text="Remaining Fees to be paid: '%d'"%(tup1[0]-tup[0]),fg="RED")
            labview.config(font=("TIMES NEW ROMAN",16))
            labview.place(x=100,y=400)
        except Exception as e:
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

def studentdata1():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from ciim where roll='%s';" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    

    

    


    
def ciimman1():    
    top1.destroy()
    global top2
    top2=Tkinter.Tk()
    top2.geometry("600x700")
    lab21=Label(top2,text="Welcome Manager")
    lab21.config(font=("TIMES NEW ROMAN",22))
    lab21.pack()
    bu11=Tkinter.Button(top2,text="Register Student",command=registerstudent1,height=5,width=50)
    bu11.place(x=100,y=100)
    bu22=Tkinter.Button(top2,text="Deposit Fees",command=depositfees1,height=5,width=50)
    bu22.place(x=100,y=250)
    bu33=Tkinter.Button(top2,text="Balance Fees",command=balfees1,height=5,width=50)
    bu33.place(x=100,y=400)
    bu44=Tkinter.Button(top2,text="Student Data",command=studentdata1,height=5,width=50)
    bu44.place(x=100,y=550)
    
    
    
    

def ciimman():
    
    lab11=Label(top1,text="Cnandigarh Institute of Internet Marketing Login",fg="BLUE")
    lab11.place(x=100,y=400)
    lab12=Label(top1,text="Username")
    lab12.place(x=100,y=450)
    E12=Entry(top1,bd=1)
    E12.place(x=300,y=450)
    lab13=Label(top1,text="Password")
    lab13.place(x=100,y=480)
    E13=Entry(top1,bd=1,show='*')
    E13.place(x=300,y=480)

    def sub():
        a=E12.get()
        b=E13.get()

        if(a=="apoorvciim" and b=="1234"):
            lab14=Label(top1,text="Logging In. Redirecting in few seconds...")
            lab14.place(x=100,y=580)
            ciimman1()

        else:
            lab15=Label(top1,text="Invalid Username or Password")
            lab15.place(x=100,y=580)

    submit=Tkinter.Button(top1,text="Submit",command=sub ,height=2,width=10)
    submit.place(x=100,y=520)


def customerciim():
    top1.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from ciim where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    
    

    
    

def ciim():
    global top1
    top1 = Tkinter.Tk()
    top1.geometry("600x700")
    top1.title("Chandigarh Institute of Internet Marketing")
    lab11=Label(top1,text="Welcome \nChandigarh Institute of Internet Marketing")
    lab11.pack()
    bu1=Tkinter.Button(top1,text="Manager",command=ciimman,height=5,width=50)
    bu1.place(x=100,y=100)
    bu2=Tkinter.Button(top1,text="Student",command=customerciim,height=5,width=50)
    bu2.place(x=100,y=250)
    def info():
        topinfo=Tkinter.Tk()
        topinfo.geometry("600x700")
        topinfo.title("Chandigarh Institue of Internet Marketing Info")
        textinfotitle="Chandigarh Institue of Internet Marketing"
        textinfo= """CIIM is professional institute of Digital Marketing
                    \nin Chandigarh, Mohali and Panchkula, Punjab,India.
                    \nWe not only cater our experts services to students,
                    \nbut also provide training to Entrepreneur,Corporate
                    \nand professionals regardless of their field of work
                    \nand experience. Topics covered include Digital
                    \nMarketing,PPC,SEO,Video Marketing,E-mail Marketing,
                    \nDisplay Adds, Affiliate Marketing,ORM,ASO-Mobile &
                    \nanalytics.
                    \nwww.ciim.in"""
        info2=Label(topinfo,text=textinfotitle,fg="BLUE")
        info2.config(font=("Caliber",18))
        info2.pack()


        info1=Label(topinfo,text= textinfo)
        info1.config(font=("Caliber",16))
        info1.place(x=35,y=100)
    buinfo=Tkinter.Button(top1,text="About",command=info,height=2,width=10)
    buinfo.place(x=100,y=50)


    
#CIIM


#CA

def registerstudent2():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Register Student") 
    lab31=Label(top3,text="Register Student",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()
    
    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=100)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=100)
    
    lab33=Label(top3,text="Name")
    lab33.place(x=100,y=150)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=150)
    
    lab34=Label(top3,text="Course")
    lab34.place(x=100,y=200)
    E34=Tkinter.Entry(top3,bd=2)
    E34.place(x=325,y=200)
 
    lab35=Label(top3,text="Mobile Number")
    lab35.place(x=100,y=250)
    E35=Tkinter.Entry(top3,bd=2)
    E35.place(x=325,y=250)

    lab36=Label(top3,text="Course Fees")
    lab36.place(x=100,y=300)
    E36=Tkinter.Entry(top3,bd=2)
    E36.place(x=325,y=300)
    
    lab37=Label(top3,text="Fees Paid")
    lab37.place(x=100,y=350)
    E37=Tkinter.Entry(top3,bd=2)
    E37.place(x=325,y=350)    

    def sub11():
        roll_no= E32.get()
        name= E33.get()
        course= E34.get()
        amount= E36.get()
        amt= E37.get()
        mob= E35.get()
        try:
            cursor.execute("insert into ca (roll,name,course,totalfees,mob,feespaid) values('%s','%s','%s','%s','%s','%s');" %(roll_no,name,course,amount,mob,amt))
            db.commit()
            sublab=Label(top3,text="Succesfully Registered",fg="GREEN")
            sublab.place(x=100,y=550)
            
        except Exception as e:
            sublab=Label(top3,text="Could not be Registered:'%s'" %(e),fg="RED")
            sublab.place(x=100,y=550)
            db.rollback()

    def exit():
        top3.destroy()
    
    
    busub1=Tkinter.Button(top3,text="Submit",command=sub11,height=2,width=10)
    busub1.place(x=100,y=450)

    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=450)



    

def depositfees2():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Deposit Fees") 
    lab31=Label(top3,text="Deposit Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    lab33=Label(top3,text="Money")
    lab33.place(x=100,y=300)
    E33=Tkinter.Entry(top3,bd=2)
    E33.place(x=325,y=300)

    def view():
        try:
            cursor.execute("select feespaid from ca where roll='%s'"%(E32.get()))
            data=cursor.fetchall()
            tup=data[0]
            add=tup[0]+ int(E33.get())
            cursor.execute("update ca set feespaid='%d' where roll='%s'"%(add,E32.get()))
            labv=Label(top3,text="Successfully Updated")
            labv.place(x=100,y=550)
            db.commit()

        except Exception as e:
            labv=Label(top3,text="Could not be Updated: '%s'"%(e))
            labv.place(x=100,y=550)
            db.rollback()
            

    def exit():
        top3.destroy()
            

    busub1=Tkinter.Button(top3,text="Deposit",command=view,height=2,width=10)
    busub1.place(x=100,y=400)
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=400)

def balfees2():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Balance Fees") 
    lab31=Label(top3,text="Check Balance Fees",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        roll_no=E32.get()
        
        try:
            cursor.execute("select feespaid from ca where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]
            cursor.execute("select totalfees from ca where roll='%s'" %(roll_no))
            data1=cursor.fetchall()
            tup1=data1[0]
            labview=Label(top3,text="Remaining Fees to be paid: '%d'"%(tup1[0]-tup[0]),fg="RED")
            labview.config(font=("TIMES NEW ROMAN",16))
            labview.place(x=100,y=400)
        except Exception as e:
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

def studentdata2():
    top2.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from ca where roll='%s';" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    

    

    


    
def caman1():    
    top1.destroy()
    global top2
    top2=Tkinter.Tk()
    top2.geometry("600x700")
    lab21=Label(top2,text="Welcome Manager")
    lab21.config(font=("TIMES NEW ROMAN",22))
    lab21.pack()
    bu11=Tkinter.Button(top2,text="Register Student",command=registerstudent2,height=5,width=50)
    bu11.place(x=100,y=100)
    bu22=Tkinter.Button(top2,text="Deposit Fees",command=depositfees2,height=5,width=50)
    bu22.place(x=100,y=250)
    bu33=Tkinter.Button(top2,text="Balance Fees",command=balfees2,height=5,width=50)
    bu33.place(x=100,y=400)
    bu44=Tkinter.Button(top2,text="Student Data",command=studentdata2,height=5,width=50)
    bu44.place(x=100,y=550)
    
    
    
    

def caman():
    
    lab11=Label(top1,text="Cnandigarh Academy Login",fg="BLUE")
    lab11.place(x=100,y=400)
    lab12=Label(top1,text="Username")
    lab12.place(x=100,y=450)
    E12=Entry(top1,bd=1)
    E12.place(x=300,y=450)
    lab13=Label(top1,text="Password")
    lab13.place(x=100,y=480)
    E13=Entry(top1,bd=1,show='*')
    E13.place(x=300,y=480)

    def sub():
        a=E12.get()
        b=E13.get()

        if(a=="apoorvca" and b=="1234"):
            lab14=Label(top1,text="Logging In. Redirecting in few seconds...")
            lab14.place(x=100,y=580)
            caman1()

        else:
            lab15=Label(top1,text="Invalid Username or Password")
            lab15.place(x=100,y=580)

    submit=Tkinter.Button(top1,text="Submit",command=sub ,height=2,width=10)
    submit.place(x=100,y=520)


def customerca():
    top1.destroy()
    top3=Tkinter.Tk()
    top3.geometry("600x700")
    top3.title("Student Data") 
    lab31=Label(top3,text="Student Data",fg="RED")
    lab31.config(font=("TIMES NEW ROMAN",22))
    lab31.pack()

    lab32=Label(top3,text="Roll No")
    lab32.place(x=100,y=200)
    E32=Tkinter.Entry(top3,bd=2)
    E32.place(x=325,y=200)

    def exit():
        top3.destroy()

    def view():
        
        try:
            top4=Tkinter.Tk()
            top4.geometry("600x700")
            top4.title("Student Data")
            lab41=Label(top4,text="Student Data")
            lab41.pack()
            roll_no=E32.get()

            cursor.execute("select * from ca where roll='%s'" %(roll_no))
            data=cursor.fetchall()
            tup=data[0]

            lab411=Label(top4,text="Name",fg="BLUE")
            lab411.place(x=100,y=100)
            lab412=Label(top4,text="Roll No",fg="BLUE")
            lab412.place(x=100,y=150)
            lab413=Label(top4,text="Course",fg="BLUE")
            lab413.place(x=100,y=200)
            lab414=Label(top4,text="Mobile No.",fg="BLUE")
            lab414.place(x=100,y=250)
            lab415=Label(top4,text="Course Fees",fg="BLUE")
            lab415.place(x=100,y=300)
            lab416=Label(top4,text="Fees Paid",fg="BLUE")
            lab416.place(x=100,y=350)

            lab421=Label(top4,text='%s'%(tup[0]))
            lab421.place(x=300,y=100)
            lab422=Label(top4,text='%s'%(tup[1]))
            lab422.place(x=300,y=150)
            lab423=Label(top4,text='%s'%(tup[2]))
            lab423.place(x=300,y=200)
            lab424=Label(top4,text='%s'%(tup[3]))
            lab424.place(x=300,y=250)
            lab425=Label(top4,text='%s'%(tup[4]))
            lab425.place(x=300,y=300)
            lab426=Label(top4,text='%s'%(tup[5]))
            lab426.place(x=300,y=350)
            
        except Exception as e:
            top4.destroy()
            labview=Label(top3,text="ERROR: '%s'"%(e),fg="RED")
            labview.place(x=100,y=400)
            db.rollback()
        

    busub1=Tkinter.Button(top3,text="View",command=view,height=2,width=10)
    busub1.place(x=100,y=300)
    
    busub2=Tkinter.Button(top3,text="Exit",command=exit,height=2,width=10)
    busub2.place(x=350,y=300)

    
    

    
    

def ca():
    global top1
    top1 = Tkinter.Tk()
    top1.geometry("600x700")
    top1.title("Chandigarh Academy")
    lab11=Label(top1,text="Welcome \nChandigarh Academy")
    lab11.pack()
    bu1=Tkinter.Button(top1,text="Manager",command=caman,height=5,width=50)
    bu1.place(x=100,y=100)
    bu2=Tkinter.Button(top1,text="Student",command=customerca,height=5,width=50)
    bu2.place(x=100,y=250)
    def info():
        topinfo=Tkinter.Tk()
        topinfo.geometry("600x700")
        topinfo.title("Chandigarh Academy Info")
        textinfotitle="Chandigarh Academy"
        textinfo= """Get the best Coaching to crack NDA, AFCAT, CDS,
                    \nSSB, MERCHANT Navy, Sainik School Exams,
                    \nPolice Exams. We make sure your needs are
                    \nAlways met efficiently. Excellent in innovative
                    \nshort tricks that help the students get selected
                    \nwith targeted preparation in minimum amount of
                    \ntime.
                    \nwww.chandigarhacademy.com"""
        info2=Label(topinfo,text=textinfotitle,fg="BLUE")
        info2.config(font=("Caliber",18))
        info2.pack()


        info1=Label(topinfo,text= textinfo)
        info1.config(font=("Caliber",16))
        info1.place(x=50,y=100)
    buinfo=Tkinter.Button(top1,text="About",command=info,height=2,width=10)
    buinfo.place(x=100,y=50)

#CA

button1=Tkinter.Button(top,text="WebTech Learning",command=webtech,height=5,width=50)
button1.place(x=100,y=150)
button2=Tkinter.Button(top,text="Chandigarh Institute of Internet Marketing",command=ciim,height=5,width=50)
button2.place(x=100,y=350)
button3=Tkinter.Button(top,text="Chandigarh Academy",command=ca,height=5,width=50)
button3.place(x=100,y=550)




top.mainloop()
