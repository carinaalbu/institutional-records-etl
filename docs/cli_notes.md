# PowerShell Data Exploration Notes

These commands allow for quick inspection of the raw CSV files directly in the terminal.

## 1. Preview the File

Reads the first 5 lines to check headers.
`Get-Content data/raw/records_2022.csv -TotalCount 5`

## 2. Count Total Rows

Calculates the dataset size.
`(Get-Content data/raw/records_2022.csv).Count`

## 3. Search and Filter

Finds all rows containing the text "Admission" (case-insensitive).
`Select-String "Admission" data/raw/records_2022.csv`

## 4. Extract a Specific Column

Displays only the 'category' column for the first 5 rows.
`Import-Csv data/raw/records_2022.csv | Select-Object category | Select-Object -First 5`

## 5. Filter and Save (Redirection)

Finds all "Billing" records in the 2023 dataset and saves them to a new file.
`Select-String "Billing" data/raw/records_2023.csv | Out-File billing_records.txt`
