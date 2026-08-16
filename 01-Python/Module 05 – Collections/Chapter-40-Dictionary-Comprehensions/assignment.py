# Assignment 1 — Student Profile

student = {
    "name": "Gautham",
    "age": 33,
    "course": "Python",
    "score": 85
}

# Print the name.
print(student["name"])
# Print the score.
print(student["score"])
# Update the score to 90.
student["score"] = 90
# Add "city": "Bengaluru".
student["city"] = "Bengaluru"
# Remove "age".
del student["age"]
# Print the final dictionary.
print(student)


# Assignment 2 — Product
product = {
    "name": "Laptop",
    "price": 75000,
    "brand": "Dell",
    "in_stock": True
}
# Check whether "price" exists.
if "price" in product:
    print("Price exists")
# Check whether "discount" exists.
if "discount" not in product:
    print("Discount not in product")
# Use .get() to retrieve "discount" with a default of 0.
discount_val = product.get("discount", 0)
print(discount_val)
# Update the price to 70000.
product["price"] = 70000
# Add "discount": 5000
product["discount"] = 5000

employees = [
    {"name": "Anita", "department": "AI", "salary": 1200000},
    {"name": "Rahul", "department": "Backend", "salary": 1000000},
    {"name": "Priya", "department": "Finance", "salary": 90000000},
    {"name": "Vikram", "department": "AI", "salary": 1400000}
]

# Print every employee's name.
for employee in employees:
    print(employee["name"])
# Print every employee's name and department.
for employee in employees:
    print(employee["name"], '-' ,employee["department"])
# Print employees whose salary is greater than 1000000.
for employee in employees:
    if employee["salary"] > 1000000:
        print(employee["name"])
# Calculate the total salary of all employees.
total_Salary = 0
for employee in employees:
    total_Salary+=employee["salary"]
print(total_Salary)
# Find the employee with the highest salary.
highest_salary = 0
highest_salary_name = ""
for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_salary_name = employee["name"]
print(highest_salary_name)

holdings = [
    {"symbol": "INFY", "quantity": 20, "price": 1500},
    {"symbol": "TCS", "quantity": 10, "price": 3500},
    {"symbol": "RELIANCE", "quantity": 15, "price": 2800},
    {"symbol": "ITC", "quantity": 50, "price": 500}
]

# value = quantity × price

for holding in holdings:
    holding["value"] = holding["quantity"] * holding["price"]


portfolio = {
    "investor": "Gautham",
    "holdings": [
        {"symbol": "INFY", "quantity": 20, "price": 1500},
        {"symbol": "TCS", "quantity": 10, "price": 3500},
        {"symbol": "RELIANCE", "quantity": 15, "price": 2800},
        {"symbol": "ITC", "quantity": 50, "price": 500}
    ]
}

# Write a program that:

# Prints the investor name.
print(portfolio["investor"])
# Calculates the value of each holding.
portfolio_holdings = portfolio["holdings"]
for holding in portfolio_holdings:
    value = holding["price"] * holding["quantity"]
    holding["value"] = value
    print(holding["symbol"], '-', value)
# Calculates the total portfolio value.
total_portfolio_value = 0
for holding in portfolio_holdings:
    total_portfolio_value+=holding["value"]
print(total_portfolio_value)
# Finds the holding with the highest value.
highest_value_holding = {}
temp_highest = 0
for holding in portfolio_holdings:
    if holding["value"] > temp_highest:
        temp_highest = holding["value"]
        highest_value_holding = holding.copy()
print(highest_value_holding)
# Prints stocks whose value is greater than 30000.
for holding in portfolio_holdings:
    if holding["value"] > 30000:
        print(holding["symbol"])


students = [
    {
        "name": "Anita",
        "marks": {
            "python": 90,
            "sql": 85,
            "math": 88
        }
    },
    {
        "name": "Rahul",
        "marks": {
            "python": 75,
            "sql": 80,
            "math": 70
        }
    },
    {
        "name": "Priya",
        "marks": {
            "python": 95,
            "sql": 92,
            "math": 90
        }
    }
]

# Print each student's name.
for student in students:
    print(student["name"])
    
# Print each student's Python mark.
for student in students:
    print(student["marks"]["python"])
# Calculate each student's average mark.
for student in students:
    total_marks = 0
    for key, value in student["marks"].items():
        total_marks+=value
    student["avg_mark"] = round(total_marks / 3, 2)
    
# Print students whose average is greater than 85.
for student in students:
    if student["avg_mark"] > 85:
        print(student["name"])
# Find the student with the highest average.
highest_avg = 0
highest_avg_stud = ""
for student in students:
    student_avg = student["avg_mark"]
    if student_avg > highest_avg:
        highest_avg = student["avg_mark"]
        highest_avg_stud = student["name"]
        
portfolio = {
    "investor": "Gautham",
    "holdings": [
        {
            "symbol": "INFY",
            "quantity": 20,
            "buy_price": 1400,
            "current_price": 1500
        },
        {
            "symbol": "TCS",
            "quantity": 10,
            "buy_price": 3200,
            "current_price": 3500
        },
        {
            "symbol": "RELIANCE",
            "quantity": 15,
            "buy_price": 2900,
            "current_price": 2800
        },
        {
            "symbol": "ITC",
            "quantity": 50,
            "buy_price": 450,
            "current_price": 500
        }
    ]
}
# add the below one
# invested_value = quantity × buy_price
# current_value = quantity × current_price
# pnl = current_value - invested_value

portfolio_holdings = portfolio["holdings"]
for holding in portfolio_holdings:
    holding["invested_value"] = holding["quantity"] * holding["buy_price"]
    holding["current_value"] = holding["quantity"] * holding["current_price"]
    holding["pnl"] = holding["current_value"] - holding["invested_value"]

# Then calculate:

# Total invested value.
total_invested = 0
for holding in portfolio_holdings:
    total_invested+=holding["invested_value"]
# Total current value.
total_current = 0
for holding in portfolio_holdings:
    total_current+=holding["current_value"]
# Total P&L.
total_pnl = 0
for holding in portfolio_holdings:
    total_pnl+=holding["pnl"]
# Most profitable stock.
temp_profit = 0
profit_stock = ""
for holding in portfolio_holdings:
    profit = holding["pnl"]
    if profit > temp_profit:
        temp_profit = profit
        profit_stock = holding["symbol"]
# Stock with the biggest loss.
temp_loss = portfolio_holdings[0]["pnl"]
loss_stock = ""
for holding in portfolio_holdings:
    loss = holding["pnl"]
    if loss < temp_loss:
        temp_loss = loss
        loss_stock = holding["symbol"]
print(loss_stock)
# Stocks currently in profit.
profit_stocks = []
for holding in portfolio_holdings:
    if holding["pnl"] > 0:
        profit_stocks.append(holding["symbol"])
print(profit_stocks)
# Stocks currently in loss.
loss_stocks = []
for holding in portfolio_holdings:
    if holding["pnl"] < 0:
        loss_stocks.append(holding["symbol"])
print(loss_stocks)

# Create a dictionary using comprehension:

# pnl_by_stock = {
#     "INFY": ...,
#     "TCS": ...,
#     ...
# }

pnl_by_stock = {holding["symbol"]: holding["pnl"] for holding in portfolio_holdings}

print(pnl_by_stock)