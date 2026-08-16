# Portfolio Data Analyzer
portfolio = {
    "investor": "Gautham",
    "holdings": [
        {
            "symbol": "INFY",
            "sector": "IT",
            "quantity": 20,
            "buy_price": 1400,
            "current_price": 1500
        },
        {
            "symbol": "TCS",
            "sector": "IT",
            "quantity": 10,
            "buy_price": 3200,
            "current_price": 3500
        },
        {
            "symbol": "RELIANCE",
            "sector": "Energy",
            "quantity": 15,
            "buy_price": 2900,
            "current_price": 2800
        },
        {
            "symbol": "ITC",
            "sector": "FMCG",
            "quantity": 50,
            "buy_price": 450,
            "current_price": 500
        },
        {
            "symbol": "HDFCBANK",
            "sector": "Banking",
            "quantity": 25,
            "buy_price": 1500,
            "current_price": 1650
        }
    ]
}
print("Investor:", portfolio["investor"])
# Number of holdings: 5
print("Number of holdings:", len(portfolio["holdings"]))
portoflio_holdings = portfolio["holdings"]
for holding in portoflio_holdings:
    print(holding["symbol"])
# {"IT", "Energy", "FMCG", "Banking"}
unique_stocks = {holding["sector"] for holding in portoflio_holdings}
print(unique_stocks)
# Create a tuple containing the portfolio's first and last stock symbols.
tuple_portfolio = (portoflio_holdings[0]["symbol"], portoflio_holdings[-1]["symbol"])
print(tuple_portfolio)
# invested_value = quantity × buy_price
# current_value = quantity × current_price
# pnl = current_value - invested_value
for holding in portoflio_holdings:
    holding["invested_value"] = holding["quantity"] * holding["buy_price"]
    holding["current_value"] = holding["quantity"] * holding["current_price"]
    holding["pnl"] = holding["current_value"] - holding["invested_value"]

# Total invested value.
total_invested_value = 0
for holding in portoflio_holdings:
    total_invested_value+= holding["invested_value"]
# Total current value.
total_current_value = 0
for holding in portoflio_holdings:
    total_current_value+= holding["current_value"]
# Total P&L.
total_pnl = 0
for holding in portoflio_holdings:
    total_pnl+= holding["pnl"]
print("Total Invested: ", total_invested_value)
print("Current value: ", total_current_value)
print("Total P&L: ", total_pnl)

# Create a list: containing symbols where: pnl > 0
pnl_list = [holding["symbol"] for holding in portoflio_holdings if holding["pnl"] > 0]
print(pnl_list)
# Create a list:  loss_making_stocks = [] where pnl < 0
loss_list = [holding["symbol"] for holding in portoflio_holdings if holding["pnl"] < 0]
print(loss_list)
# Find the best-performing stock based on P&L.
temp_pnl = portoflio_holdings[0]["pnl"]
best_stock = portoflio_holdings[0]["symbol"]
for holding in portoflio_holdings:
    if holding["pnl"] > temp_pnl:
        temp_pnl = holding["pnl"]
        best_stock = holding["symbol"]
print(best_stock)
# Find the worst-performing stock based on P&L.
temp_pnl = portoflio_holdings[0]["pnl"]
worst_stock = portoflio_holdings[0]["symbol"]
for holding in portoflio_holdings:
    if holding["pnl"] < temp_pnl:
        temp_pnl = holding["pnl"]
        worst_stock = holding["symbol"]
    
print(worst_stock)

# list of stock symbols
stock_symbols = [holding["symbol"] for holding in portoflio_holdings]
# set of sectors
sectors_list = {holding["sector"] for holding in portoflio_holdings}
# dict of pnl_by_stock
pnl_by_stock = {}
for holding in portoflio_holdings:
    pnl_by_stock[holding["symbol"]] = holding["pnl"]
print(pnl_by_stock)

pnl_by_stock_comp = {holding["symbol"]:holding["pnl"] for holding in portoflio_holdings}
print(pnl_by_stock_comp)

high_value_stocks = [holding for holding in portoflio_holdings if holding["current_value"] > 30000]
print(high_value_stocks)