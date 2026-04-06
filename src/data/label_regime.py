"""
Market Regime Labels Module (label_regime.py)

Input:
- features.csv

Process:
1. Aggregate market (average return or use NIFTY)
2. Define:
   - Bull -> sustained positive returns
   - Bear -> sustained negative returns
   - Crisis -> high volatility
3. Assign regime per date

Output:
- data/labels/regimes.csv

Format:
Date, Regime
"""
