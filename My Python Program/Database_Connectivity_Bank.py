import mysql.connector
import time
db=mysql.connector.connect(host="localhost",database="Bank",user="root",password="12345")

cursor=db.cursor()

def manager():
    a=raw_input("Enter Username: ")
    b=raw_input("Enter Password: ")

    if(a=="apoorv" and b=="12345"):
        choice1=1
        while(choice1 != 4):
            print "Welcome Manager."
            print "1.Create new account"
            print "2.Deposit Money"
            print "3.Check Balance"
            print "4.Exit"
            choice1=input("Enter your choice: ")
            if(choice1==1):
                print
                print("Create new account.")
                acc_no=input("Enter account number: ")
                name=raw_input("Enter name:")
                city=raw_input("Enter city: ")
                amount=input("Enter amount: ")
                mob=raw_input("Enter mob: ")
                try:
                    cursor.execute("insert into dena_bank(accn,name,city,amount,mob) values('%d','%s','%s','%d','%s')" %(acc_no,name,city,amount,mob))
                    db.commit()
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()

            elif(choice1==2):
                print
                print("Deposit Money")
                acc_no=input("Enter account number: ")
                amount=input("Enter amount to be deposited: ")
                try:
                    cursor.execute("update dena_bank set amount=amount+'%d' where accn='%d'" %(amount,acc_no))
                    db.commit()
                    print "Proceeding Transaction..."
                    time.sleep(5)
                    print "Transaction Successful"
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==3):
                print
                print("Check Balance.")
                acc_no=input("Enter account number: ")
                try:
                    cursor.execute("select amount from dena_bank where accn='%d'" %(acc_no))
                    data=cursor.fetchall()
                    print "Balance is: ",data
                except Exception as e:
                    print"Exception is there: ",e
                    db.rollback()
                    
            elif(choice1==4):
                print "You will be exited."

            else:
                print"Wrong Choice"

    else:
        print "Wrong Username or Password"



def customer():
    print"*****Welcome to Dena Bank*****"
    choice3=1
    while(choice3!=3):
        print"1.Check Balance."
        print"2.Withdraw Money"
        print"3.Exit"
        choice3=input("Enter your choice: ")
        if(choice3==1):
            print
            print("Check Balance.")
            acc_no=input("Enter account number: ")
            try:
                cursor.execute("select amount from dena_bank where accn='%d'" %(acc_no))
                data=cursor.fetchall()
                print "Balance is: ",data
            except Exception as e:
                print"Exception is there: ",e
                db.rollback()

        elif(choice3==2):
            print
            print("Withdraw Money")
            acc_no=input("Enter account number: ")
            amount=input("Enter amount to be withdrawn: ")
            try:
                cursor.execute("update dena_bank set amount=amount-'%d' where accn='%d'" %(amount,acc_no))
                print "Proceeding Transaction..."
                time.sleep(5)
                print "Transaction Successful"
                db.commit()
            except Exception as e:
                print"Exception is there: ",e
                db.rollback()

        elif(choice3==3):
            print "You are not exited."

        else:
            print "Wrong Choice"










while(1):
    print"Welcome to Dena Bank"
    print"1.Manager"
    print"2.Customer"
    print"3.Exit"
    choice=input("Enter your choice: ")
    if(choice==1):
        manager()

    elif(choice==2):
        customer()

    elif(choice==3):
        exit()

    else:
        print"Wrong Choice."
