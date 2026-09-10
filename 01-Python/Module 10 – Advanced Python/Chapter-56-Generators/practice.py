def numbers():
    print("Starting")
    yield 1

    print("Continuing")
    yield 2

    print("Finishing")
    yield 3
    
gen = numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# for number in gen:
#     print(number)
    
def infinite_number():
    number = 1
    
    if number == 10:
        return
    while True:
        yield number
        number+=1

genInfy = infinite_number()

# print(next(genInfy))
# print(next(genInfy))
# print(next(genInfy))


def even_numbers(limit):
    number = 0
    listt = []
    
    while number <= limit:
        listt.append(number)
        number+=2
    return listt
        
def gen_even_numbers(limit):
    number = 0
    
    while number<=limit:
        yield number
        number+=2

getEven = gen_even_numbers(10)
# for number in getEven:
#     print(number)
# print(even_numbers(10))

def countdown(n):
    while n > 0:
        yield(n)
        n-=1

count = countdown(5)
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))

def even_numbers_limit(limit):
    for number in range(limit + 1):
        
        if number % 2 == 0:
            yield number
    
# for number in even_numbers_limit(10):
#     print((number))
    
numbers = (x * 2 for x in range(5))
# print(next(numbers))
# print(next(numbers))
total_list = sum([x * 2 for x in range(1_000_000)])
total = sum(x * 2 for x in range(1_000_000))
# print(total_list)
# print(total)

gen = (x for x in range(5))

for number in gen:
    print(number)
    
for number in gen:
    print(number)