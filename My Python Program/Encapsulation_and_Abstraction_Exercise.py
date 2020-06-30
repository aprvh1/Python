car={'Hatchback':30,'Sedan':50,'SUV':100}

class rental:
    def __init__(self,car):
        self.carlist=car
        
    def view(self):
        for car in self.carlist :
            print "Car: " +car+ "->",self.carlist[car]
            
    def book(self,name):
        if (name in self.carlist):
            self.nod=input("Enter no of days: ")
            return self.carlist[name]*self.nod
        else:
            print "Car not in store."

    def returncar(self,name):
        if (name in self.carlist):
            print("Car can be accepted.")
        else:
            print "Car not of this store."

    def addcar(self,name,costperday):
        self.carlist[name]=costperday
        print "Car added successfully"
        

class customer:
    def book(self):
        self.name=raw_input("Enter car name to be booked: ")
        return self.name
    def returncar(self):
        self.name=raw_input("Enter car name to be returned: ")
        return self.name
    
rent = rental(car)
cust=customer()

while(1):
    print
    print("*****MENU*****")
    print("1.View all vehicle and Cost per Day")
    print("2.Book a vehicle")
    print("3.Return a vehicle")
    print("4.Add vehicle to list (Can only be done by manager)")
    print("5.Exit")
    
    choice=input("Enter a option: ")
    print
    
    if(choice==1):
        rent.view()
                            
    elif(choice==2):
        a=cust.book()
        amt=rent.book(a)
        print "Total fare payable: ",amt
        
    elif(choice==3):
        a=cust.returncar()
        rent.returncar(a)

    elif(choice==4):
        pass1=raw_input("Enter manager's password: ")
        if(pass1=="apoorv"):
            a=raw_input("Enter car name: ")
            b=input("Enter cost per day: ")
            rent.addcar(a,b)
        else:
            print "Password is wrong."
        
    else:
        quit()
    
    
