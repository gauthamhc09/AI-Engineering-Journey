
    
# for row in range(3):

#     for column in range(3):
#         print("*", end=" ")
    
#     print()
    
# Print a 4 × 4 square of *.

for row in range(4):
    for column in range(4):
        print("*", end=" ")
    print()

# Print a 5 × 3 rectangle of #.
for row in range(3):
    for col in range(5):
        print("#", end=" ")
    print()
    
# Print numbers like this:

for row in range(3):
    num = 0
    for col in range(3):
        num+=1
        print(num, end=" ")
    print()

# Print:    
# *
# * *
# * * *
# * * * *
# * * * * *
n=1
for row in range(5):
    for col in range(n):
        print("*", end=" ")
    n+=1
    print()
# Print the inverted version:
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for row in range(5):
    for col in range(n):
        print("*", end=" ")
    n-=1
    print()
    
# Print a multiplication table from 1 to 5.
for row in range(1, 6):
    for col in range(1, 11):
        mul = row * col
        print(f"{row} * {col} = {mul}")
    print()
        