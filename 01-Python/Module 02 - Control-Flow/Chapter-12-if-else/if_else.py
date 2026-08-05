# ask user for 2 numbers, check which one is bigger
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
if number1 > number2:
    print("number1 is bigger")
else:
    print("number2 is bigger")

# program to check if a person is eligible to vote.
age = int(input(("enter age: ")))

if age >= 18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

# Check whether a number is even or odd.
num = int(input(("enter number: ")))

if num % 2 == 0:
    print('Even number')
else:
    print('Odd number')
    
name = input("Enter name: ")
marks = int(input("Enter marks obtained: "))

if marks >= 35:
    print(f"Congratulations {name}, you have passed")
else:
    print(f"Sorry {name}, you have failed")
    