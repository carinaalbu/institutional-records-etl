# Data Integrity & Verification

To ensure the raw dataset has not been corrupted or tampered with, we use SHA-256 checksums.

## 1. Manifest Location

The checksum manifest is stored at: `data/raw/checksums.sha256`

It contains the "fingerprints" of the original 2022 and 2023 CSV files.

## 2. How to Verify

To verify that the files currently on disk match the original fingerprints, run the integrity script:

```bash
python src/checksum.py verify
```
