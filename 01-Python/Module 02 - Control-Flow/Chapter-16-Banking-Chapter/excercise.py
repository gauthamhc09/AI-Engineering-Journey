"""============================================================
WELCOME TO PYTHON BANK
============================================================

Username:
gautham

PIN:
1234

Login Successful

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Choose Option:
3

Withdraw Amount:
5000

Withdrawal Successful

Remaining Balance : ₹20000"""

user_name = "gautham"
pin = 1234
balance = 20000

print("=" * 60)
print("WELCOME TO PYTHON BANK")
print("=" * 60)

entered_username = input("Enter username: ")

if user_name == entered_username:
    entered_pin = int(input("Enter pin: "))
    if pin == entered_pin:
        print(f"Login successful! Welcome {user_name}")
    else:
        print("wrong pin, please try again")
        exit()    
else:
    print("Not a valid user! Please try with valid user name")
    exit() 
    
print("1: to Check Balance: ")
print("2: to Check Deposit: ")
print("3: to Withdraw: ")
print("4: to Exit: ")

action = int(input("Please Select the desired actions: "))

match action:
    case 1:
        print(f"Your Balance is {balance}")
    case 2:
        deposit = (int(input("Please enter amount to deposit: ")))
        balance += deposit
        print(f"Updated balance is {balance}")
    case 3:
        withdraw = int(input("Please enter amount to withdraw: "))
        if(withdraw <= 0):
            print("Invalid withdrawal amount")
        elif(withdraw <= balance):
            balance -= withdraw
            print(f"Withdraw is successful, Available Balance : ₹{balance:,.2f}")
        else:
            print(f"You do not have sufficient balance, your balance amount is {balance}")
        another_transaction = (input("Do you want another transaction? "))
        if another_transaction == "yes":
            action = int(input("Please Select the desired actions: "))
        else:
            print("Thank you for Banking with us.")
    case 4:
        print("Successfully Exit")
    case _:
        print("Invalid select")
        
print("Thank you Have a nice day!")





