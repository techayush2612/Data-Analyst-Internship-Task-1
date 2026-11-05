#1. Data Cleaning and Preprocessing

# Import Libraries
import pandas as pd
import numpy as np

# Load Raw Dataset
df = pd.read_csv("Mall_Customers_DataSet.csv")
# Display First 5 Rows
print("\nFirst 5 Rows")
print(df.head())
# Dataset Shape
print("\nDataset Shape")
print(df.shape)
# Dataset Information
print("\nDataset Information")
df.info()
# Statistical Summary
print("\nStatistical Summary")
print(df.describe())
# Missing Values
print("\nMissing Values")
print(df.isnull().sum())
# Duplicate Records
print("\nDuplicate Records")
print(df.duplicated().sum())

# Step 2: Handle Missing Values

print("\nMissing Values Before Cleaning ")
print(df.isnull().sum())

# Fill missing numerical values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object').columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# Step 3: Remove Duplicate Records

print("\nDuplicate Records Before Cleaning")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDuplicate Records After Cleaning")
print(df.duplicated().sum())

# Step 4: Standardize Text Values
df['Gender'] = df['Gender'].str.strip().str.title()

print("\nStandardized Gender Values")
print(df['Gender'].unique())

# Step 5: Date conversion was not applicable because the selected dataset does not contain any date column.

# Step 6: Rename Column Headers
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r'[^a-z0-9]+', '_', regex=True)
    .str.strip('_')
)
print("\nUpdated Column Names")
print(df.columns.tolist())

# Step 7: Check Data Types
print("\nData Types Before Correction")
print(df.dtypes)

# Convert columns into appropriate data types
df['customerid'] = df['customerid'].astype(int)
df['age'] = df['age'].astype(int)
df['annual_income_k'] = df['annual_income_k'].astype(int)
df['spending_score_1_100'] = df['spending_score_1_100'].astype(int)

print("\n----- Data Types After Correction -----")
print(df.dtypes)

# Step 8: Save Cleaned Dataset
df.to_csv("Mall_Customer_Cleaned.csv", index=False)

print("\nCleaned Dataset Successfully Saved!")