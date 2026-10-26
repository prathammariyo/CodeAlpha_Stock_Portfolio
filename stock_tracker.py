"""CodeAlpha Task 2: Stock Portfolio Tracker
Calculates total investment value from manually defined stock prices.
Concepts: dictionary, input/output, arithmetic, file handling.
"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities."""
    portfolio = {}
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' when finished.\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Stock not found. Choose from the list above.")
            continue
        try:
            qty = int(input(f"Quantity of {symbol}: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    return portfolio


def build_report(portfolio):
    """Return report lines and the total investment value."""
    lines = []
    total = 0
    for symbol, qty in portfolio.items():
        value = STOCK_PRICES[symbol] * qty
        total += value
        lines.append(f"{symbol}: {qty} x ${STOCK_PRICES[symbol]} = ${value}")
    lines.append(f"TOTAL INVESTMENT: ${total}")
    return lines


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return

    report = build_report(portfolio)
    print("\n--- Portfolio Summary ---")
    print("\n".join(report))

    if input("\nSave result to file? (y/n): ").strip().lower() == "y":
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(report) + "\n")
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
