try:
    number = int("hello")

except ValueError as e:
    print(type(e))
    print(e)
    
try:
    x = int("100")
    print(x)
except ValueError:
    print("Invalid number")