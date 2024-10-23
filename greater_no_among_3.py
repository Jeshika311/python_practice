number1 = int(input("Enter number1 :-"))
number2 = int(input("Enter number2 :-"))
number3 = int(input("Enter number3 :-"))

if(number1>number2 and number1>number3):
    print("Number1 is largest of them.")

elif(number2>number1 and number2>number3):
    print("Number2 is largest of them.")

elif(number3>number1 and number3>number2):
    print("Number3 is greatest of them.")

else:
    print("Two or more numbers are equal")