import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Data Cleaning and Processing

# Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Removing duplicates
df = df.drop_duplicates()

# Filtering data: Passengers in first class
first_class = df[df["Pclass"] == 1]

# Data Visualization

# Bar Graph: Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()
# Conclusion: Passengers in higher classes had a better survival rate, with first-class passengers having the highest chance of survival.

# Histogram: Age distribution
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# Conclusion: The majority of passengers were between 20 and 40 years old, with a relatively normal distribution.

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()
# Conclusion: There is a wide variation in fares, with younger and older passengers both paying high fares, possibly indicating different travel classes.
