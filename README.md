# Institutional Records ETL Pipeline

## 1. Project Purpose

This project implements a reproducible data engineering pipeline to process synthetic institutional transaction records. The goal is to automate the cleaning, standardization, and validation of raw log data from disparate legacy systems without manual intervention.

The pipeline addresses common real-world data issues, including:

- **Schema Drift:** Harmonizing differences between 2022 and 2023 data formats.
- **Data Quality:** Normalizing inconsistent naming conventions (e.g., "IMAGING" vs. "imaging"), handling missing values, and detecting duplicate records.
- **Reproducibility:** Ensuring the entire workflow can be executed via a single command in a controlled environment.

## 2. Dataset Description

The source data consists of two raw CSV files representing annual transaction logs:

- **`records_2022.csv`**: Contains fields `record_id`, `date`, `category`, `value`, `unit`, `source`, `status`.
- **`records_2023.csv`**: Introduces schema drift with new fields (`department`, `priority`) and renames `source` to `source_system`.

**Key Data Issues Handled:**

- **Inconsistent Strings:** Categories vary in case and whitespace (e.g., "medication", "MEDICATION ", "Medication").
- **Date Formats:** Mixed usage of ISO 8601 (`YYYY-MM-DD`) and other formats.
- **Integrity:** Presence of duplicate record IDs and invalid numerical outliers (negative values).

## Reproducibility Instructions

### 1. Environment Setup

This project uses **Conda** to manage dependencies and ensuring the environment is identical across different machines.

1.  **Install Conda:**
    Ensure you have [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.

2.  **Create the environment:**

    ```bash
    # Create a new environment named 'etl-env' with Python 3.9
    conda create --name etl-env python=3.9 -y
    ```

3.  **Activate the environment:**

    ```bash
    conda activate etl-env
    ```

4.  **Install dependencies:**

    ```bash
    # Install standard data libraries
    conda install pandas numpy openpyxl -y

    # Or, if you have an environment.yml file (Recommended)
    # conda env update --file environment.yml --prune
    ```

### 2. Running the Pipeline

### Execution

Once the environment is active in your PowerShell, run the pipeline script:

````powershell
python src/etl.py

```bash
# [TODO: Add specific execution command here]
# Example: python src/main.py
````

### Setup (Manual)

If you are not using the automated `make` commands, you can recreate the environment manually:

1. **Create a Conda environment** (Optional but recommended):
   ```bash
   conda create -n etl-env python=3.9
   conda activate etl-env
   ```

## 4. Data Integrity

To ensure the raw data has not been corrupted or tampered with, this project includes a SHA-256 checksum verification system.

- **Manifest File:** `data/raw/checksums.sha256` (Contains the original file fingerprints).
- **Verification Script:** `src/checksum.py`

**To verify the dataset integrity:**
Run the following command. It will check the current files against the stored fingerprints.

````bash
python src/checksum.py verify
### Update the Numbering
Since you inserted a new section 4, you should rename the old **"4. Expected Outputs"** to **"5. Expected Outputs"**.

### Final Commit
Once you have saved the README, send the changes to GitHub so your repo is 100% up to date.

```powershell
git add README.md
git commit -m "docs: Add data integrity verification instructions to README"
git push
````
