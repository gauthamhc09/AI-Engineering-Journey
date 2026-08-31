portfolio = {
    "name": "My Portfolio",
    "value": 500000,
    "pnl": 25000,
    "active": True
}

import json

portfolio_json = json.dumps(portfolio)

print(portfolio_json)
print(type(portfolio_json))

data = '{"name": "Gautham", "age": 33}'

result = json.loads(data)

print(type(result))

def save_portfolio(filename, portfolio):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(portfolio, file, indent=4)
    
    
save_portfolio("jsonFile.json", portfolio)