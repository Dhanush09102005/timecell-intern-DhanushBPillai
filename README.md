# timecell-intern-DhanushBPillai
Assessment tasks for Timecell internship — a set of Python tools for portfolio analysis and management.

---

## Task 1 — Portfolio Risk Metrics
Computes key risk indicators for a portfolio under a crash scenario — including post-crash value, how many months of expenses it can cover, and which asset carries the highest risk. Flags concentration if any single asset exceeds 40% allocation.

## Task 2 — Live Asset Price Fetcher
Fetches real-time prices for BTC, NIFTY50, and Gold using Yahoo Finance. Displays current price and currency for each asset with a timestamp, requiring no API key.

## Task 3 — AI Portfolio Advisor
Uses an LLM (Llama via Groq) to generate a plain-English analysis of a portfolio — risk summary, strengths, suggested improvement, and a final verdict of Aggressive, Balanced, or Conservative.

## Task 4 — Portfolio Rebalancer
Takes current vs target allocation percentages and total portfolio value, then calculates the exact amount to buy, sell, or hold for each asset to get back on target.
