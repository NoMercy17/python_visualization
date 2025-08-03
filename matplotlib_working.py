import matplotlib.pyplot as plt
import pandas as pd

# Working with the matplotlib to visualize and modify the data


# data exploration
data = pd.read_csv("data.csv")
print(data.head())
print("-"*50)
print(data.info())
print("-"*50)
print(data.describe())

# modifying the datetime
data['Date'] = pd.to_datetime(data['Date'])
print(data.info())

# LINE PLOT
plt.figure(1, figsize=(12,6))
plt.plot(data['Date'], data["Sleep_Hours"])
plt.title("Sleep hours over time(Line plot)")
plt.xlabel('Date')
plt.ylabel('Nr of Sleep')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
plt.close()


# HISTOGRAM

plt.figure(2, figsize=(12,6))
plt.hist(data['Sleep_Hours'], bins=20, alpha = 0.7, linewidth = 1.7, edgecolor = 'black', histtype='stepfilled', density= False) 
# bins = width
# alpha = transparency
# histtype = step (only exterior lines)
# density, False = shows the data count
#           True = shows the percentage 

plt.title('Distribution of Sleep Hours (Histogram)')
plt.tight_layout()
#plt.show()
plt.close()


# plt.hist(data['Sleep_Hours'], bins=20, density=True)
# plt.title('Density Plot (Percentages)')
# plt.ylabel('Density')
# plt.show()


# SCATTER PLOTS
plt.figure(3, figsize=(12,6))
plt.scatter(data['Sleep_Hours'], data['Sleep_Quality'])
plt.xlabel('Sleep Hours')
plt.ylabel('Sleep Quality')
plt.title('Sleep Hours vs Sleep Quality (Scatter plots)')
#plt.show()
plt.close()


# SCATTER PLOTS variations

plt.figure(4, figsize=(12,6))
# we color based on the stress level
plt.scatter(data["Sleep_Hours"], data['Sleep_Quality'], c=data["Stress_Level"], cmap= 'viridis')
plt.colorbar(label='Stress Level')
#plt.show()
plt.close()


plt.figure(5, figsize=(12,6))
plt.scatter(data["Sleep_Hours"], data['Sleep_Quality'], s=data["Exercise_Minutes"])
#plt.show()
plt.close()



# BOX PLOTS

plt.figure(6, figsize=(12,6))
plt.boxplot( [data[data['Day_of_Week'] == day]['Sleep_Hours'] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']] )
plt.xticks(range(1,8), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.ylabel('Sleep Hours')
plt.title('Sleep Hours by Day of Week')
#plt.show()
plt.close()


# BOX PLOTS - sleep quality by stress


plt.figure(7, figsize=(12,6))
stress_levels = data['Stress_Level'].unique()
plt.boxplot( [data[data['Stress_Level']== levels]['Sleep_Quality'] for levels in stress_levels] )
plt.xticks(range(1, len(stress_levels)+1), stress_levels)
plt.xlabel("Stress label")
plt.ylabel("Sleep Quality")
plt.title("Sleep Quality by Stress level")
#plt.show()
plt.close()


# BAR CHARTS
plt.figure(figsize=(12,6))
avg_sleep_by_day = data.groupby('Day_of_Week')['Sleep_Hours'].mean()
plt.bar(avg_sleep_by_day.index, avg_sleep_by_day.values)
plt.show()

# BAR - GROUPED CHARTS

plt.figure(figsize=(12,6))

day_stats = data.groupby('Day_of_Week').agg({
    'Sleep_Hours' : 'mean',
    'Sleep_Quality' : 'mean',
    'Exercise_Minutes' : 'mean'
}).round(2)


index = range(len(day_stats.index))
width = 0.25


plt.bar( [i-width for i in index], day_stats['Sleep_Hours'], width, label='Sleep Hours')
plt.bar(index, day_stats['Sleep_Quality'], width, label = 'Sleep Quality')
plt.bar([i+width for i in index], day_stats['Exercise_Minutes']/10, width, label = 'Exercise (/10)')


plt.xlabel('Day of Week')
plt.ylabel('Values')
plt.title('Sleep & Exercise by Day of Week')
plt.xticks(index, day_stats.index, rotation = 45)
plt.show()


# SUBPLOTS

# 1x2

plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1) # rows columns position
plt.plot(data['Date'], data['Sleep_Hours'], color = 'red')
plt.title('Sleep Hours over time')
plt.xlabel('Date')
plt.ylabel('Hours')
plt.xticks(rotation = 45)


plt.subplot(1, 2, 2)
plt.hist(data['Sleep_Hours'], bins = 15, alpha = 0.7, color = 'green')
plt.title('Sleep Hours Distribution')
plt.xlabel('Hours')

plt.tight_layout()
plt.show()

plt.figure()
plt.close()



# 2x1

plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(data['Date'], data['Sleep_Hours'], color='blue')
plt.title("Sleep Hours over time")
plt.xlabel('Date')
plt.ylabel('Hours')
plt.xticks(rotation = 10)

plt.subplot(2, 1, 2)  # (2 rows, 1 column, position 2)
plt.plot(data['Date'], data['Sleep_Quality'], color='red', linewidth=2)
plt.title('Sleep Quality')
plt.xlabel('Date')
plt.ylabel('Quality Score')
plt.xticks(rotation=45)

plt.show()
plt.close()



# 2x2

plt.figure(figsize=(12,6))
plt.subplot(2, 2, 1)
plt.plot(data['Date'], data['Sleep_Hours'], color='blue')
plt.title('Sleep Hours Over Time')
plt.ylabel('Hours')

plt.subplot(2, 2, 2)
plt.hist(data['Sleep_Hours'], bins=15, alpha=0.7, color='green')
plt.title('Sleep Hours Distribution')
plt.xlabel('Hours')

plt.subplot(2, 2, 3)
plt.scatter(data['Sleep_Hours'], data['Sleep_Quality'])
plt.title('Sleep Hours vs Quality')
plt.xlabel('Sleep Hours')
plt.ylabel('Sleep Quality')

plt.subplot(2, 2, 4)
avg_sleep_by_day = data.groupby('Day_of_Week')['Sleep_Hours'].mean()
plt.bar(avg_sleep_by_day.index, avg_sleep_by_day.values)
plt.title('Average Sleep by Day')
plt.ylabel('Hours')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
