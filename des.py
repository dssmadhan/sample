import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('diabetes.csv')


print("Dataset Info:")
print(df.info()) 


print("\nDescriptive Statistics (Summary):")
print(df.describe())  


df.hist(bins=15, figsize=(15, 10), grid=False)
plt.suptitle('Histograms of Diabetes Dataset')
plt.show()



correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Diabetes Dataset')
plt.show()

plt.figure(figsize=(8, 6))
sns.kdeplot(df['Age'], fill=True, color='purple')
plt.title('Density Plot of Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()


