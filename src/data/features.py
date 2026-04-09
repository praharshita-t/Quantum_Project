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

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def process_features(input_path: str, output_path: str):
    """Reads clean data, computes features, normalizes, and saves."""
    if not os.path.exists(input_path):
        print(f"Error: Required input {input_path} not found.")
        return
        
    # Read clean data
    df = pd.read_csv(input_path)
    
    # Ensure Date is datetime and sort by Stock and Date mapping
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by=['Stock', 'Date'], ascending=[True, True], inplace=True)
    
    # --- Step 1: Compute Daily Returns ---
    # return = (close - previous_close) / previous_close
    df['Return'] = df.groupby('Stock')['Close'].pct_change()
    
    # --- Step 2: Clean Returns (VERY IMPORTANT) ---
    # Remove or handle infinite values (division issues) and NaNs
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(subset=["Return"], inplace=True)
    
    # --- Step 3: Compute Features ---
    # Rolling volatility (window = 7)
    df['Volatility'] = df.groupby('Stock')['Return'].transform(lambda x: x.rolling(window=7).std())
    
    # Moving average (window = 7)
    df['Moving_Avg'] = df.groupby('Stock')['Close'].transform(lambda x: x.rolling(window=7).mean())
    
    # Since rolling introduces NaNs and Quantum steps are sensitive to NaNs
    # Clean the dataframe of records where features could not be computed
    df.dropna(subset=['Volatility', 'Moving_Avg'], inplace=True)
    
    # Guarantee no missing values overall across all features before scaling
    df.dropna(inplace=True)
    
    # --- Step 4: Normalize Features (CRITICAL FOR QUANTUM STEP) ---
    # Apply scaling to: Return, Volatility, Moving_Avg
    scaler = StandardScaler()
    cols_to_scale = ['Return', 'Volatility', 'Moving_Avg']
    
    # Fit scaler on these columns and replace values with scaled output
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    # Enforce correct output format: Date, Stock, Return, Volatility, Moving_Avg
    df_final = df[['Date', 'Stock', 'Return', 'Volatility', 'Moving_Avg']]
    
    # Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_final.to_csv(output_path, index=False)
    print(f"Features successfully processed and saved to {output_path}")

if __name__ == "__main__":
    # Setup paths relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    
    in_file = os.path.join(project_root, "data", "processed", "clean_data.csv")
    out_file = os.path.join(project_root, "data", "processed", "features.csv")
    
    process_features(in_file, out_file)
