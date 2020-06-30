class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print "Addition"
        return (self.a+self.b)
    def sub(self):
        print "Substraction"
        return (self.a-self.b)
    def mul(self):
        print "Multiplication"
        return (self.a*self.b)
    def div(self):
        print "Division"
        return (self.a/self.b)
    def mod(self):
        print "Modulus"
        return (self.a%self.b)
    def exp(self):
        print "Exponent Multiplication"
        return (self.a**self.b)
    def expdiv(self):
        print "Exponent Division"
        return (self.a//self.b)


print("*****Calculator*****")
print"1.Addition"
print"2.Substraction"
print"3.Multiplication"
print"4.Division"
print"5.Modulus"
print"6.Exponent Multiplication"
print"7.Exponent Division"
print"8.Exit"


choice=int(input("Enter choice: "))
a=int(input("Enter a: "))
b=int(input("Enter b: "))

while(choice!=8):
    calc1=calc(a,b)
    if choice==1:
        print calc1.add()

    elif choice==2:
        print calc1.sub()

    elif choice==3:
        print calc1.mul()

    elif choice==4:
        print calc1.div()

    elif choice==5:
        print calc1.mod()

    elif choice==6:
        print calc1.exp()

    elif choice==7:
        print calc1.expdiv()

    else:
        print"Wrong Choice"

    print("*****Calculator*****")
    print"1.Addition"
    print"2.Substraction"
    print"3.Multiplication"
    print"4.Division"
    print"5.Modulus"
    print"6.Exponent Multiplication"
    print"7.Exponent Division"
    print"8.Exit"


    choice=int(input("Enter choice: "))
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))























    
