# Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
# Print numbers from 10 to 1.
num = 11
for i in range(10, 0, -1):
    print(i)
# Print all even numbers from 1 to 20.
for i in range(0, 21, 2):
    print(i)
# Print all odd numbers from 1 to 20.
for i in range(1, 21, 2):
    print(i)
# Print the multiplication table of 9.
for i in range(1, 11):
    mul = 9 * i
    print(f"{9} * {i} = {mul}")
    
# Print each character of your name on a new line.
name="gautham"
for char in name:
    print(char)

# Find the sum of numbers from 1 to 100 using a for loop.
total = 0
for i in range(101):
    total+=i
print(total)

# Count how many vowels are in a string.
vowels = ["a", "e", "i", "o", "u"]
stringVal = "gautham"
result = []
for val in stringVal:
    if val in vowels:
        result.append(val)
clean_numbers = list(set(result))
print("The vowel length is ", len(clean_numbers))
    

fruits = ["mango", "apple", "orange"]
for fruit in fruits:
    print(fruit)
