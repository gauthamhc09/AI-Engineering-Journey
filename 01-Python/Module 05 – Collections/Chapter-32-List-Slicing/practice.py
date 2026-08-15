numbers = [10, 20, 30, 40, 50, 60, 70]
# Create slices for:

# First three elements
print(numbers[:3])
# Last three elements
print(numbers[-3:])
# Elements from index 2 to the end
print(numbers[2:])
# Elements from index 1 through 4 (remember the stop boundary)
print(numbers[1:5])
# Every second element
second_ele = numbers[::2]
print(second_ele, 'sec')
# The entire list using slicing
new_list = numbers[:]
print(new_list)
# A reversed copy
reverse_copy = numbers[::-1]
print(reverse_copy)


numbers1 = [10, 20, 30, 40, 50, 60]
# Predict the output before executing:
# For every slice, explain:

# Start
# Stop
# Step
# Which indexes are selected
print(numbers1[1:5]) # start is 1st index and the stop is 4th index
print(numbers1[:4]) # start from 0 and stops at 3rd index
print(numbers1[3:]) # start from 3rd index and goes till end
print(numbers1[-3:]) # start from last 3rd index and goes till end
print(numbers1[::2]) # returns all element by jumping 2 steps
print(numbers1[1::2]) #starts from 1st index goes till end and skips 2 steps
print(numbers1[::-1]) # reverse the numbers

numbers3 = [10, 20, 30, 40]

part = numbers3[1:3]

part[0] = 999

print(numbers3) # [10, 20, 30, 40] 
print(part) # [999, 30] 
print(numbers3 is part) # False