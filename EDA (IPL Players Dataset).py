import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("E:\Pyhton code\Data Sets\cricket_data_2025.csv")

# print(df.head())

# print(df.info())
# print(df.describe())

#Removing null values
df= df.drop_duplicates()
df = df.dropna()
# print(df.isnull().sum())

# print(df.info())

#changing datatype
# print(df.columns)

df = df.astype({'Matches_Batted':'float', 'Not_Outs':'float', 'Runs_Scored':'float',
      'Batting_Average':'float', 'Balls_Faced':'float',
       'Batting_Strike_Rate':'float', 'Centuries':'float', 'Half_Centuries':'float', 'Fours':'float', 'Sixes':'float',
       'Catches_Taken':'float', 'Stumpings':'float', 'Matches_Bowled':'float', 'Balls_Bowled':'float',
       'Runs_Conceded':'float', 'Wickets_Taken':'float',
       'Bowling_Average':'float', 'Economy_Rate':'float', 'Bowling_Strike_Rate':'float',
       'Four_Wicket_Hauls':'float', 'Five_Wicket_Hauls':'float'})
df['Highest_Score']=df['Highest_Score'].str.extract('(/d+)').astype(float)
df['Year'] = df['Year'].astype(int)
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
# print(df.info())


# print(df.columns)


# Histogram: Runs Scored
sns.histplot(df["Runs_Scored"] , kde=True, bins=20, color="purple")
plt.title("Run Scored")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.show()

#Box Plot: For Wickets Taken by players
plt.figure(figsize=(6, 5))
sns.boxplot(x=df['Wickets_Taken'], color='orange')
plt.title('Wickets Taken - Outlier Detection')
plt.xlabel('Wickets Taken')
plt.show()
    
    
#Scatter Plot:RUNS VS Batting strike rate
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Runs_Scored'], y=df['Batting_Strike_Rate'], color='green')
plt.title('Runs vs Batting Strike Rate')
plt.xlabel('Runs Scored')
plt.ylabel('Batting Strike Rate')
plt.show()


#bar chat :To see top 10 players
top_players = df.groupby('Player_Name')['Runs_Scored'].sum().nlargest(10)
plt.figure(figsize=(10, 5))
top_players.plot(kind='bar', color='purple')
plt.title('Top 10 Players by Runs Scored')
plt.xlabel('Player Name')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.show()


#Pair Plot:shows overall performance of players
sns.pairplot(df[['Runs_Scored', 'Batting_Average', 'Batting_Strike_Rate', 'Centuries']])
plt.show()

#Scatterplot: shows relationship between matches played and runs scored in those matches.
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Matches_Batted', y='Runs_Scored', hue='Year', palette='tab10')
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.title("Relationship between Matches playes and runs scored in a year")
plt.legend(title="Year", bbox_to_anchor=(1, 1))
plt.show()
