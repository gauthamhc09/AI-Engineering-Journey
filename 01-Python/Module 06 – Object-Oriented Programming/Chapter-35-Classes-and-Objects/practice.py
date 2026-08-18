class Dog:
    sound = "Bark"
    pass

dog1 = Dog
dog2 = Dog

# print(dog1)

# Car class
# car1 object
# car2 object
# Print both objects
# Add one simple class attribute such as wheels = 4
# Access that attribute through both objects

class Car:
    wheels = 4

car1 = Car()
car2 = Car()

car1.brand = "Toyota"
car1.speed = 80
car2.brand = "BMW"
car2.speed = 120

class Dog:
    def bark(self):
        print(f"the address of self inside", {id(self)})

dog1 = Dog()
print(f"the address of self outside", {id(dog1)})

dog1.bark()

class Car:
    def show_info(self):
        print(f"{self.brand} is moving at {self.speed}")

car1 = Car()
car2 = Car()

car1.brand = "Toyota"
car1.speed = 80
car2.brand = "BMW"
car2.speed = 120

# car1.show_info()
# car2.show_info()

class BankAccount:
    
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print(f"Insufficient Balance {self.balance}")
    def show_balance(self):
        print(f"Your balance is {self.balance}")
        
sbi = BankAccount()
sbi.balance = 10000

sbi.deposit(5000)

sbi.withdraw(5000)
sbi.withdraw(5000)
sbi.withdraw(5000)
sbi.withdraw(9000)
sbi.show_balance()
