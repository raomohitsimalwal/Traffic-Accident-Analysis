import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\OneDrive\Prodigy InfoTech\DS_05\UK_Accident.csv")

print(df.head())

print(df.isnull().sum())

df = df.drop(columns=["Special_Conditions_at_Site", "Carriageway_Hazards"])

df["Location_Easting_OSGR"].fillna(df["Location_Easting_OSGR"].mean(), inplace=True)
df["Longitude"].fillna(df["Longitude"].mean(), inplace=True)
df["Location_Northing_OSGR"].fillna(df["Location_Northing_OSGR"].mean(), inplace=True)
df["Time"].fillna(df["Time"].mode()[0], inplace=True)

df["Junction_Control"].fillna(df["Junction_Control"].mode()[0], inplace=True)
df["Pedestrian_Crossing-Human_Control"].fillna(df["Pedestrian_Crossing-Human_Control"].mode()[0], inplace=True)

df = df.dropna()

print(df.isnull().sum())

# Accident Severity
severity_counts = df['Accident_Severity'].value_counts().sort_index()
severity_labels = ['Fatal', 'Serious', 'Slight']

plt.figure(figsize=(8, 6))
sns.barplot(x=severity_labels, y=severity_counts.values, palette='viridis')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# Temporal Analysis
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce')

df['Day_of_Week'] = df['Date'].dt.day_name()
day_of_week_counts = df['Day_of_Week'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=day_of_week_counts.index, y=day_of_week_counts.values, palette='muted')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.show()

# Road Conditions and Weather
plt.figure(figsize=(12, 6))
sns.countplot(x='Road_Surface_Conditions', data=df, hue='Weather_Conditions', palette='coolwarm')
plt.title('Accidents by Road Surface Conditions and Weather')
plt.xlabel('Road Surface Conditions')
plt.ylabel('Number of Accidents')
plt.legend(title='Weather Conditions', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Geospatial Analysis (Assuming you have latitude and longitude columns)
plt.figure(figsize=(10, 10))
sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='Accident_Severity', palette='Set1', alpha=0.5)
plt.title('Accident Hotspots')
plt.show()

# Contributing Factors
contributing_factor_counts = df['Junction_Control'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=contributing_factor_counts.index, y=contributing_factor_counts.values, palette='pastel')
plt.title('Accidents by Junction Control')
plt.xlabel('Junction Control')
plt.ylabel('Number of Accidents')
plt.show()
