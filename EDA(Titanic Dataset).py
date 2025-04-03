import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


url= "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
#Data Cleaning and processing

# # Inspecting data
# print(df.info())
# print(df.describe())

#Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] =df["Embarked"].fillna(df["Embarked"].mode()[0])

#Removing duplicates
df= df.drop_duplicates()

#Filtering data: Passengers in first class
first_class = df[df["Pclass"]==1]
# print("First class Passengers: \n",first_class.head())

#Data Visualization

#Bar Graph:Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar",color="skyblue")
plt.title("Survival rate by class")
plt.ylabel("Survival Rate")
plt.show()

# #Histogram: Age distribution
# sns.histplot(df["Age"],kde=True,bins=20,color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# #Scatter Plot:Age vs Fare
# plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.title("Age vs Fare")
# plt.show()

