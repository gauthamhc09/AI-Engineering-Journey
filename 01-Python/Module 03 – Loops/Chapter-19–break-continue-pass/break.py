# Basic

# Print numbers 1 to 10, but stop at 6 using break.
for i in range(1, 11):
    print(i)
    if i==6:
        break
    
# Print numbers 1 to 10, skipping 5 using continue.
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    
# Create an empty function using pass.
def firstFun():
    pass


# Ask the user repeatedly for a password until they enter "python123" using break.
result = False
while True:
    password = input("Please enter the right password: ")
    if password == "python123":
        print("Access granted")
        break
    print("wrong password")
    
# Print numbers from 1 to 20, skipping all multiples of 3.
for i in range(1, 21):
    if i%3 == 0:
        continue
    print(i)
    
# Read a list of numbers and stop when a negative number is found.
listOfNum = [1,2,3,5,4,-1,3]
for num in listOfNum:
    if num<0:
        break
    print(num)