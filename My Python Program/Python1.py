a= int(input("Enter a no: "))

rev=0

while(a > 0):
    digit= a % 10
    a = a//10
    rev = rev*10 + digit 

print ( rev )
    
    
