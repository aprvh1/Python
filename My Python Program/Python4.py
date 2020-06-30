a = int(input("Enter a no: "))

i=2;
count=0;

while(i<a//2):
    if(a%i==0):
        count=count+1
    i=i+1
if(count==0):
    print("Prime no")
else:
    print("Not")
