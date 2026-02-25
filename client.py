import os
from binance.client import Client
from dotenv import load_dotenv
from logging_config import setup_logger

load_dotenv()
logger = setup_logger()

class BinanceClient:

    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API credentials not found in .env file")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logger.info(f"Response: {response}")
            return response

        except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise