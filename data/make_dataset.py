import pandas as pd
import os

def clean_financial_data(input_path: str, output_path: str):
    """Basic hardening: cleans columns and handles missing values."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} missing.")
        
    df = pd.read_csv(input_path)
    
    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    # Fill missing D&A with 0 as a safe financial assumption
    df['depreciation_amortization'] = df['depreciation_amortization'].fillna(0)
    
    df.to_csv(output_path, index=False)
    print(f"Data hardened and saved to {output_path}")

if __name__ == "__main__":
    clean_financial_data('data/raw/firm_data.csv', 'data/processed/clean_firms.csv')
