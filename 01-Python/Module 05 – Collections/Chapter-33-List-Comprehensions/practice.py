matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = []
for row in matrix:
    for number in row:
        result.append(number)
       
# print(result)
numbers = [1, 2, 3, 4, 5, 20]
square = [number * number for number in numbers]

# Convert this loop into a comprehension:
    
result = []
for number in numbers:
    result.append(number * 2)
    
result_new = [number * 2 for number in numbers]
# print(result_new)

# Convert this loop:
result = []

for number in numbers:
    if number > 10:
        result.append(number)
        
result_10 = [number for number in numbers if number > 10]
result_5 = [number for number in numbers if number > 5]
result_boolean = [
    "even" if x % 2 == 0 else "odd"
    for x in numbers
]
# print(result_boolean)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
# Using list comprehensions:

# Create a list containing the squares.
squares = [number * number for number in numbers]
# print(squares)
# Create a list containing the cubes.
cubes = [number * number * number for number in numbers]
# Create a list containing only even numbers.
even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)
# Create a list containing only odd numbers.
odd_numbers = [number for number in numbers if number % 2 != 0]
# print(odd_numbers)
# Create a list containing numbers greater than 5.
greater_5 = [number for number in numbers if number > 5]
# print(greater_5)
# Create a list containing the doubled values of even numbers.
doubled_values_even = [number * number for number in numbers if number % 2 == 0]
# print(doubled_values_even)

stocks = ["tcs", "infy", "itc", "reliance", "nestle"]
# 1. Convert everything to uppercase
upper_case_stocks = [stock.upper() for stock in stocks]
print(upper_case_stocks)
# 2. Create a list containing the length of every stock symbol.
length_stock = [len(stock) for stock in stocks]
print(length_stock)
# 3. Create a list containing only symbols whose length is greater than 3.
length_3 = [stock for stock in stocks if len(stock) > 3]
print(length_3)
# 4. Create a list containing symbols converted to uppercase only if their length is greater than 3.
length_3_uppercase = [stock.upper() for stock in stocks if len(stock) > 3]
print(length_3_uppercase)
# print odd and even
odd_even = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(odd_even)

users = [
    {"name": "Gautham", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Arun", "active": True},
    {"name": "Suresh", "active": False}
]
# extract all names
names = [user["name"] for user in users]
# Extract only active users.
active_users = [user for user in users if user["active"]]
print(active_users)