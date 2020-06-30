a= input ("Enter 1st list: ")
b= input ("Enter no to be multiplied to array: ")
print a
print b

i=0

while(i< len(a)):
      a[i]=a[i] * b
      i+=1
print"a*",b,":"
print a
