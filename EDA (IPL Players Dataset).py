import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("E:\Pyhton code\Data Sets\cricket_data_2025.csv")

# Display basic information about the dataset
# print(df.head())  # Shows the first few rows of the dataset
# print(df.info())  # Provides details about data types and null values
# print(df.describe())  # Summary statistics of numerical columns

# Data Cleaning: Removing duplicate and null values
df = df.drop_duplicates()  # Removes duplicate records if any
df = df.dropna()  # Removes rows with missing values
# print(df.isnull().sum())  # Verifies that there are no missing values left

# Data Type Conversion: Ensuring consistency in numerical columns
df = df.astype({'Matches_Batted':'float', 'Not_Outs':'float', 'Runs_Scored':'float',
      'Batting_Average':'float', 'Balls_Faced':'float',
       'Batting_Strike_Rate':'float', 'Centuries':'float', 'Half_Centuries':'float', 'Fours':'float', 'Sixes':'float',
       'Catches_Taken':'float', 'Stumpings':'float', 'Matches_Bowled':'float', 'Balls_Bowled':'float',
       'Runs_Conceded':'float', 'Wickets_Taken':'float',
       'Bowling_Average':'float', 'Economy_Rate':'float', 'Bowling_Strike_Rate':'float',
       'Four_Wicket_Hauls':'float', 'Five_Wicket_Hauls':'float'})

# Extracting numerical values from 'Highest_Score' column (if it contains '/' or text)
df['Highest_Score'] = df['Highest_Score'].str.extract('(/d+)').astype(float)

# Converting 'Year' column to datetime format
df['Year'] = df['Year'].astype(int)
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Data Visualization

# Histogram: Distribution of Runs Scored
sns.histplot(df["Runs_Scored"], kde=True, bins=20, color="purple")
plt.title("Distribution of Runs Scored")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.show()
# Conclusion: Most players have scored lower runs, with a few high scorers creating a right-skewed distribution.

# Box Plot: Outlier Detection for Wickets Taken
plt.figure(figsize=(6, 5))
sns.boxplot(x=df['Wickets_Taken'], color='orange')
plt.title('Wickets Taken - Outlier Detection')
plt.xlabel('Wickets Taken')
plt.show()
# Conclusion: The presence of outliers suggests that a few bowlers have taken an exceptionally high number of wickets.
    
# Scatter Plot: Relationship between Runs Scored and Batting Strike Rate
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Runs_Scored'], y=df['Batting_Strike_Rate'], color='green')
plt.title('Runs vs Batting Strike Rate')
plt.xlabel('Runs Scored')
plt.ylabel('Batting Strike Rate')
plt.show()
# Conclusion: There is a positive correlation, indicating that players who score more runs also tend to have a higher strike rate.

# Bar Chart: Top 10 Players by Total Runs Scored
top_players = df.groupby('Player_Name')['Runs_Scored'].sum().nlargest(10)
plt.figure(figsize=(10, 5))
top_players.plot(kind='bar', color='purple')
plt.title('Top 10 Players by Runs Scored')
plt.xlabel('Player Name')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.show()
# Conclusion: A few standout players dominate the run-scoring chart, showing consistency and superior batting performance.

# Pair Plot: Examining relationships between batting performance metrics
sns.pairplot(df[['Runs_Scored', 'Batting_Average', 'Batting_Strike_Rate', 'Centuries']])
plt.show()
# Conclusion: The relationships confirm that players with high averages and centuries also tend to score more runs.

# Scatter Plot: Relationship between Matches Played and Runs Scored in a Year
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Matches_Batted', y='Runs_Scored', hue='Year', palette='tab10')
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.title("Relationship between Matches Played and Runs Scored in a Year")
plt.legend(title="Year", bbox_to_anchor=(1, 1))
plt.show()
# Conclusion: Players who participate in more matches generally score more runs, reinforcing the importance of consistent playtime.
