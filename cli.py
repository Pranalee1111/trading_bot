import argparse
from client import BinanceClient

def main():
    parser = argparse.ArgumentParser(description="Simple Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    if args.side.upper() not in ["BUY", "SELL"]:
        print("Side must be BUY or SELL")
        return

    if args.type.upper() not in ["MARKET", "LIMIT"]:
        print("Type must be MARKET or LIMIT")
        return

    if args.type.upper() == "LIMIT" and not args.price:
        print("Price is required for LIMIT order")
        return

    try:
        client = BinanceClient()

        print("\n===== ORDER SUMMARY =====")
        print("Symbol:", args.symbol.upper())
        print("Side:", args.side.upper())
        print("Type:", args.type.upper())
        print("Quantity:", args.quantity)
        if args.price:
            print("Price:", args.price)

        response = client.place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )

        print("\n===== ORDER RESPONSE =====")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\nOrder placed successfully!")

    except Exception as e:
        print("Something went wrong:", str(e))

if __name__ == "__main__":
    main()