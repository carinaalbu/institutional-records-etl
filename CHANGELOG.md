# Changelog

All notable changes to this project will be documented in this file.

## [v1.0] - 10-01-2026

### Added

- **ETL Pipeline:** Automated script (`src/etl.py`) to clean and merge 2022/2023 datasets.
- **Data Integrity:** SHA-256 checksum verification (`src/checksum.py`).
- **Reporting:** Automated pipeline summary report generation (`src/analyze.py`).
- **Multi-format Support:** Added JSON export alongside standard CSV output.
- **Automation:** Created `Makefile` and `make.bat` for one-click execution.

### Changed

- Refactored `src/etl.py` to handle missing columns (`department`, `priority`) dynamically.
- Updated pipeline to execute `verify` -> `clean` -> `analyze` in sequence.

### Fixed

- Resolved schema drift issues where 2022 data lacked granular source details.
- Fixed dependency management by documenting `requirements.txt`.
