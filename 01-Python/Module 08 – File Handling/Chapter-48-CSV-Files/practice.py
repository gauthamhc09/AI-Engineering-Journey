# symbol,quantity,price
# RELIANCE,10,2500
# INFY,20,1500
# TCS,5,3500

# total value = quantity × price

import csv

# Prepare data as a list of dictionaries (matches your DictReader preference!)
portfolio_data = [
    {"symbol": "RELIANCE", "quantity": 10, "price": 2500},
    {"symbol": "INFY", "quantity": 20, "price": 1500},
    {"symbol": "TCS", "quantity": 5, "price": 3500}
]

with open("portfolio.csv", 'w', newline="", encoding='utf-8') as file:
    fieldnames = ["symbol", "quantity", "price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(portfolio_data)
    
print("Portoflio created successfully")

def calculate_total_value(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            value = int(row["quantity"]) * float(row["price"])
            total +=value
        return total

total_value = calculate_total_value("portfolio.csv")

print(total_value)