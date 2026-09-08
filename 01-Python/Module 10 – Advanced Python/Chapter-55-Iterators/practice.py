numbers = [10, 20, 30]

iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
    
    
    
numbersTrial = [10, 20, 30, 40]

iterator = iter(numbersTrial)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        print("Stop Iteration")
        break