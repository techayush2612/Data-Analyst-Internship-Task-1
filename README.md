# Task 1: Data Cleaning and Preprocessing

## Internship: Data Analyst Internship

# 1. Project Overview
The objective of this task is to clean and prepare a raw dataset using Python and Pandas.

# 2. Dataset Information
- Dataset Name: Mall Customer Segmentation Data
- Total Records:200
- Total Columns: 5
- Source:Kaggle
- Tools Used: Python, Pandas, NumPy, VS Code

# 3. Data Cleaning Operations Performed

1. Dataset Loading:Loaded the CSV dataset using Pandas.
2. Missing Values Handling:Checked missing values using `isnull()` and handled them using median and mode imputation wherever required.
3. Duplicate Removal:Identified and removed duplicate records using `drop_duplicates()`.
4. Text Standardization: Standardized Gender values using string operations.
5. Date Conversion: Not applicable because the dataset does not contain a date column.
6. Column Renaming: Converted column names into lowercase and replaced spaces with underscores.
7. Data Type Checking: Checked and corrected numerical column data types.
8. Dataset Export:Saved the cleaned dataset as a new CSV file.

# 4. Results
- Missing values found: 0
- Duplicate records found: 0
- Records after cleaning: 200
- Columns after cleaning: 5
- Cleaned dataset successfully exported.

# 5. Files Included
- `data_cleaning.py` – Python source code.
- `Mall_Customers_DataSet.csv` – Original dataset.
- `Mall_Customer_Cleaned.csv` – Cleaned dataset.

# 6. Conclusion
The Mall Customer dataset was inspected and processed using Python libraries. Data quality checks and preprocessing operations were performed, and the final cleaned dataset was exported successfully.

This task helped develop practical knowledge of data cleaning and preprocessing using Pandas.