# Basic
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Print the first row.
# print(matrix[0])
# Print the second row.
# print(matrix[1])
# Print 50.
# print(matrix[1][1])
# Print 90.
# print(matrix[2][2])
# Change 50 to 500.
matrix[1][1] = 500
# Print the updated matrix.
# print(matrix)
# Iterate through every element using nested for loops.
# for row in matrix:
#     for col in row:
#         print(col)
        
# Intermediate Assignment       
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# A flattened list.
flattened_list = [row for row in matrix]
print(flattened_list)
# A list containing only even numbers.
even_list = [ number for row in matrix for number in row if number%2 == 0]
print(even_list)
# A list containing the square of every number.
square_list = [number * number for row in matrix for number in row]
print(square_list)
# A new matrix where every number is doubled.
doubled_matrix = [[number * 2 for number in row] for row in matrix]
print(doubled_matrix)

result = []
for row in range(3):
    roww = []
    for number in range(3):
        print(number)
        roww.append(number)
    result.append(roww)
print(result)

matrix = [
    [1, 2],
    [3, 4]
]

result = []

for row in matrix:
    new_row = []

    for number in row:
        new_row.append(number * 10)

    result.append(new_row)

print(result)

