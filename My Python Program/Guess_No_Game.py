import random
a=random.randint(1,10)

no=input("Enter a number (1-10): ")



while(no!=a):
    
    if(no>a):
        print "Entered no is greater."
    elif(no<a):
        print "Entered no is less."
        
    print "Try Again"
    no=input("Enter a number (1-10): ")

print "You have entered correct no. "
print "The no is: ",a

        
