import pandas as pd

# Load the dataset using openpyxl engine for compatibility
df = pd.read_excel("E:\Pyhton code\demo.txt\sample data.xlsx", engine="openpyxl")

# Drop missing values
df = df.dropna(axis=1)  # Remove entire columns with missing values
df = df.dropna()  # Remove rows with missing values
df = df.drop_duplicates()  # Remove duplicate rows
df = df.drop(columns=["Unnecessary_Column"], errors='ignore')  # Drop a specific column safely

#Filling missing values
df["Plot"] = df["Plot"].fillna(0)  # Fill missing values in 'Plot' column with 0
df.fillna(method="ffill", inplace=True)  # Forward fill: Fill NaN with the value above
df.fillna(method="bfill", inplace=True)  # Backward fill: Fill NaN with the value below
df["Plot"] = df["Plot"].interpolate()  # Interpolate missing values based on pattern


# Data Modification
df = df.rename(columns={"Price(in Rupees)": "Price"})  # Rename column
df["Price"] = df["Price"].astype(int)  # Convert 'Price' column to integer type


# Adding a new column with modified values
df["New_Price"] = df["Price"] * 2

# Replacing values
df["Category"] = df["Category"].replace({"Old_Value": "New_Value"})  # Replace values in a column

# Data concatenation and merging
combined = pd.concat([df1, df2], axis=0)  # Combine dataframes along rows
combined = pd.concat([df1, df2], axis=1)  # Combine dataframes along columns

# Merge dataframes based on a common column
merged = pd.merge(df1, df2, on="Common_column")  # Merge using common column
merged = pd.merge(df1, df2, how="left", on="Common_column")  # Left join
merged = pd.merge(df1, df2, how="inner", on="Common_column")  # Inner join

# Join dataframes using index alignment
joined = df1.join(df2, how="inner")
