class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Gautham", 34)
student2 = Student("Rahul", 31)

# print(student1.__dict__)
# print(student2.__dict__)

class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def show_balance(self):
        print(f"{self.account_holder}'s balance is {self.balance}")
        
    def deposit(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance {self.balance}")
        else:
            self.balance-=amount




sbi = BankAccount("Gautham", 10000)
hdfc = BankAccount("Rahul", 50000)

# sbi.show_balance()

# sbi.deposit(2000)
# sbi.withdraw(1000)
# sbi.withdraw(12000)

# sbi.show_balance()

class Rectangle:
    def __init__(self, height, width):
        
        if height <=0 or width <=0:
            raise ValueError("Height and width must be greater than 0")
        
        self.height = height
        self.width = width
        
    def calculate_area(self):
        return self.height * self.width
    

    def show_info(self):
        print(f"The height is {self.height}")
        print(f"The width is {self.width}")
        print(f"The area is {self.calculate_area()}")
        
rect1 = Rectangle(4, 5)
rect1.show_info()
# rect1.width = 10
# rect1.show_info()

class BankAccount:
    
    def __init__(self, account_holder, initial_balance):
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_holder = account_holder
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance+=amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            print("Insufficient balance")
            return
        
        self.balance-=amount
    
    
    def show_balance(self):
        print(f"{self.account_holder} balance is {self.balance}")

canara = BankAccount('Gautham', 10000)
canara.deposit(5000)
canara.withdraw(3000)
canara.show_balance()