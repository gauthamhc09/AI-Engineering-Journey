# pattern1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
    
# # pattern2
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
for row in range(1, 6):
    for col in range(row):
        print(row, end=" ")
    print()

# pattern 3
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
for row in range(5, 0, -1):
    for col in range(5, row - 1, -1):
        print(col, end=" ")
    print()   

# Print a centered pyramid:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
