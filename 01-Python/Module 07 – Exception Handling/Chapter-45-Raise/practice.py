age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print(e)
    
# try:
#     x = 10 / 0

# except ZeroDivisionError:
#     print("Something went wrong")
#     raise

try:
    raise ValueError("Something is wrong")

except ValueError:
    print("Handled")
    
def withdraw(balance, amount):
    try: 
        if amount > balance:
            print("Insufficient balance")

    except ValueError:
        print(ValueError)
        
    return balance - amount

withdraw(1000, 1500)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Number cannot be divided by zero")
    
    return a/b

divide(10/0)