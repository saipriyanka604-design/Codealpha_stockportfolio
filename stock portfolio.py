import json
import os

FILE_NAME = "portfolio.json"


# Load portfolio data
def load_portfolio():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save portfolio data
def save_portfolio(portfolio):
    with open(FILE_NAME, "w") as file:
        json.dump(portfolio, file, indent=4)


# Add a stock
def add_stock(portfolio):
    try:
        name = input("Enter stock name: ").strip().upper()

        if not name:
            print("Stock name cannot be empty.")
            return

        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter purchase price per share: "))
        current_price = float(input("Enter current price per share: "))

        if quantity <= 0 or buy_price <= 0 or current_price < 0:
            print("Please enter valid positive values.")
            return

        stock = {
            "name": name,
            "quantity": quantity,
            "buy_price": buy_price,
            "current_price": current_price
        }

        portfolio.append(stock)
        save_portfolio(portfolio)

        print(f"{name} added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# Display portfolio
def view_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n---------- YOUR STOCK PORTFOLIO ----------")

    for stock in portfolio:
        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]
        profit_loss = current_value - investment

        print(f"\nStock Name: {stock['name']}")
        print(f"Quantity: {stock['quantity']}")
        print(f"Purchase Price: Rs.{stock['buy_price']:.2f}")
        print(f"Current Price: Rs.{stock['current_price']:.2f}")
        print(f"Investment: Rs.{investment:.2f}")
        print(f"Current Value: Rs.{current_value:.2f}")
        print(f"Profit/Loss: Rs.{profit_loss:.2f}")


# Calculate portfolio summary
def portfolio_summary(portfolio):
    total_investment = sum(
        s["quantity"] * s["buy_price"] for s in portfolio
    )

    total_value = sum(
        s["quantity"] * s["current_price"] for s in portfolio
    )

    profit_loss = total_value - total_investment

    print("\n---------- PORTFOLIO SUMMARY ----------")
    print(f"Total Investment: Rs.{total_investment:.2f}")
    print(f"Current Portfolio Value: Rs.{total_value:.2f}")
    print(f"Total Profit/Loss: Rs.{profit_loss:.2f}")


# Update current stock price
def update_stock_price(portfolio):
    name = input("Enter stock name to update: ").strip().upper()

    for stock in portfolio:
        if stock["name"] == name:
            try:
                price = float(input("Enter new current price: "))

                if price < 0:
                    print("Price cannot be negative.")
                    return

                stock["current_price"] = price
                save_portfolio(portfolio)

                print("Stock price updated successfully!")
                return

            except ValueError:
                print("Please enter a valid price.")
                return

    print("Stock not found.")


# Main program
def main():
    portfolio = load_portfolio()

    while True:
        print("\n====== STOCK PORTFOLIO TRACKER ======")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Portfolio Summary")
        print("4. Update Stock Price")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            view_portfolio(portfolio)

        elif choice == "3":
            portfolio_summary(portfolio)

        elif choice == "4":
            update_stock_price(portfolio)

        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()