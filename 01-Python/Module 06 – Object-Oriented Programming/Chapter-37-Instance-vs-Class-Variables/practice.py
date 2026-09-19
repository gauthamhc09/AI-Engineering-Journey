class Student:
    section = 'B'
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        

student1 = Student('Gautham', 85)
student2 = Student('Rahul', 92)

print(student1.name, student1.marks)
print(student2.name, student2.marks)

class Car:
    wheels = 4

car1 = Car()    
car2 = Car()  

car1.wheels = 6  

Car.wheels = 8

# print(car1.wheels)
# print(car2.wheels)

class Employee:
    company = "TechCorp"

employee1 = Employee()
employee2 = Employee()

employee1.company = "StartupX"

# print(employee1.company) #StartupX
# print(employee2.company) #TechCorp
# print(Employee.company) #TechCorp

class Team:
    players = []
    
team1 = Team()
team2 = Team()

print(team1.players)

team1.players.append("Gautham")

# print(team1.players)
# print(team2.players)

class Product:

    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price
# Laptop → 75000
# Mouse  → 1500
product1 = Product('Laptop', 75000)
product2 = Product('Mouse', 1500)
# Print both product names.
# print(product1.name)
# print(product2.name)
# # Print both prices.
# print(product1.price)
# print(product2.price)
# # Print the category through each object.
# print(product1.category)
# print(product2.category)
# # Print the category through the class.
# print(Product.category)
# # Change the category only for the Laptop to "Computer".
# product1.category = "Computer"
# # Print the category for both products and the class.
# print(product1.category)
# print(product2.category)
# print(Product.category)

class BankAccount:
    bank_name = "ABC Bank"
    total_accounts = 0
    
    def __init__(self, account_holder, balance):
        
        if balance <= 0:
            raise ValueError("Balance cannot be negative")
        
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts+=1
    
    def show_details(self):
        return (f"{self.account_holder} has balance {self.balance} in {self.bank_name}")


bank1 = BankAccount("Gautham", 5000)

# print(bank1.show_details())
BankAccount.bank_name = "Canara"
bank2 = BankAccount("Rahul", 5000)
# print(bank2.show_details())

bank1.bank_name = "Private Bank"

# print(bank1.show_details())
# print(bank2.show_details())
# print(BankAccount.bank_name)

# Each account has its own account_holder.
# Each account has its own balance.
# All accounts can access bank_name.
# BankAccount.total_accounts correctly represents the number of accounts created.
# Change the bank name at the class level.
# Show that all accounts that don't have their own bank_name now see the new bank name.
# Override bank_name for only one account and demonstrate that the other accounts still see the class-level value.

class StockHolding:
    market = "NSE"
    total_holdings = 0
    
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price
        StockHolding.total_holdings+=1
    
    def investment_value(self):
        return self.quantity * self.buy_price
    
    def show_details(self):
        return f"{self.symbol} | BUy Price: {self.buy_price} | Market: {self.market}."
    
stock1 = StockHolding('RELIANCE', 10, 2500)
stock2 = StockHolding('INFY', 20, 1500)
stock3 = StockHolding('TCS', 5, 3500)

StockHolding.market = "BSE"

# print(stock1.show_details())
# print(stock2.show_details())
# print(stock3.show_details())

stock1.market = "NSE"

# print(stock1.show_details())
# print(stock2.show_details())
# print(stock3.show_details())
# print(StockHolding.market)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        if(value <= 0):
            raise ValueError("Invalid Value")
        self._width = value

rectangle = Rectangle(10, 5)


rectangle.width = 20
print(rectangle.__dict__)
print(rectangle.width)
print(rectangle.height)

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self._price = price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
product = Product("Laptop", 75000)

# product.price = -11
# print(product.price)

class StockHolding:
    
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price
        
    @property
    def investment_value(self):
        return self.quantity * self.buy_price
    
stock = StockHolding("RELIANCE", 10, 2500)

# print(stock.investment_value)