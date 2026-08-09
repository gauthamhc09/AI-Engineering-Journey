# pattern A
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# rows=5 , col = same as rows but decreasing
for row in range(5, 0, -1):
    for col in range(row):
        print(row - col, end=" ")
    print()
    
# pattern B
# A
# B C
# D E F
# G H I J
asci_val = 65
for row in range(1, 5):
    for col in range(row):
        print(chr(asci_val), end = " ")
        asci_val+=1    
    print()
# pattern C
# 1
# 2 3
# 4 5 6
# 7 8 9 10
num = 1
for row in range(1, 5):
    for col in range(row):
        print(num, end=" ")
        num+=1
    print()
    
# pattern d
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for row in range(1, 6):
    for col in range(row):
        print(row - col, end=" ")
    print()