# Print numbers from 1 to 10 using a while loop.
# num=1
# while(num<=10):
#     print(num)
#     num+=1
# # Print numbers from 10 to 1.
# num=10
# while(num>=0):
#     print(num)
#     num-=1
# # Print all even numbers between 1 and 20.
# num=1

# while(num <= 20):
#     if(num%2 == 0):
#         print(num)
#     num+=1
    
    
    
    
# Print all odd numbers between 1 and 20.
# num=1
# while(num <= 20):
#     if(num%2 !=0):
#         print(num)
#     num+=1
# Print the multiplication table of 7 using a while loop.
# num=1
# loop = []
# while(num <= 10):
#     mul = num * 7
#     loop.append(mul)
#     num+=1
# print(loop)


# # Print the Fibonacci sequence up to n terms using a while loop.
n=10
a=0
b=1
fib=[a, b]
while(b<=n):
    c = a + b
    fib.append(c)
    a = b
    b = a + (a-1)

print('fib', fib)

# # Find the sum of numbers from 1 to 100.
# sumofNum = 0
# num=1
# while(num<=100):
#     sumofNum+=num
#     num = num + 1
# print(sumofNum)


# choice = int(input("Choose an option: "))
# while(choice != 5):
#     print("===== Counter Utility =====")
#     match choice:
#         case 1:
#             print("Count Up")
#             exit()
#         case 2:
#             print("Count Down")
#         case 3:
#             print("Print Even Numbers")
#         case 4:
#             print("Print Odd Numbers")
#         case _:
#             print("not a safe option")
            
# print("Exit")