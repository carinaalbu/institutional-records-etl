# Data Format Choices

For this project, the pipeline exports processed data in two formats:

1. **CSV (.csv):** Chosen for its human readability and universal compatibility with legacy systems and Excel. It remains the primary format for business reporting.
2. **JSON (.json):** Selected as the secondary format to demonstrate web-compatible data exchange.

**Why JSON?**
Unlike CSV, JSON preserves data types (numbers stay numbers, strings stay strings) and is the standard format for APIs. If this pipeline were connected to a dashboard or a web application later, JSON would be the required format. The schema evolution (adding 'department' and 'priority') is handled naturally in JSON's key-value structure.
