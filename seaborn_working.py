import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
data = pd.read_csv('data.csv')

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set Seaborn style
sns.set_style('whitegrid')

# Visualize the correlation matrix of numerical features
correlation_matrix = data.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(correlation_matrix, annot = True, cmap='coolwarm', center = 0)
plt.show()


# Scatter plot with regression line between Sleep_Hours and Sleep_Quality
sns.regplot(data = data, x ='Sleep_Hours', y='Sleep_Quality')
plt.show()

# PAIRPLOT
sns.pairplot(data[['Sleep_Hours', 'Sleep_Quality', 'Stress_Level', 'Exercise_Minutes']])
plt.show()

# Scatter between sleep hours/quality colored by stress level and big/small based on exercise
sns.scatterplot(data = data, x = 'Sleep_Hours', y ='Sleep_Quality', hue='Stress_Level', size = 'Exercise_Minutes')
plt.show()

# HISTOGRAM
# Distribution of Sleep_Hours with KDE
sns.histplot(data = data, x = "Sleep_Hours", kde = True) 
plt.show()


sns.boxplot(data= data, x = 'Day_of_Week', y='Sleep_Hours')
plt.show()