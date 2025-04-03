import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from an Excel file
file_path = "E:\Pyhton code\demo.txt\sample data.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
print(df.head())

# Display dataset info and size
print(df.info())
print(f"Dataset Size: {df.size}")

# Drop unnecessary columns
df.drop(["Dimensions", "Plot Area"], axis=1, inplace=True)

# Fill missing values with 0
df.fillna(value=0, inplace=True)

# Convert specific columns to integer type
df['Price '] = df['Price '].astype(int)
df['Bathroom'] = df['Balcony'].astype(int)
df['Balcony'] = df['Balcony'].astype(int)

# Rename column to remove trailing space
df = df.rename(columns={'Price ': 'Price'})

# Extract numeric values from 'Carpet Area' and 'Super Area' and convert to integer
df['Carpet Area'] = df['Carpet Area'].str.extract(r'(\d+)').fillna(0).astype(int)
df['Super Area'] = df['Super Area'].str.extract(r'(\d+)').fillna(0).astype(int)

# Display updated column names and check for missing values
print(df.columns)
print(df.isnull().sum())

# Calculate average price based on furnishing type
furnishing_price = df.groupby("Furnishing")['Price'].mean().sort_values(ascending=False)

# Plot bar chart for average price by furnishing type
sns.barplot(x=furnishing_price.index, y=furnishing_price.values, palette='viridis')
plt.xticks(rotation=0)
plt.xlabel("House Interior")
plt.ylabel("Average Price")
plt.title("Average House Price by Furnishing Type")
plt.show()

# Scatter plot: Carpet Area vs Price, colored by location
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Carpet Area', y='Price', hue='location', palette='tab10')
plt.xlabel("Carpet Area (sqft)")
plt.ylabel("Price")
plt.title("Relationship between Carpet Area and Price based on Location")
plt.legend(title="Location", bbox_to_anchor=(1, 1))
plt.show()

# Scatter plot: Super Area vs Price, colored by location
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Super Area', y='Price', hue='location', palette='tab10')
plt.xlabel("Super Area (sqft)")
plt.ylabel("Price")
plt.title("Relationship between Super Area and Price based on Location")
plt.legend(title="Location", bbox_to_anchor=(1, 1))
plt.show()

# Categorize 'Carpet Area' into bins
df['Carpet Area'] = pd.cut(df['Carpet Area'], bins=[0, 500, 1000, 1500, 2000, 3000], 
                           labels=["<500", "500-1000", "1000-1500", "1500-2000", "2000+"])

# Box plot: Price distribution across different Carpet Area ranges
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Carpet Area', y='Price', hue='location', palette='coolwarm')
plt.xlabel("Carpet Area Range (sqft)")
plt.ylabel("Price")
plt.title("Price Distribution for Different Carpet Area Ranges by Location")
plt.legend(title="Location", bbox_to_anchor=(1, 1))
plt.show()
