"""
Task 2: Stock Portfolio Tracker
--------------------------------
- User inputs stock names and quantity.
- Hardcoded dictionary defines stock prices.
- Displays total investment value.
- Optionally saves the result in a .txt or .csv file.
"""

# Hardcoded stock prices 
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

def get_portfolio():
    """Take stock names and quantities from the user."""
    portfolio = {}

    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

    print("\nEnter stock symbol and quantity (type 'done' to finish)")

    while True:
        stock = input("\nStock symbol: ").strip().upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"'{stock}' not found in price list. Try again.")
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    """Calculate total investment and per-stock breakdown."""
    breakdown = []
    total = 0

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        breakdown.append((stock, qty, price, value))

    return breakdown, total


def display_summary(breakdown, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for stock, qty, price, value in breakdown:
        print(f"{stock:<8}{qty:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 45)


def save_to_file(breakdown, total):
    """Optionally save the portfolio summary to a .txt or .csv file."""
    choice = input("\nSave result to file? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        return

    file_format = input("Choose format - txt or csv: ").strip().lower()

    if file_format == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty, price, value in breakdown:
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"TOTAL,,,{total}\n")
    else:
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 45 + "\n")
            for stock, qty, price, value in breakdown:
                f.write(f"{stock:<8}{qty:<8}${price:<9}${value:<9}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total}\n")

    print(f"Saved as {filename}")


def main():
    print("=== Simple Stock Portfolio Tracker ===")
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)
    display_summary(breakdown, total)
    save_to_file(breakdown, total)


if __name__ == "__main__":
    main()
