import mysql.connector
import time

db = mysql.connector.connect(host="localhost",database="Institute",user="root",password="12345")
cursor=db.cursor()

def manager1():
    print"*****Welcome to Web_Tech Institute*****"
    use=raw_input("Enter Username: ")
    passw=raw_input("Enter Password: ")

    if(use=="apoorv" and passw=="12345"):
        choice1=1
        while(choice1 != 4):
            print "Welcome Manager."
            print "1.Register New Student"
            print "2.Deposit Fees"
            print "3.Balance Fees to be PAID"
            print "4.Exit"
            choice1=input("Enter your choice: ")
            if(choice1==1):
                print
                print("NEW STUDENT REGISTRATION.")
                roll_no=input("Enter Roll number: ")
                name=raw_input("Enter name:")
                course=raw_input("Enter course: ")
                amount=input("Enter Total Course Fees to be Paid: ")
                amt=input("Enter amount PAID: ")
                mob=raw_input("Enter Mobile number: ")
                try:
                    cursor.execute("insert into Web_Tech (roll,name,course,totalfees,mob,feespaid) values('%d','%s','%s','%d','%s','%d');" %(roll_no,name,course,amount,mob,amt))
                    db.commit()
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()

            elif(choice1==2):
                print
                print("DEPOSIT FEES")
                roll_no=input("Enter Roll number: ")
                amt=input("Enter amount to be deposited: ")
                try:
                    cursor.execute("update Web_Tech set feespaid=feespaid+'%d' where roll='%d'" %(amt,roll_no))
                    db.commit()
                    print "Proceeding Transaction..."
                    time.sleep(3)
                    print "Transaction Successful"
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==3):
                print
                print("Balance Fees to be PAID.")
                roll_no=input("Enter Roll number: ")
                try:
                    cursor.execute("select feespaid from Web_Tech where roll='%d'" %(roll_no))
                    data=cursor.fetchall()
                    tup=data[0]
                    cursor.execute("select totalfees from Web_Tech where roll='%d'" %(roll_no))
                    data1=cursor.fetchall()
                    tup1=data1[0]
                    print "Balance is: ",tup1[0]-tup[0] 
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==4):
                print "You will be exited."

            else:
                print"Wrong Choice"

    else:
        print "Wrong Username or Password"


def customer1():
    print"*****Welcome to Web_Tech Institute*****"
    choice3=1
    while(choice3!=2):
        print"1.Get Information."
        print"2.Exit"
        choice3=input("Enter your choice: ")
        if(choice3==1):
            print
            print("Get Information.")
            roll_no=input("Enter account number: ")
            try:
                cursor.execute("select * from Web_Tech where roll='%d'" %(roll_no))
                data=cursor.fetchall()
                tup=data[0]
                print "Student data is:"
                print "Name: ",tup[0]
                print "Roll No.: ",tup[1]
                print "Course: ",tup[2]
                print "Mobile No.: ",tup[3]
                print "Total Course Fees: ",tup[4]
                print "Fees Paid: ",tup[5]
                print "\n"
            except Exception as e:
                print"Exception is there: ",e
                db.rollback()

        elif(choice3==2):
            print "You will now exit."

        else:
            print "Wrong Choice"


def manager2():
    print"*****Welcome to Chandigarh Institute of Internet Marketing Institute*****"
    use=raw_input("Enter Username: ")
    passw=raw_input("Enter Password: ")

    if(use=="apoorv" and passw=="12345"):
        choice1=1
        while(choice1 != 4):
            print "Welcome Manager."
            print "1.Register New Student"
            print "2.Deposit Fees"
            print "3.Balance Fees to be PAID"
            print "4.Exit"
            choice1=input("Enter your choice: ")
            if(choice1==1):
                print
                print("NEW STUDENT REGISTRATION.")
                roll_no=input("Enter Roll number: ")
                name=raw_input("Enter name:")
                course=raw_input("Enter course: ")
                amount=input("Enter Total Course Fees to be Paid: ")
                amt=input("Enter amount PAID: ")
                mob=raw_input("Enter Mobile number: ")
                try:
                    cursor.execute("insert into CIIM (roll,name,course,totalfees,mob,feespaid) values('%d','%s','%s','%d','%s','%d');" %(roll_no,name,course,amount,mob,amt))
                    db.commit()
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()

            elif(choice1==2):
                print
                print("DEPOSIT FEES")
                roll_no=input("Enter Roll number: ")
                amt=input("Enter amount to be deposited: ")
                try:
                    cursor.execute("update CIIM set feespaid=feespaid+'%d' where roll='%d'" %(amt,roll_no))
                    db.commit()
                    print "Proceeding Transaction..."
                    time.sleep(3)
                    print "Transaction Successful"
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==3):
                print
                print("Balance Fees to be PAID.")
                roll_no=input("Enter Roll number: ")
                try:
                    cursor.execute("select feespaid from CIIM where roll='%d'" %(roll_no))
                    data=cursor.fetchall()
                    tup=data[0]
                    cursor.execute("select totalfees from CIIM where roll='%d'" %(roll_no))
                    data1=cursor.fetchall()
                    tup1=data1[0]
                    print "Balance is: ",tup1[0]-tup[0] 
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==4):
                print "You will be exited."

            else:
                print"Wrong Choice"

    else:
        print "Wrong Username or Password"


def customer2():
    print"*****Welcome to Chandigarh Institute of Internet Marketing Institute*****"
    choice3=1
    while(choice3!=2):
        print"1.Get Information."
        print"2.Exit"
        choice3=input("Enter your choice: ")
        if(choice3==1):
            print
            print("Get Information.")
            roll_no=input("Enter account number: ")
            try:
                cursor.execute("select * from CIIM where roll='%d'" %(roll_no))
                data=cursor.fetchall()
                tup=data[0]
                print "Student data is:"
                print "Name: ",tup[0]
                print "Roll No.: ",tup[1]
                print "Course: ",tup[2]
                print "Mobile No.: ",tup[3]
                print "Total Course Fees: ",tup[4]
                print "Fees Paid: ",tup[5]
                print "\n"
            except Exception as e:
                print"Exception is there: ",e
                db.rollback()

        elif(choice3==2):
            print "You will now exit."

        else:
            print "Wrong Choice"


def manager3():
    print"*****Welcome to Chandigarh Academy*****"
    use=raw_input("Enter Username: ")
    passw=raw_input("Enter Password: ")

    if(use=="apoorv" and passw=="12345"):
        choice1=1
        while(choice1 != 4):
            print "Welcome Manager."
            print "1.Register New Student"
            print "2.Deposit Fees"
            print "3.Balance Fees to be PAID"
            print "4.Exit"
            choice1=input("Enter your choice: ")
            if(choice1==1):
                print
                print("NEW STUDENT REGISTRATION.")
                roll_no=input("Enter Roll number: ")
                name=raw_input("Enter name:")
                course=raw_input("Enter course: ")
                amount=input("Enter Total Course Fees to be Paid: ")
                amt=input("Enter amount PAID: ")
                mob=raw_input("Enter Mobile number: ")
                try:
                    cursor.execute("insert into CA (roll,name,course,totalfees,mob,feespaid) values('%d','%s','%s','%d','%s','%d');" %(roll_no,name,course,amount,mob,amt))
                    db.commit()
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()

            elif(choice1==2):
                print
                print("DEPOSIT FEES")
                roll_no=input("Enter Roll number: ")
                amt=input("Enter amount to be deposited: ")
                try:
                    cursor.execute("update CA set feespaid=feespaid+'%d' where roll='%d'" %(amt,roll_no))
                    db.commit()
                    print "Proceeding Transaction..."
                    time.sleep(3)
                    print "Transaction Successful"
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==3):
                print
                print("Balance Fees to be PAID.")
                roll_no=input("Enter Roll number: ")
                try:
                    cursor.execute("select feespaid from CA where roll='%d'" %(roll_no))
                    data=cursor.fetchall()
                    tup=data[0]
                    cursor.execute("select totalfees from CA where roll='%d'" %(roll_no))
                    data1=cursor.fetchall()
                    tup1=data1[0]
                    print "Balance is: ",tup1[0]-tup[0]    
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==4):
                print "You will be exited."

            else:
                print"Wrong Choice"

    else:
        print "Wrong Username or Password"


def customer3():
    print"*****Welcome to Chandigarh Academy*****"
    choice3=1
    while(choice3!=2):
        print"1.Get Information."
        print"2.Exit"
        choice3=input("Enter your choice: ")
        if(choice3==1):
            print
            print("Get Information.")
            roll_no=input("Enter account number: ")
            try:
                cursor.execute("select * from CA where roll='%d'" %(roll_no))
                data=cursor.fetchall()
                tup=data[0]
                print "Student data is:"
                print "Name: ",tup[0]
                print "Roll No.: ",tup[1]
                print "Course: ",tup[2]
                print "Mobile No.: ",tup[3]
                print "Total Course Fees: ",tup[4]
                print "Fees Paid: ",tup[5]
                print "\n"
            except Exception as e:
                print"Exception is there: ",e
                db.rollback()

        elif(choice3==2):
            print "You will now exit."

        else:
            print "Wrong Choice"




while(1):
    print "Welcome to STUDENT PORTAL"
    print
    print"1.WebTech Learning"
    print"2.Chandigarh Institute of Internet Marketing"
    print"3.Chandigarh Academy"
    print"4.Exit"
    choice=input("Enter your choice: ")
    if(choice==1):
        ch=1
        while(ch!=3):
            print "Web_Tech Learning"
            print "1.Manager"
            print "2.Student"
            print "3.Exit"
            ch=input("Enter your choice: ")
            if(ch==1):
                manager1()
            elif(ch==2):
                customer1()
            elif(ch==3):
                print"Exit..."
            else:
                print"Wrong Choice."
            

    elif(choice==2):
        ch=1
        while(ch!=3):
            print "Chandigarh Institute of Internet Management"
            print "1.Manager"
            print "2.Student"
            print "3.Exit"
            ch=input("Enter your choice: ")
            if(ch==1):
                manager2()
            elif(ch==2):
                customer2()
            elif(ch==3):
                print"Exit..."
            else:
                print"Wrong Choice."
            

    elif(choice==3):
        ch=1
        while(ch!=3):
            print "Chandigarh Academy."
            print "1.Manager"
            print "2.Student"
            print "3.Exit"
            ch=input("Enter your choice: ")
            if(ch==1):
                manager3()
            elif(ch==2):
                customer3()
            elif(ch==3):
                print"Exit..."
            else:
                print"Wrong Choice."
            

    elif(choice==4):
        exit()

    else:
        print"Wrong Choice."
