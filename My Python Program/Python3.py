a= int(input("Enter a no: "))
fact=1

if(a==0):
    print("Fact is 1")

if(a==1):
    print("Fact is 1")

else:
    while(a>0):
        fact=fact*a
        a=a-1
    print("Fact is ",fact)
        
