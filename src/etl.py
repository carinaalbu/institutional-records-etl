import pandas as pd
import os
import sys

# Define file paths
# We use '..' to go up one level from 'src' to the root, then into 'data'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

def load_data():
    """Reads the raw CSV files."""
    print("Loading data...")
    try:
        # Load 2022 data
        path_22 = os.path.join(RAW_DIR, 'records_2022.csv')
        df_2022 = pd.read_csv(path_22)
        print(f"  - Loaded 2022 data: {df_2022.shape[0]} rows")

        # Load 2023 data
        path_23 = os.path.join(RAW_DIR, 'records_2023.csv')
        df_2023 = pd.read_csv(path_23)
        print(f"  - Loaded 2023 data: {df_2023.shape[0]} rows")
        
        return df_2022, df_2023
    except FileNotFoundError as e:
        print(f"Error: Could not find file. Make sure your files are in data/raw/. \nDetails: {e}")
        sys.exit(1)

def align_schema(df_22, df_23):
    """Fixes schema drift so 2022 matches 2023."""
    print("Aligning schemas...")
    
    # 1. Rename 'source' to 'source_system' in 2022
    if 'source' in df_22.columns:
        df_22.rename(columns={'source': 'source_system'}, inplace=True)
    
    # 2. Add missing columns to 2022 (department, priority)
    # We fill them with 'Unknown' because that data didn't exist in 2022
    df_22['department'] = 'Unknown'
    df_22['priority'] = 'Unknown'
    
    # 3. Combine them
    df_combined = pd.concat([df_22, df_23], ignore_index=True)
    return df_combined

def clean_data(df):
    """Cleans garbage values and formats text."""
    print("Cleaning data...")
    
    # 1. Standardize text (lowercase, remove extra spaces)
    # This fixes "IMAGING", "imaging ", "Imaging" -> "imaging"
    text_cols = ['category', 'source_system', 'status', 'unit']
    for col in text_cols:
        df[col] = df[col].astype(str).str.lower().str.strip()

    # 2. Handle missing numerical values
    # Fill missing values in 'value' with 0 (or you could drop them)
    df['value'] = pd.to_numeric(df['value'], errors='coerce').fillna(0)

    # 3. Drop duplicates based on record_id
    before_dedup = len(df)
    df.drop_duplicates(subset=['record_id'], keep='first', inplace=True)
    after_dedup = len(df)
    print(f"  - Removed {before_dedup - after_dedup} duplicate rows")

    return df

def main():
    # Ensure output directory exists
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Run the pipeline steps
    df_22, df_23 = load_data()
    df_merged = align_schema(df_22, df_23)
    df_clean = clean_data(df_merged)

    # Save output
    output_path = os.path.join(PROCESSED_DIR, 'records_clean.csv')
    df_clean.to_csv(output_path, index=False)
    print(f"Success! Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    main()