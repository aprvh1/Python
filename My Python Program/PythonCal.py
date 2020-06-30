print("\nPlease Enter the index to function you want to perform: \n1. Addition\n2. Substraction\n3. Division\n4. Multiplication\n5. Exponent Division\n6. Exponent Multiplication\n7. Exit")
choice=int(input())

while(choice != 7):
    if(choice == 1):
        print("\nAddition\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a+b)

    elif(choice == 2):
        print("\nSubstraction\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a-b)

    elif(choice == 3):
        print("\nDivision\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a/b)

    elif(choice == 4):
        print("\nMultiplication\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a*b)

    elif(choice == 5):
        print("\nExponenet Division\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a//b)

    elif(choice == 6):
        print("\nExponent Multiplication\n")
        a=int(input("Enter First no.: "))
        b=int(input("Enter Second no.: "))
        print (a**b)

    else:
        print ("Please Enter correct choice: \n")
    print("\nPlease Enter the index to function you want to perform: \n1. Addition\n2. Substraction\n3. Division\n4. Multiplication\n5. Exponent Division\n6. Exponent Multiplication\n7. Exit")
    choice=int(input())

