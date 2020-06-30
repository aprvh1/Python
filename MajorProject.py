from Tkinter import*
import Tkinter
import tkMessageBox
import matplotlib.pyplot as plt
import statistics

top=Tkinter.Tk()
top.geometry("720x500")
top.title("National Institute of Technology")
lab01=Label(top, text = "Hazard Identification\nand Risk Analysis in\nMining Industry.\n(Beta Software)",fg="RED")
lab01.config(font=("TIMES NEW ROMAN",44))
lab01.pack()
lab02=Label(top, text = "Made By: Apoorv Harsh(156707 15MN04)")
lab02.place(x=460,y=300)
    
def continuetop():
    top.destroy()
    top1=Tkinter.Tk()
    top1.geometry("720x500")
    top1.title("Data Entry")
    lab11=Label(top1, text = "Enter Fatal and Serious Accident Data")
    lab11.config(font=("TIMES NEW ROMAN",16))
    lab11.pack()

    labfat= Label(top1,text="Fatal",fg="RED")
    labfat.place(x=337,y=30)
    labfat.config(font=("TIMES NEW ROMAN",13))
    labacc= Label(top1,text="No. of Acc.")
    labacc.place(x=275,y=50)
    labinj= Label(top1,text="No. of Inj.")
    labinj.place(x=375,y=50)
            
    labser= Label(top1,text="Serious",fg="BLUE")
    labser.place(x=578,y=30)
    labser.config(font=("TIMES NEW ROMAN",13))
    labacc= Label(top1,text="No. of Acc.")
    labacc.place(x=525,y=50)
    labinj= Label(top1,text="No. of Inj.")
    labinj.place(x=625,y=50)

    #Entry Labels
    labdata1= Label(top1,text="Ground Movements")
    labdata1.place(x=50,y=75)
    labdata2= Label(top1,text="Transportation Machinery\n(Winding in Shaft)",justify=LEFT)
    labdata2.place(x=50,y=100)
    labdata3= Label(top1,text="Transportation Machinery\n(Other than Winding in Shaft)",justify=LEFT)
    labdata3.place(x=50,y=140)
    labdata4= Label(top1,text="Machinery (Other than \nTransportation Machinery)",justify=LEFT)
    labdata4.place(x=50,y=180)
    labdata5= Label(top1,text="Explosives",justify=LEFT)
    labdata5.place(x=50,y=220)
    labdata6= Label(top1,text="Electricity",justify=LEFT)
    labdata6.place(x=50,y=245)
    labdata7= Label(top1,text="Gas,Dust and Other\nCombustible Material",justify=LEFT)
    labdata7.place(x=50,y=270)
    labdata8= Label(top1,text="Fall\n(Other than Ground)",justify=LEFT)
    labdata8.place(x=50,y=310)
    labdata9= Label(top1,text="Other Causes",justify=LEFT)
    labdata9.place(x=50,y=350)    

    #Entry Field Fatal no of accident
    efatalacc1=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc1.place(x=275,y=75)
    efatalacc2=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc2.place(x=275,y=100)
    efatalacc3=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc3.place(x=275,y=140)
    efatalacc4=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc4.place(x=275,y=180)
    efatalacc5=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc5.place(x=275,y=220)
    efatalacc6=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc6.place(x=275,y=245)
    efatalacc7=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc7.place(x=275,y=270)
    efatalacc8=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc8.place(x=275,y=310)
    efatalacc9=Tkinter.Entry(top1,width=10,bd=2)
    efatalacc9.place(x=275,y=350)

    #Entry Field Fatal no of injuries
    efatalinj1=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj1.place(x=375,y=75)
    efatalinj2=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj2.place(x=375,y=100)
    efatalinj3=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj3.place(x=375,y=140)
    efatalinj4=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj4.place(x=375,y=180)
    efatalinj5=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj5.place(x=375,y=220)
    efatalinj6=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj6.place(x=375,y=245)
    efatalinj7=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj7.place(x=375,y=270)
    efatalinj8=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj8.place(x=375,y=310)
    efatalinj9=Tkinter.Entry(top1,width=10,bd=2)
    efatalinj9.place(x=375,y=350)

    #Entry Field Serious no of accident
    eseracc1=Tkinter.Entry(top1,width=10,bd=2)
    eseracc1.place(x=525,y=75)
    eseracc2=Tkinter.Entry(top1,width=10,bd=2)
    eseracc2.place(x=525,y=100)
    eseracc3=Tkinter.Entry(top1,width=10,bd=2)
    eseracc3.place(x=525,y=140)
    eseracc4=Tkinter.Entry(top1,width=10,bd=2)
    eseracc4.place(x=525,y=180)
    eseracc5=Tkinter.Entry(top1,width=10,bd=2)
    eseracc5.place(x=525,y=220)
    eseracc6=Tkinter.Entry(top1,width=10,bd=2)
    eseracc6.place(x=525,y=245)
    eseracc7=Tkinter.Entry(top1,width=10,bd=2)
    eseracc7.place(x=525,y=270)
    eseracc8=Tkinter.Entry(top1,width=10,bd=2)
    eseracc8.place(x=525,y=310)
    eseracc9=Tkinter.Entry(top1,width=10,bd=2)
    eseracc9.place(x=525,y=350)

    #Entry Field Serious no of injuries
    eserinj1=Tkinter.Entry(top1,width=10,bd=2)
    eserinj1.place(x=625,y=75)
    eserinj2=Tkinter.Entry(top1,width=10,bd=2)
    eserinj2.place(x=625,y=100)
    eserinj3=Tkinter.Entry(top1,width=10,bd=2)
    eserinj3.place(x=625,y=140)
    eserinj4=Tkinter.Entry(top1,width=10,bd=2)
    eserinj4.place(x=625,y=180)
    eserinj5=Tkinter.Entry(top1,width=10,bd=2)
    eserinj5.place(x=625,y=220)
    eserinj6=Tkinter.Entry(top1,width=10,bd=2)
    eserinj6.place(x=625,y=245)
    eserinj7=Tkinter.Entry(top1,width=10,bd=2)
    eserinj7.place(x=625,y=270)
    eserinj8=Tkinter.Entry(top1,width=10,bd=2)
    eserinj8.place(x=625,y=310)
    eserinj9=Tkinter.Entry(top1,width=10,bd=2)
    eserinj9.place(x=625,y=350)

    def submit():
        fatalacc=[]
        fatalinj=[]
        seracc=[]
        serinj=[]
        
        fatalacc.append(int(efatalacc1.get()))
        fatalacc.append(int(efatalacc2.get()))
        fatalacc.append(int(efatalacc3.get()))
        fatalacc.append(int(efatalacc4.get()))
        fatalacc.append(int(efatalacc5.get()))
        fatalacc.append(int(efatalacc6.get()))
        fatalacc.append(int(efatalacc7.get()))
        fatalacc.append(int(efatalacc8.get()))
        fatalacc.append(int(efatalacc9.get()))

        fatalinj.append(int(efatalinj1.get()))
        fatalinj.append(int(efatalinj2.get()))
        fatalinj.append(int(efatalinj3.get()))
        fatalinj.append(int(efatalinj4.get()))
        fatalinj.append(int(efatalinj5.get()))
        fatalinj.append(int(efatalinj6.get()))
        fatalinj.append(int(efatalinj7.get()))
        fatalinj.append(int(efatalinj8.get()))
        fatalinj.append(int(efatalinj9.get()))

        seracc.append(int(eseracc1.get()))
        seracc.append(int(eseracc2.get()))
        seracc.append(int(eseracc3.get()))
        seracc.append(int(eseracc4.get()))
        seracc.append(int(eseracc5.get()))
        seracc.append(int(eseracc6.get()))
        seracc.append(int(eseracc7.get()))
        seracc.append(int(eseracc8.get()))
        seracc.append(int(eseracc9.get()))

        serinj.append(int(eserinj1.get()))
        serinj.append(int(eserinj2.get()))
        serinj.append(int(eserinj3.get()))
        serinj.append(int(eserinj4.get()))
        serinj.append(int(eserinj5.get()))
        serinj.append(int(eserinj6.get()))
        serinj.append(int(eserinj7.get()))
        serinj.append(int(eserinj8.get()))
        serinj.append(int(eserinj9.get()))
        
        top1.destroy()
        top2=Tkinter.Tk()
        top2.geometry("720x500")
        top2.title("Data Entry")
        lab20=Label(top2, text = "Manshift Hour and \nNumber of Employees")
        lab20.config(font=("TIMES NEW ROMAN",16))
        lab20.pack()
        lab21= Label(top2, text="Total Manshift Hours: ")
        lab21.place(x=150,y=100)
        ent21=Tkinter.Entry(top2,bd=2)
        ent21.place(x=450,y=100)
        lab22= Label(top2,text="No of Employees")
        lab22.place(x=150,y=200)
        ent22=Tkinter.Entry(top2,bd=2)
        ent22.place(x=450,y=200)

        severity=[]
        frequency=[]

        def submit1():
            manshift=float(ent21.get())
            employee=float(ent22.get())
            for i in range(len(fatalinj)):
                severity.append(((50*fatalacc[i] + seracc[i])  * 100000)/manshift)
                frequency.append(((fatalinj[i]+ serinj [i])*1000)/employee)

            top2.destroy()
            top3=Tkinter.Tk()
            top3.geometry("720x500")
            top3.title("Result 1")
            lab30=Label(top3, text = "Severity and Frequency Result")
            lab30.config(font=("TIMES NEW ROMAN",16))
            lab30.pack()

            labsev= Label(top3,text="Severity",fg="RED")
            labsev.place(x=375,y=40)
            labsev.config(font=("TIMES NEW ROMAN",13))
            
            labfreq= Label(top3,text="Frequency",fg="BLUE")
            labfreq.place(x=475,y=40)
            labfreq.config(font=("TIMES NEW ROMAN",13))

            labdata1= Label(top3,text="Ground Movements")
            labdata1.place(x=150,y=75)
            labsev1= Label(top3,text=str(round(severity[0],6)),fg="RED")
            labsev1.place(x=375,y=75)
            labfreq1= Label(top3,text=str(round(frequency[0],6)),fg="BLUE")
            labfreq1.place(x=475,y=75)
            
            labdata2= Label(top3,text="Transportation Machinery\n(Winding in Shaft)",justify=LEFT)
            labdata2.place(x=150,y=100)
            labsev2= Label(top3,text=str(round(severity[1],6)),fg="RED")
            labsev2.place(x=375,y=100)
            labfreq2= Label(top3,text=str(round(frequency[1],6)),fg="BLUE")
            labfreq2.place(x=475,y=100)

            
            labdata3= Label(top3,text="Transportation Machinery\n(Other than Winding in Shaft)",justify=LEFT)
            labdata3.place(x=150,y=140)
            labsev3= Label(top3,text=str(round(severity[2],6)),fg="RED")
            labsev3.place(x=375,y=140)
            labfreq3= Label(top3,text=str(round(frequency[2],6)),fg="BLUE")
            labfreq3.place(x=475,y=140)
            
            labdata4= Label(top3,text="Machinery (Other than \nTransportation Machinery)",justify=LEFT)
            labdata4.place(x=150,y=180)
            labsev4= Label(top3,text=str(round(severity[3],6)),fg="RED")
            labsev4.place(x=375,y=180)
            labfreq4= Label(top3,text=str(round(frequency[3],6)),fg="BLUE")
            labfreq4.place(x=475,y=180)
            
            labdata5= Label(top3,text="Explosives",justify=LEFT)
            labdata5.place(x=150,y=220)
            labsev5= Label(top3,text=str(round(severity[4],6)),fg="RED")
            labsev5.place(x=375,y=220)
            labfreq5= Label(top3,text=str(round(frequency[4],6)),fg="BLUE")
            labfreq5.place(x=475,y=220)
            
            labdata6= Label(top3,text="Electricity",justify=LEFT)
            labdata6.place(x=150,y=245)
            labsev6= Label(top3,text=str(round(severity[5],6)),fg="RED")
            labsev6.place(x=375,y=245)
            labfreq6= Label(top3,text=str(round(frequency[5],6)),fg="BLUE")
            labfreq6.place(x=475,y=245)
            
            labdata7= Label(top3,text="Gas,Dust and Other\nCombustible Material",justify=LEFT)
            labdata7.place(x=150,y=270)
            labsev7= Label(top3,text=str(round(severity[6],6)),fg="RED")
            labsev7.place(x=375,y=270)
            labfreq7= Label(top3,text=str(round(frequency[6],6)),fg="BLUE")
            labfreq7.place(x=475,y=270)
            
            labdata8= Label(top3,text="Fall\n(Other than Ground)",justify=LEFT)
            labdata8.place(x=150,y=310)
            labsev8= Label(top3,text=str(round(severity[7],6)),fg="RED")
            labsev8.place(x=375,y=310)
            labfreq8= Label(top3,text=str(round(frequency[7],6)),fg="BLUE")
            labfreq8.place(x=475,y=310)
            
            labdata9= Label(top3,text="Other Causes",justify=LEFT)
            labdata9.place(x=150,y=350)
            labsev9= Label(top3,text=str(round(severity[8],6)),fg="RED")
            labsev9.place(x=375,y=350)
            labfreq9= Label(top3,text=str(round(frequency[8],6)),fg="BLUE")
            labfreq9.place(x=475,y=350)

            str1 =""
            str2 =""
            str3 =""
            str4 =""

            sevmed= statistics.mean(severity)
            freqmed= statistics.mean(frequency)

            if ( severity[0] >= sevmed and frequency[0] >= freqmed):
                str1= str1 + "Ground Movements,\n"
            if ( severity[1] >= sevmed and frequency[1] >= freqmed):
                str1= str1 + "Transportation Machinery\n(Winding in Shaft),\n"
            if ( severity[2] >= sevmed and frequency[2] >= freqmed):
                str1= str1 + "Transportation Machinery\n(Other than Winding in Shaft),\n"
            if ( severity[3] >= sevmed and frequency[3] >= freqmed):
                str1= str1 + "Machinery (Other than \nTransportation Machinery),\n"
            if ( severity[4] >= sevmed and frequency[4] >= freqmed):
                str1= str1 + "Explosives,\n"
            if ( severity[5] >= sevmed and frequency[5] >= freqmed):
                str1= str1 + "Electricity,\n"
            if ( severity[6] >= sevmed and frequency[6] >= freqmed):
                str1= str1 + "Gas,Dust and Other\nCombustible Material,\n"
            if ( severity[7] >= sevmed and frequency[7] >= freqmed):
                str1= str1 + "Fall\n(Other than Ground),\n"
            if ( severity[8] >= sevmed and frequency[8] >= freqmed):
                str1= str1 + "Other Causes,\n"

            if ( severity[0] < sevmed and frequency[0] < freqmed):
                str2= str2 + "Ground Movements,\n"
            if ( severity[1] < sevmed and frequency[1] < freqmed):
                str2= str2 + "Transportation Machinery\n(Winding in Shaft),\n"
            if ( severity[2] < sevmed and frequency[2] < freqmed):
                str2= str2 + "Transportation Machinery\n(Other than Winding in Shaft),\n"
            if ( severity[3] < sevmed and frequency[3] < freqmed):
                str2= str2 + "Machinery (Other than \nTransportation Machinery),\n"
            if ( severity[4] < sevmed and frequency[4] < freqmed):
                str2= str2 + "Explosives,\n"
            if ( severity[5] < sevmed and frequency[5] < freqmed):
                str2= str2 + "Electricity,\n"
            if ( severity[6] < sevmed and frequency[6] < freqmed):
                str2= str2 + "Gas,Dust and Other\nCombustible Material,\n"
            if ( severity[7] < sevmed and frequency[7] < freqmed):
                str2= str2 + "Fall\n(Other than Ground),\n"
            if ( severity[8] < sevmed and frequency[8] < freqmed):
                str2= str2 + "Other Causes,\n"

            if ( severity[0] >= sevmed and frequency[0] < freqmed):
                str3= str3 + "Ground Movements,\n"
            if ( severity[1] >= sevmed and frequency[1] < freqmed):
                str3= str3 + "Transportation Machinery\n(Winding in Shaft),\n"
            if ( severity[2] >= sevmed and frequency[2] < freqmed):
                str3= str3 + "Transportation Machinery\n(Other than Winding in Shaft),\n"
            if ( severity[3] >= sevmed and frequency[3] < freqmed):
                str3= str3 + "Machinery (Other than \nTransportation Machinery),\n"
            if ( severity[4] >= sevmed and frequency[4] < freqmed):
                str3= str3 + "Explosives,\n"
            if ( severity[5] >= sevmed and frequency[5] < freqmed):
                str3= str3 + "Electricity,\n"
            if ( severity[6] >= sevmed and frequency[6] < freqmed):
                str3= str3 + "Gas,Dust and Other\nCombustible Material,\n"
            if ( severity[7] >= sevmed and frequency[7] < freqmed):
                str3= str3 + "Fall\n(Other than Ground),\n"
            if ( severity[8] >= sevmed and frequency[8] < freqmed):
                str3= str3 + "Other Causes,\n"

            if ( severity[0] < sevmed and frequency[0] >= freqmed):
                str4= str4 + "Ground Movements,\n"
            if ( severity[1] < sevmed and frequency[1] >= freqmed):
                str4= str4 + "Transportation Machinery\n(Winding in Shaft),\n"
            if ( severity[2] < sevmed and frequency[2] >= freqmed):
                str4= str4 + "Transportation Machinery\n(Other than Winding in Shaft),\n"
            if ( severity[3] < sevmed and frequency[3] >= freqmed):
                str4= str4 + "Machinery (Other than \nTransportation Machinery),\n"
            if ( severity[4] < sevmed and frequency[4] >= freqmed):
                str4= str4 + "Explosives,\n"
            if ( severity[5] < sevmed and frequency[5] >= freqmed):
                str4= str4 + "Electricity,\n"
            if ( severity[6] < sevmed and frequency[6] >= freqmed):
                str4= str4 + "Gas,Dust and Other\nCombustible Material,\n"
            if ( severity[7] < sevmed and frequency[7] >= freqmed):
                str4= str4 + "Fall\n(Other than Ground),\n"
            if ( severity[8] < sevmed and frequency[8] >= freqmed):
                str4= str4 + "Other Causes,\n"

            top4=Tkinter.Tk()
            top4.geometry("720x500")
            top4.title("Risk Analysis Matrix")
            lab40=Label(top4, text = "Risk Analysis Matrix")
            lab40.config(font=("TIMES NEW ROMAN",16))
            lab40.pack()

            lab41=Label(top4, text= str1, height=13,width=30 ,bd=2,bg="RED")
            lab41.place(x=125,y=75)
            lab42=Label(top4, text= str3, height=13,width=30 ,bd=2,bg="YELLOW")
            lab42.place(x=125,y=285)
            lab43=Label(top4, text= str4, height=13,width=30 ,bd=2,bg="YELLOW")
            lab43.place(x=350,y=75)
            lab44=Label(top4, text= str2, height=13,width=30 ,bd=2,bg="GREEN")
            lab44.place(x=350,y=285)

            lab50=Label(top4, text = "High Severity")
            lab50.place(x=125,y=50)
            lab51=Label(top4, text = "Low Severity")
            lab51.place(x=490,y=50)
            lab52=Label(top4, text = "High \nFrequency",justify=LEFT)
            lab52.place(x=50,y=75)
            lab53=Label(top4, text = "Low \nFrequency",justify=LEFT)
            lab53.place(x=50,y=450)
            
            plt.scatter(severity,frequency)
            plt.title("Risk Map\nSeverity-Frequency Graph")
            plt.xlabel("Severity")
            plt.ylabel("Frequency")
            x1=[max(severity),0]
            y1=[0,max(frequency)]
            plt.plot(x1,y1,color="red")
            plt.grid()
            plt.show()
          
        but11=Tkinter.Button(top2,text="Submit",command=submit1,height=2,width=10)
        but11.place(x=325,y=400)              
        
    but01=Tkinter.Button(top1,text="Submit",command= submit,height=2,width=10)
    but01.place(x=325,y=400)

def exittop():
    top.destroy()

but01=Tkinter.Button(top,text="Continue",command= continuetop,height=2,width=10)
but01.place(x=250,y=380)
but02=Tkinter.Button(top,text="Exit",command= exittop,height=2,width=10)
but02.place(x=385,y=380)
top.mainloop()
