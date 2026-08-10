def add(a, b):
    return a + b

sum1 = add(3 ,4)
sum2 = add(5 ,4)
sum3 = add(8 ,4)

def full_name(first_name, last_name):
    return first_name, last_name

full_name_result = full_name('gautham', 'chengappa')

print(full_name_result)

def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 9)

print(area1)

# ==========================
# Invoice
# ==========================

# Customer :
# Total :

# Thank You!

def calculate_total(price, quantity):
    return price * quantity


def print_invoice(customer, total):
    print("=" * 30)
    print("Invoice")
    print("=" * 30)
    
    print(f"Customer: {customer}")
    print(f"Total: {total}")
    
    print("Thank you!")

print_invoice("Rahul", calculate_total(30, 2))


def add(a, b):
    print(a + b)

x = add(5, 10)

print(x)