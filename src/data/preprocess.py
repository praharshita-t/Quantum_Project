"""
Data Cleaning Module (preprocess.py)

Input:
- Multiple CSV files from data/raw/

Process:
1. Read all stock files
2. Standardize column names
3. Convert Date to datetime format
4. Sort by date (ascending)
5. Remove duplicates
6. Handle missing values
7. Add a "Stock" column (from filename)

Output:
- data/processed/clean_data.csv

Format:
Date, Stock, Open, High, Low, Close, Volume
"""
