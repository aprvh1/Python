print "WELCOME TO APARNA COMPLEX"
print
print"1.Manager"
print"2.Customer"
print"3.Exit"
choice=int(input("Select a option : "))

name=[]
cid=[]
bal=[]
while(choice!=3):
    if(choice==1):
        user=raw_input("Enter the username: ")
        passw=raw_input("Enter the password: ")
        if(user== "apoorv" and passw=="12345"):
            print("Welcome manager...")
            print("1.Recharge")
            print("2.Check Balance")
            print("3.Create Customer")
            print("4.Exit")
            choice1=int(input("Select a option : "))

            while(choice1!=4):
                if(choice1==1):
                    print("Recharge")
                    a=input("Enter Customer ID: ")
                    b=input("Enter amount to be added: ")
                    i=0
                    while(i<len(cid)):
                        if(a==cid[i]):
                            bal[i]=bal[i]+b
                        i+=1
                    print("Balance added successfully.")

                    
                elif(choice1==2):
                    print("Check Balance")
                    a=input("Enter Customer ID: ")
                    i=0
                    while(i<len(cid)):
                        if(a==cid[i]):
                            print"Balance: ",bal[i]
                        i+=1
                            
                elif(choice1==3):
                    print("Create Customer")
                    a=raw_input("Enter name: ")
                    b=input("Enter Customer ID: ")
                    c=input("Enter Balance: ")
                    name.append(a)
                    cid.append(b)
                    bal.append(c)
                    print("New customer added successfully.")
                else:
                    print("Wrong Choice.")
                
                print("Welcome manager...")
                print("1.Recharge")
                print("2.Check Balance")
                print("3.Create Customer")
                print("4.Exit")
                choice1=int(input("Select a option : "))

    elif(choice==2):
        print"*****Welcome to FOOD COURT*****"
        print
        print("1.KFC")
        print("2.McDonalds")
        print("3.Dominos")
        print("4.Exit")
        print
        choice2=input("Enter a option: ")
        orderamt=0
        choice4=1
        
        while(choice2!=4 and choice4==1):

            if(choice2==1):
                print("MENU")
                print("1.Smoky grilled wings 15pc. COST:340")
                print("2.Smoky grilled wings 8pc. COST:180")
                print("3.Meal. COST:140")
                choice3=input("Select a order: ")
                if(choice3==1):
                    print("Selected Smoky Grilled Wings 15pc.")
                    orderamt+=340
                elif(choice3==2):
                    print("Selected Smoky grilled wings 8pc.")
                    orderamt+=180
                elif(choice3==3):
                    print("Selected Meal.")
                    orderamt+=140
                else:
                    print "Wrong choice"
                        
            elif(choice2==2):
                print("MENU")
                print("1.Mc Mahraja. COST:140")
                print("2.Fries. COST:60")
                print("3.Mc Meal. COST:180")

                choice3=input("Select a order: ")
                
                if(choice3==1):
                    print("Selected Mc Mahraja.")
                    orderamt+=140
                elif(choice3==2):
                    print("Selected Fries.")
                    orderamt+=60
                elif(choice3==3):
                    print("Mc Meal.")
                    orderamt+=180
                else:
                    print "Wrong choice"


            elif(choice2==3):
                print("MENU")
                print("1.Pepper Paneer Pizza. COST:140")
                print("2.Barbeque Chicken. COST:160")
                print("3.Chicken Peri Peri. COST:180")

                choice3=input("Select a order: ")
                
                if(choice3==1):
                    print("Selected Mc Mahraja.")
                    orderamt+=140
                elif(choice3==2):
                    print("Selected Fries.")
                    orderamt+=160
                elif(choice3==3):
                    print("Mc Meal.")
                    orderamt+=180
                else:
                    print "Wrong choice"


            else:
                print "Wrong Choice"

            print("You want to order something else: ")
            print("1.YES")
            print("2.No")
            choice4=input("Enter your choice: ")

            if(choice4==1):
                print"*****Welcome to FOOD COURT*****"
                print
                print("1.KFC")
                print("2.McDonalds")
                print("3.Dominos")
                print("4.Exit")
                print
                choice2=input("Enter a option: ")

        a=input("Enter Customer ID: ")
        print "Your order total is: ",orderamt
        i=0
        while(i<len(cid)):
            if(a==cid[i]):
                if(orderamt<bal[i]):
                    bal[i]=bal[i]-orderamt*1.055
                    print "Balance Deduction successfully. GST also deducted"
                    print "Remaining Balance: ",bal[i]
                    break
                else:
                    print("Insufficient Balance")
            i+=1
        if(i>=len(cid)):
            print "Customer id not match"
        
        orderamt=0

    else:
        print "Wrong Choice."

        
    print "WELCOME TO APARNA COMPLEX"
    print
    print"1.Manager"
    print"2.Customer"
    print"3.Exit"
    choice=int(input("Select a option : "))
            
