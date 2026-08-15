stocks = {"TCS", "INFY"}

stocks.update(["ITC", "RELIANCE", "HDFCBANK"])

numbers = {10, 20, 30}

value = numbers.pop()

# print(value)
# print(numbers)

unique_stocks = set(stocks)

print(unique_stocks)

a = {1, 2, 3}
b = {3, 4, 5}
# print(b-a)


## Assignment 1 — Basic Set Operations

# Create:
numbers = {10, 20, 30, 40, 50}
# Perform:

# 1. Print the set.
print(numbers)
# 2. Print the length.
print(len(numbers))
# 3. Check whether `30` exists.
print(30 in numbers)
# 4. Check whether `100` exists.
print(100 in numbers)
# 5. Add `60`.
numbers.add(60)
# 6. Add `60` again.
numbers.add(60)

# 7. Remove `20`.
numbers.remove(20)

# 8. Discard `100`.
numbers.discard(100)

# 9. Iterate through the set.
for number in numbers:
    print(number)
# 10. Clear the set.
numbers.clear()

# 11. Print the final set.
print(numbers)
