portfolio = {
"total_value_inr": 10_000_000, # 1 Crore INR
"monthly_expenses_inr": 80_000,
"assets": [
{"name": "BTC", "allocation_pct": 30, "expected_crash_pct": -80},
{"name": "NIFTY50","allocation_pct": 40, "expected_crash_pct": -40},
{"name": "GOLD", "allocation_pct": 20, "expected_crash_pct": -15},
{"name": "CASH", "allocation_pct": 10, "expected_crash_pct": 0},
]
}

# Write a Python function compute_risk_metrics(portfolio) that returns a dictionary with:
# 1. post_crash_value — total portfolio value after the crash scenario
# 2. runway_months — how many months the post-crash portfolio can cover expenses
# 3. ruin_test — 'PASS' if runway > 12 months, 'FAIL' otherwise
# 4. largest_risk_asset — name of the asset with highest (allocation × crash magnitude)
# 5. concentration_warning — True if any single asset > 40% of portfolio

def compute_risk_metrics(portfolio):
    total_value = portfolio["total_value_inr"]
    monthly_expenses = portfolio["monthly_expenses_inr"]
    
    post_crash_value = 0
    largest_risk = 0
    largest_risk_asset = None
    concentration_warning = False

    for asset in portfolio["assets"]:
        allocation = asset["allocation_pct"]
        crash = asset["expected_crash_pct"]
        
        # 1st value - post crash value
        asset_value = total_value * allocation/100
        crashed_value = crash * asset_value/100
        post_crash_value += crashed_value + asset_value
        
        # 4th value - highest risk asset
        risk = allocation * abs(crash)
        if risk > largest_risk:
            largest_risk = risk
            largest_risk_asset = asset["name"]
        
        # 5th value - concentration value
        if asset["allocation_pct"] > 40:
            concentration_warning = True

    # 2nd value - runway months
    runway_months = post_crash_value / monthly_expenses
    
    # 3rd value - ruin test
    ruin_test = "PASS" if runway_months > 12 else "FAIL"

    return {
        "post_crash_value": post_crash_value,
        "runway_months": runway_months,
        "ruin_test": ruin_test,
        "largest_risk_asset": largest_risk_asset,
        "concentration_warning": concentration_warning
    }

print(compute_risk_metrics(portfolio))