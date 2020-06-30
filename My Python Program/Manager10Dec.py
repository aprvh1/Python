print("-----Welcome to Apoorv Harsh Corpn.-----")
print("\n1.Manager\n2.Employee\n")

a=int(input("Enter your designation: "))
b=int(input("Enter the login ID: "))
count=0
list1=[]

if(b==12345):
    print("**Welcome Sir**")
    print("\n1.Insert\n2.View the Record\n3.Delete\n4.Exit")
    c=int(input("\nEnter ur choice: "))

    while(c!=4):
        if(c==1):
            print("\nEnter a record.")
            name=raw_input("Enter the name of employee: ")
            Id=int(input("Enter the id of Employee: "))
            sal=int(input("Enter the salary of Employee: "))
            list1.append([name,Id,sal])
            count+=1
        elif(c==2):
            print("\nView record.")
            i=0
            while(i<len(list1)):
                list2=list1[i]
                print"\nEmployee ",i+1,  " Name: ",list2[0]
                print"\nEmployee ",i+1,  " ID: ",list2[1]
                print"\nEmployee ",i+1,  " Salary: ",list2[2]
                print"\n"
                i+=1
        elif(c==3):
            del1=int(input("\nDelete a record.Enter record no (Take first record as 0)"))
            list1.pop(del1)
            count-=1
        else:
            print("Wrong Choice")
        print("\n1.Insert\n2.View the Record\n3.Delete\n4.Exit")
        c=int(input("\nEnter ur choice: "))
        
else:
    print("Wrong ID")
