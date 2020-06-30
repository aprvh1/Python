print("\n*****Welcome to the Apoorv Harsh Hotel*****\n")

print("\n1.Press 1 if you are manager.")
print("2.Press 2 if you are customer.\n3.Exit")

a=int(input())
list1=[]

while(a!=3):
    if(a==1):
        b=int(input("Enter Login ID: "))
        if(b==12345):
            print("\nWelcome\n")
            print("1.Check In\n2.Bill\n3.Exit")
            c=int(input("\nEnter Choice: "))
            while(c==1 or c==2):
                if(c==1):
                    print("\nCheck-In")
                    name=raw_input("Enter customer name: ")
                    Id=int(input("Enter customer ID: "))
                    day=int(input("Enter no of days: "))
                    list1.append([name,Id,day])
                elif(c==2):
                    print("\nBill")
                    Id=int(input("Enter customer ID: "))
                    i=0
                    while(i<len(list1)):
                        list2=list1[i]
                        if(list2[1]==Id):
                            total=list2[2]*1000
                            print("\nTotal amount to be processed: ",total)
                        i+=1
                        
                print("\nWelcome\n")
                print("1.Check In\n2.Bill\n3.Exit")
                c=int(input("\nEnter Choice: "))
                
        else:
            print("Wrong ID")

    elif(a==2):
        b=int(input("Enter Customer Id"))
        i=0
        while(i<len(list1)):
            list2=list1[i]
            if(list2[1]==Id):
                total=list2[2]*1000
                print("\nTotal amount to be processed: ",total)
            i+=1

    else:
        print("Wrong Option.")

    print("*****Welcome to the Apoorv Harsh Hotel*****")

    print("\n1.Press 1 if you are manager.")
    print("2.Press 2 if you are customer.\n3.Exit")

    a=int(input())


    
        
        
