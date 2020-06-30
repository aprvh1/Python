a= input ("Enter a list: ")
print type(a)

max=a[0]
min=a[0]
i=0

while(i<len(a)):
    if(max<a[i]):
        max=a[i]
    if(min>a[i]):
        min=a[i]
    i+=1

print "Max: ",max
print "Min: ",min
