a= input ("Enter 1st list: ")
b= input ("Enter 2nd list: ")
print a
print b

i=0
while(i<min(len(a),len(b))):
      a[i]=a[i]+b[i]
      i+=1
print"a+b:"
print a
