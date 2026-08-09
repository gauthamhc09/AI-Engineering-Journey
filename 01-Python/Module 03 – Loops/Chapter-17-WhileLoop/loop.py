# password = input("Please enter password: ")


# while(password != "python123"):
#     print("Wrong password, please try again!")

print("Welcome Spidy!")

# Sum of first five numbers
total = 0
count = 1

while(count<=5):
    print(count, 'count')
    count = count + 1
    total+=count 

print(total)

# Print numbers from 1 to 10 using a while loop.
num=1
while(num<=10):
    print('numbers are', num)
    num=num+1
    
sum=0
number=1
while(number<=100):
    sum+=number
    number=number+1

print(sum)
    
# Reverse the digits of an integer (e.g., 12345 → 54321).
orgNum = [12345]
lenNum = len(orgNum)
reversedNum = []
county = 0
while(lenNum >= county):
    
    reversedNum =reversedNum.append(orgNum(lenNum - 1))
    county=county+1
# result = int("".join(map(str, reversedNum)))
print('result', reversedNum)

    
