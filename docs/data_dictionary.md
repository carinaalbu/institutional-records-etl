# Data Dictionary: Institutional Records

**Granularity:** One row per administrative event (admission, billing, medication, etc.).
**Time Range:** 2022-2023

| Column Name     | Data Type | Description                               | Issues Handled                                                              |
| :-------------- | :-------- | :---------------------------------------- | :-------------------------------------------------------------------------- |
| `record_id`     | String    | Unique identifier (e.g., R0000794).       | **Critical:** Used for deduplication.                                       |
| `date`          | Date      | Event date.                               | Standardized mixed formats (`YYYY-MM-DD` and `DD/MM/YYYY`) to ISO 8601.     |
| `category`      | String    | Event type (Admission, Billing, etc.).    | Normalized case (e.g., "IMAGING" $\to$ "imaging") and trimmed whitespace.   |
| `value`         | Float     | Numerical magnitude of the event.         | Missing values filled with 0; parsed from strings.                          |
| `unit`          | String    | Measurement unit (points, EUR, mg, etc.). | Normalized to lowercase.                                                    |
| `source_system` | String    | Originating IT system.                    | Unified `source` (2022) and `source_system` (2023) into this single column. |
| `status`        | String    | Workflow status (ok, pending, etc.).      | Normalized to lowercase.                                                    |
| `department`    | String    | Hospital department (e.g., ICU, LAB).     | **New in 2023.** Filled with "Unknown" for 2022 records.                    |
| `priority`      | String    | Urgency level (high, medium, low).        | **New in 2023.** Filled with "Unknown" for 2022 records.                    |
