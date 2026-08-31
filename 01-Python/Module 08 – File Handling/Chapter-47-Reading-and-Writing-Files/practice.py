def save_portfolio_summary(filename, portfolio_name, value, pnl):
    with open(filename, 'w', encoding="utf-8") as file:
        content = f"{portfolio_name} is having value of {value} and {pnl}"
        file.write(content)

    print("mission successfull")

save_portfolio_summary(
    "portfolio.txt",
    "My Portfolio",
    500000,
    25000
)

import os

# This prints the exact path to the folder where files are being saved
print("Files will be saved in:", os.getcwd())