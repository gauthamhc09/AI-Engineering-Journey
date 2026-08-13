numbers = [10, 20, 30]

other = numbers.copy()

removed = other.pop(1)
print(numbers is other)
print(other == numbers)

# Perform these operations:
numbers = [50, 20, 40, 10, 30]
# Add 60
numbers.append(60)
# Add [70, 80]
numbers.extend([70, 80])
# Insert 5 at the beginning
numbers.insert(0, 5)
# Remove 40
numbers.remove(40)
# Pop the last element
numbers.pop()
# Count the number 20
numbers.count(20)
# Find the index of 30
index_30 = numbers.index(30)
# Sort the list
numbers.sort()
# Reverse the list
numbers.sort(reverse=True)
# Print the final list
print(numbers)

stocks = ["TCS", "INFY", "ITC"]
# Add "RELIANCE"
stocks.append("RELIANCE") # will not return
# Add multiple stocks
stocks.extend(["NESTLE", "COLPAL", "TRITURBINE"]) # will not return
# Insert one stock at a specific position
stocks.insert(1, "HCLTECH") # no return
# Remove one stock by value
stocks.remove("ITC") # no return
# Remove one stock using pop()
stocks.pop(3)  # returns removed value
# Find the index of a stock
index_stock = stocks.index("TCS") # returns the index number
# Count a stock
count_value = stocks.count("RELIANCE")  # returns the counts
# Sort the list
stocks.sort() # no return
# Reverse the list
stocks.sort(reverse=True) # no return

numbers = [5, 2, 8, 2, 1]

a = numbers.append(10)
b = numbers.sort()
c = numbers.pop()

print(numbers) # []
print(a) 
print(b)
print(c)