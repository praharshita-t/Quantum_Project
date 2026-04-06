"""
Feature Engineering Module (features.py)

Input:
- clean_data.csv

Process:
1. Compute daily returns
2. Compute rolling mean (e.g., 5-day, 20-day)
3. Compute rolling volatility (std dev)
4. Normalize or scale values if needed

Output:
- data/processed/features.csv

Format:
Date, Stock, Return, Volatility, Moving_Avg
"""
