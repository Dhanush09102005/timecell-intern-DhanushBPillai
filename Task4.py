total = 500000

portfolio = {
    "NIFTY50": (50, 30),  # (current percent, target percent)
    "Gold":    (20, 50),
    "Bonds":   (30, 20),
}

for asset, (cur, tgt) in portfolio.items():
    amount = ((tgt - cur) / 100) * total
    action = "BUY" if amount > 0 else "SELL" if amount < 0 else "HOLD"
    print(f"{asset}: {action} Rs. {abs(amount):,.0f}")