a=int(input("Enter a no: "))
armno=0
nod=0

temp=a

while(temp>0):
    temp=temp//10
    nod=nod+1


temp =a
digit=0

while(temp>0):
    digit= temp%10
    temp=temp//10
    armno = armno+ digit**nod

if(armno==a):
    print("Armstrong No.")
else:
    print("Not")
    

    
