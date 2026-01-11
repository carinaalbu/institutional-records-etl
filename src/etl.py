import pandas as pd
import os

# Define file paths
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
FILES = {
    2022: os.path.join(RAW_DIR, "records_2022.csv"),
    2023: os.path.join(RAW_DIR, "records_2023.csv")
}
OUTPUT_FILE_CSV = os.path.join(PROCESSED_DIR, "records_clean.csv")
OUTPUT_FILE_JSON = os.path.join(PROCESSED_DIR, "records_clean.json")

def load_data():
    """Loads raw data from CSV files."""
    print("Loading data...")
    dfs = []
    for year, file_path in FILES.items():
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df['year'] = year  # Add year column to track origin
            dfs.append(df)
        else:
            print(f"Warning: {file_path} not found.")
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def transform_data(df):
    """Cleans and harmonizes the dataset."""
    print("Transforming data...")
    
    # 1. Standardize Column Names (Lowercase + Strip spaces)
    df.columns = df.columns.str.strip().str.lower()
    
    # 2. Harmonize Columns (Fill missing columns for 2022 data)
    if 'department' not in df.columns:
        df['department'] = "Unknown"
    else:
        df['department'] = df['department'].fillna("Unknown")
        
    if 'priority' not in df.columns:
        df['priority'] = "Unknown"
    else:
        df['priority'] = df['priority'].fillna("Unknown")

    # 3. Clean Text Columns
    text_cols = ['category', 'source_system', 'department']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()

    # 4. Handle Missing Values
    if 'value' in df.columns:
        df['value'] = pd.to_numeric(df['value'], errors='coerce').fillna(0)

    # 5. Remove Duplicates (based on record_id if it exists)
    if 'record_id' in df.columns:
        df = df.drop_duplicates(subset=['record_id'])
        
    return df

def save_data(df):
    """Saves the processed data to multiple formats."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    # Save as CSV (Standard)
    df.to_csv(OUTPUT_FILE_CSV, index=False)
    print(f"Saved CSV to: {OUTPUT_FILE_CSV}")
    
    # Save as JSON (New Requirement)
    df.to_json(OUTPUT_FILE_JSON, orient="records", indent=2)
    print(f"Saved JSON to: {OUTPUT_FILE_JSON}")

if __name__ == "__main__":
    df_raw = load_data()
    if not df_raw.empty:
        df_clean = transform_data(df_raw)
        save_data(df_clean)
        print("ETL Pipeline Completed Successfully.")
    else:
        print("ETL Failed: No data loaded.")