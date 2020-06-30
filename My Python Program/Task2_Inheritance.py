class furniture:
    wood='Teakwood'

class chair(furniture):
    __no_of_legs=0
    def set(self):
        self.__no_of_legs=input("Enter no. of legs: ")
    def printno(self):
        print "No of legs: ",self.__no_of_legs

a=chair()

print "Default wood: ",a.wood
a.set()
choice=raw_input("If you want to change type of wood(y/n): ")

if(choice=='y' or choice=='Y'):
    a.wood=raw_input("Enter type of wood: ")

print
print "Chair details."
print "Chair wood: ",a.wood
a.printno()
