import random

print "*****Welcome to rolling Dice Game*****"
print "Dice Outcome: " ,random.randint(1,6)

choice=raw_input("Do you want to roll Dice again (Y/N): ")

while(choice=='Y' or choice=='y'):
    print "Dice Outcome: ",random.randint(1,6)
    choice=raw_input("Do you want to roll Dice again (Y/N): ")
    
