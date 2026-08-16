# Create this dictionary using a normal for loop first:
sample = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50
}
result = {}

for number in range(1, 6):
    result[number] = number * 10

result_comp = {number: number * 10 for number in range(1,6)}
print(result)
print(result_comp)

numbers = [1, 2, 3, 4, 5]
dict_comp = {number: number * number for number in numbers}
print(dict_comp)

numbers = range(1, 11)
odd_num_comp = {number: number * number for number in numbers if number % 2 != 0}
print(odd_num_comp)

prices = {
    "INFY": 1500,
    "TCS": 3500,
    "RELIANCE": 2800,
    "ITC": 500,
    "HDFC": 1600
}

expensive_stocks = {symb: price for symb, price in prices.items() if price > 1500}

print(expensive_stocks)

response = {
    "status": "success",
    "portfolio": {
        "investor": "Gautham",
        "summary": {
            "invested": 3500000,
            "current_value": 3750000,
            "pnl": 250000
        },
        "holdings": [
            {
                "symbol": "INFY",
                "quantity": 20,
                "value": 30000
            },
            {
                "symbol": "TCS",
                "quantity": 10,
                "value": 35000
            },
            {
                "symbol": "RELIANCE",
                "quantity": 15,
                "value": 42000
            }
        ]
    }
}

# Q1 Print the status.
print(response["status"])
# Q2 Print the investor name.
print(response["portfolio"]["investor"])
# Q3 Print the invested amount.
print(response["portfolio"]["summary"]["invested"])
# Q4 Print the current value.
print(response["portfolio"]["summary"]["current_value"])
# Q5 Print the symbol of the first holding.
print(response["portfolio"]["holdings"][0]["symbol"])
# Q6 Print the value of the second holding.
print(response["portfolio"]["holdings"][1]["value"])
# Q7 Loop through all holdings and print: INFY - 20 TCS - 10 RELIANCE - 15
holdings = response["portfolio"]["holdings"]
for stocks in holdings:
    print(stocks["symbol"], '-', stocks["quantity"])
# Loop through the holdings and print only stocks whose value is greater than 30000.
for stocks in holdings:
    if stocks["value"] > 30000:
        print(stocks["symbol"])
# Create a dictionary called: holding_values
holding_values = {stock["symbol"]: stock["value"] for stock in holdings}
print(holding_values)
# Create a dictionary containing only holdings with value > 30000:
holdings_30000 = {stock["symbol"]: stock["value"] for stock in holdings if stock["value"] > 30000}
print(holdings_30000)