import pandas as pd
import os

# Paths
INPUT_FILE = "data/processed/records_clean.csv"
OUTPUT_FILE = "reports/pipeline_summary.txt"

def generate_report():
    print(f"Generating report from {INPUT_FILE}...")
    
    # 1. Read Data
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Run ETL first.")
        exit(1)
        
    df = pd.read_csv(INPUT_FILE)
    
    # 2. Calculate Stats
    total_rows = len(df)
    categories = df['category'].value_counts().to_string()
    systems = df['source_system'].value_counts().to_string()
    
    # 3. Write Report
    os.makedirs("reports", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write("AUTOMATED PIPELINE REPORT\n")
        f.write("=========================\n\n")
        f.write(f"Total Records Processed: {total_rows}\n\n")
        f.write("Records by Category:\n")
        f.write(categories + "\n\n")
        f.write("Records by Source System:\n")
        f.write(systems + "\n")
        
    print(f"Success! Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_report()