import os
import pandas as pd
import numpy as np

def validate_pipeline(features_path: str, regimes_path: str):
    """
    Validates the generated features.csv and regimes.csv based on strict rules.
    """
    print("\n--- Pipeline Validation ---")
    
    if not os.path.exists(features_path):
        print(f"❌ Error: {features_path} not found.")
        return
        
    df_features = pd.read_csv(features_path)
    
    print(f"Loaded features.csv: {df_features.shape[0]} rows.")
    
    # Check 1: No missing values
    missing_count = df_features.isnull().sum().sum()
    if missing_count == 0:
        print("✅ No missing values in features.csv.")
    else:
        print(f"❌ Found {missing_count} missing values in features.csv.")
        
    # Check 2: Sorted properly and Data Consistency per date
    # Convert date to datetime for correct checking
    df_features['Date'] = pd.to_datetime(df_features['Date'])
    is_sorted = df_features.sort_values(by=['Stock', 'Date']).equals(df_features)
    if is_sorted:
        print("✅ features.csv is sorted properly by Stock and Date.")
    else:
        print("❌ features.csv is NOT sorted properly.")

    # Check 3: Feature Scaling Check
    cols_to_check = ['Return', 'Volatility', 'Moving_Avg']
    if all(col in df_features.columns for col in cols_to_check):
        means = df_features[cols_to_check].mean()
        stds = df_features[cols_to_check].std()
        
        # Check if mean ≈ 0 (tolerance e.g., 1e-4 but floating point might vary slightly)
        mean_ok = np.allclose(means.values, 0, atol=0.01)
        # std could be 1 or slightly off if ddof=1 vs 0, we'll check within 0.01
        std_ok = np.allclose(stds.values, 1, atol=0.01)
        
        if mean_ok and std_ok:
            print("✅ Features are correctly scaled (mean ≈ 0, std ≈ 1).")
        else:
            print(f"❌ Feature scaling might be incorrect:")
            print(f"   Means:\n{means}")
            print(f"   Stds:\n{stds}")
    
    # Check 4: Label alignment
    if not os.path.exists(regimes_path):
        print(f"⚠️ Warning: {regimes_path} not found. Skipping alignment check.")
    else:
        df_regimes = pd.read_csv(regimes_path)
        # Check alignment logic here depending on the format of regimes.csv
        # If regimes_path is purely Date, Regime, we check if the dates match the unique dates in features
        df_regimes['Date'] = pd.to_datetime(df_regimes['Date'])
        
        features_dates = df_features['Date'].drop_duplicates().sort_values().reset_index(drop=True)
        regimes_dates = df_regimes['Date'].drop_duplicates().sort_values().reset_index(drop=True)
        
        if features_dates.equals(regimes_dates):
            print("✅ Label alignment: features.csv and regimes.csv have the exact same dates.")
        else:
            print("❌ Label alignment mismatch. Dates in features.csv and regimes.csv differ.")
        
    print("---------------------------\n")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    features_csv = os.path.join(base_dir, "data", "processed", "features.csv")
    regimes_csv = os.path.join(base_dir, "data", "labels", "regimes.csv")
    
    validate_pipeline(features_csv, regimes_csv)
