numbers = (10, 20, 30, 40, 50)

# Perform:

# Print the tuple.
print(numbers)
# Print the first element.
print(numbers[0])
# Print the last element.
print(numbers[-1])
# Print the length.
print(len(numbers))
# Print the first three elements.
print(numbers[:3])
# Print the tuple in reverse.
print(numbers[::-1])
# Check whether 30 exists.
print(30 in numbers)
# Count how many times 20 appears.
print(numbers.count(20), '20 appears times')
# Find the index of 40.
print(numbers.index(10), 'index of 10 is')

person = ("Gautham", 33, "Developer")
name, age, role = person
print(name)

# swap
a = 10
b = 20
a, b = b, a

stocks = (
    ("TCS", 3500),
    ("INFY", 1800),
    ("ITC", 500)
)

# Using a for loop:
# Print each symbol.
# Print each price.
# Print symbol and price together using tuple unpacking.

for stockName, price in stocks:
    print(stockName, price)
   
def calculate(a, b):
    total = a + b
    difference = a - b
    product = "Doll"
    return total, difference, product 
    
total, difference, product = calculate(10, 5)

portfolio = (
    ("TCS", 100, 350000),
    ("INFY", 50, 90000),
    ("ITC", 200, 100000)
)

# Using tuple unpacking:

# Print every stock symbol.
stock_names = [name for name, qty, invested in portfolio]
print(stock_names)

for stock_sym, qty, invested in portfolio:
    print(stock_sym)
# Print every quantity.
for stock_sym, qty, invested in portfolio:
    print(qty)
# Print every invested value.
for stock_sym, qty, invested in portfolio:
    print(invested)
# Calculate the total invested value.
total_invested = 0
total_qty = 0
for stock_sym, qty, invested in portfolio:
    total_invested+=invested
print(total_invested)
# Calculate the total quantity.
for stock_sym, qty, invested in portfolio:
    total_qty+=qty
print(total_qty)

# Then answer:

# Would you use tuples for a real portfolio application, or would a list of dictionaries be better?
# I will use dictionary as there are muliple return values, it will be diffcult to map, in dict it is easier to maintain on key value pair