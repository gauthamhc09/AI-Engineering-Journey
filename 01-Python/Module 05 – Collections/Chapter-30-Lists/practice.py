# Basic

# Create a list containing:

# Five integers
numbers = [1,2,3,4,6]
# Five programming languages
program_languages = ["python", "js", "C", "rust", "java"]
# Five stock symbols

stock_symbols = ["tcs", "infy", "kirloseng", "nestle", "colpal"]

# For each list:

# Print the complete list.
print(numbers, program_languages, stock_symbols)

# Print the first element.
print(program_languages[0])
# Print the last element.
print(program_languages[-1])
# Print the length.
len(numbers)
# Iterate through the list using a for loop.
for stock in stock_symbols:
    print(stock)
    
    
marks = [87, 56, 98, 99, 97]
# Print the marks.
for mark in marks:
    print(mark)
# Print the first mark.
print(marks[0])
# Print the last mark.
print(marks[-1])
# Modify one mark.
marks[0] = 96
# Print the updated list.
print('updated marks', marks)
# Iterate through all marks.
for mark in marks:
    print(mark)
# Print the number of marks.
print(len(marks))