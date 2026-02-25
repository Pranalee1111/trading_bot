# Binance Futures Testnet Trading Bot

## 📌 Overview

This project is a simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

The application uses a clean structure with separate client and CLI layers, includes input validation, logging, and proper exception handling.

---

## 🚀 Features

- Supports BUY and SELL orders
- Supports MARKET and LIMIT order types
- Command Line Interface using argparse
- Input validation for:
  - Side (BUY/SELL)
  - Order Type (MARKET/LIMIT)
  - Quantity (positive numeric)
  - Price (required for LIMIT, positive numeric)
- Structured code (separate API and CLI layers)
- Logging of:
  - API requests
  - API responses
  - Errors
- Exception handling for invalid input and API failures

---

## 🛠 Requirements

- Python 3.x
- Binance Futures Testnet account
- API Key and Secret

---

## ⚙️ Setup Instructions

1. Clone the repository

2. Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
