print("___OPTIONS___")
print("1.Balance Inquiry")
print("2.Deposit")
print("3.Withdrawal")
print("4.Exit")
print("")

amount = float(input("Enter your initial balance :- "))
option = int(input("Enter option :- "))

if(option==1):
    print("Your initial balance is :- " , amount)

elif(option==2):
    deposit = float(input("Enter the amount of money you want to Deposit :-"))
    amount+=deposit
    print("Your new balance is :- ",amount) 
    

elif(option==3):
    withdrawal = float(input("Enter the amount of money you want to withdrawal :- "))
    if(withdrawal<=amount):
        amount-=withdrawal
        print("Your new balance is :- ",amount)
        
    else:
        print("Withdrawal amount is greater than initial balance")

elif(option==4):
    print("Exiting....")

else:
    print("Enter a valid option")
print("Thankyou")