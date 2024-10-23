percentage = float(input("Enter your percentage :- "))

if(percentage<=100 and percentage>=90):
    print("Grade A")

elif(percentage<90 and percentage>=80):
    print("Grade B")

elif(percentage<80 and percentage>=70):
    print("Grade C")

elif(percentage<70):
    print("Grade D")

else:
    print("Invalid Input")

print("THANKYOU")