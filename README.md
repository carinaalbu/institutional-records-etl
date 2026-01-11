# Institutional Records ETL Pipeline

![Version](https://img.shields.io/badge/version-v1.0-blue)

**Current Release:** v1.0

## 1. Project Overview

This project implements a reproducible data engineering pipeline to process synthetic institutional transaction records. The goal is to automate the cleaning, standardization, and validation of raw log data from disparate legacy systems without manual intervention.

The pipeline addresses common real-world data issues, including:

- **Schema Drift:** Harmonizing differences between 2022 and 2023 data formats.
- **Data Quality:** Normalizing inconsistent naming conventions (e.g., "IMAGING" vs. "imaging"), handling missing values, and detecting duplicate records.
- **Reproducibility:** Ensuring the entire workflow can be executed via a single command in a controlled environment.

---

## 2. Folder Structure

The project is organized to separate code, data, and documentation:

```text
├── data/
│   ├── raw/             # Original immutable CSVs + checksum manifest
│   └── processed/       # Cleaned output files (CSV & JSON)
├── docs/
│   ├── data_dictionary.md   # Detailed column definitions
│   ├── cli_notes.md         # Command-line exploration guide
│   └── formats_notes.md     # Explanation of output formats
├── reports/             # Auto-generated validation summaries
├── src/                 # Python source code (ETL, Analysis, Checksums)
├── Makefile             # Automation for Linux/Mac
├── make.bat             # Automation for Windows
└── requirements.txt     # Python dependencies
```

---

## 3. Dataset Description

The source data consists of two raw CSV files representing annual transaction logs:

- **`records_2022.csv`**: Contains fields `record_id`, `date`, `category`, `value`, `unit`, `source`, `status`.
- **`records_2023.csv`**: Introduces schema drift with new fields (`department`, `priority`) and renames `source` to `source_system`.

**Key Data Issues Handled:**

- **Inconsistent Strings:** Categories vary in case and whitespace (e.g., "medication" vs "MEDICATION ").
- **Missing Data:** 2022 records lack the `department` and `priority` columns found in 2023.
- **Integrity:** Presence of duplicate record IDs and outliers (negative values).

---

## 4. Reproducibility Instructions (How to Run)

This project is fully automated. You can install dependencies, verify integrity, clean data, and generate reports with **one command**.

### Option A: The "One Command" (Recommended)

**Prerequisite:** Ensure you have **Anaconda** or **Miniconda** installed and your terminal is open in the project folder.

**For Windows:**

```powershell
.\make.bat all
```

**For Linux/Mac:**

```bash
make all
```

_This command will:_

1.  Install Python dependencies (`pandas`, `openpyxl`).
2.  Verify raw data integrity (SHA-256).
3.  Run the ETL pipeline.
4.  Generate the final report.

### Option B: Manual Setup

1.  **Create Environment:**
    ```bash
    conda create -n etl-env python=3.9 -y
    conda activate etl-env
    ```
2.  **Install Dependencies:**
    ```bash
    conda install --yes --file requirements.txt
    ```
3.  **Run Pipeline Steps:**
    ```bash
    python src/checksum.py verify  # Step 1: Verify
    python src/etl.py              # Step 2: Clean
    python src/analyze.py          # Step 3: Report
    ```

---

## 5. Data Integrity

To ensure the raw data has not been corrupted or tampered with, this project includes a SHA-256 checksum verification system.

- **Manifest File:** `data/raw/checksums.sha256` (Contains the original file fingerprints).
- **Verification Script:** `src/checksum.py`

**To verify the dataset integrity manually:**
Run the following command. It will check the current files against the stored fingerprints.

```bash
python src/checksum.py verify
```

---

## 6. Expected Outputs

After running the pipeline, the following files will be generated:

1.  **`data/processed/records_clean.csv`**: The master dataset, unified and cleaned.
2.  **`data/processed/records_clean.json`**: The same dataset in JSON format for web compatibility.
3.  **`reports/pipeline_summary.txt`**: A text report summarizing total rows processed and category statistics.

---

## 7. Data Notes & Limitations

- **Synthetic Data:** This dataset is generated for educational purposes and contains no Personally Identifiable Information.
- **Schema Evolution:** The 2022 dataset was backfilled with "Unknown" for the `department` and `priority` columns to match the 2023 schema.
- **Constraints:** The pipeline currently rejects any file that does not match the stored SHA-256 checksums to prevent processing corrupted data.

---

## 8. How to Cite / Reuse

**Internal Use:**
This pipeline is designed for the Institutional Records Department. Before processing new yearly batches, ensure raw files are added to `data/raw/` and regenerate checksums using `python src/checksum.py`.

**Citation:**

> Albu, C. (2024). _Institutional Records ETL Pipeline_ [Source Code]. Internal Repository.
