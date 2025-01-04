print("___OPTIONS___\n1.Balance Inquiry\n2.Deposit\n3.Withdrawal\n4.Exit\n ")

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