import yfinance as yf
from datetime import datetime

def fetch_price(symbol):
    try:
        data = yf.Ticker(symbol)
        price = data.history(period="1d")["Close"].iloc[-1]
        return round(price, 2)
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

assets = {
    "BTC": "BTC-USD",
    "NIFTY50": "^NSEI",
    "GOLD": "GC=F"
}

print("Fetched at: ",datetime.now())
print(f"{'Asset':<10}{'Price':<15}{'Currency'}")

for name, symbol in assets.items():
    price = fetch_price(symbol)

    if price:
        currency = "USD" if "USD" in symbol else "INR"
        print(f"{name:<10}{price:<15}{currency}")