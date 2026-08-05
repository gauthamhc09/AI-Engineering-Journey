"""
Grade Calculator

90+ → A
75+ → B
60+ → C
35+ → D
Below 35 → Fail
"""

grade = int(input("Enter grades: "))

if(grade >= 90):
    print("You have scored Grade A")
elif (grade >=75):
    print("You have scored Grade B")
elif (grade >=60):
    print("You have scored Grade C")
elif (grade >=35):
    print("You have scored Grade D")
else:
    print("You have failed")
    
# employee role
role = "employee"
if(role == "admin"):
    print("you are a admin")
elif(role == "manager"):
    print("you are a manager")
else:
    print("you are an employee")
"""
🏦 Banking Challenge

Ask the user for their account balance.

Display:

Balance ≥ ₹1,00,000 → Premium Customer
Balance ≥ ₹50,000 → Gold Customer
Balance ≥ ₹10,000 → Silver Customer
Otherwise → Regular Customer
"""
balance = int(input("Please provide your balance: "))

if(balance >= 100000):
    print("Premium customer")
elif(balance >=50000):
    print("Gold")
elif(balance>=10000):
    print("Silver customer")
else:
    print("Regular customer")
    
    
    