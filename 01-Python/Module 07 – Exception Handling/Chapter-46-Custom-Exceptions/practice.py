class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    
    if(amount > balance):
        raise InsufficientBalanceError("There is no balance")
    
    return balance - amount

try:
    withdraw(1000, 1500)

except InsufficientBalanceError: 
    print("Withdrawal failed")