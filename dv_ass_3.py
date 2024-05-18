import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the dataset
file_path = r"C:\Users\Owner\Downloads\wine+quality (1)\winequality-red.csv"  
red_wine_data = pd.read_csv(file_path, delimiter=';')

# Correlation analysis with a heatmap
selected_variables = ['alcohol', 'sulphates', 'pH', 'quality']
correlation_matrix = red_wine_data[selected_variables].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlations Among Alcohol, Sulphates, pH, and Quality')
plt.show()

# 3D Scatter Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(
    red_wine_data['alcohol'],
    red_wine_data['sulphates'],
    red_wine_data['pH'],
    c=red_wine_data['quality'],
    cmap='viridis'
)
ax.set_xlabel('Alcohol')
ax.set_ylabel('Sulphates')
ax.set_zlabel('pH')
ax.set_title('3D Scatter Plot of Alcohol, Sulphates, and pH by Wine Quality')
plt.colorbar(sc, label='Quality')
plt.show()

# Trellis Plot
# Categorizing pH levels into low, medium, and high
pH_bins = pd.qcut(red_wine_data['pH'], 3, labels=['Low', 'Medium', 'High'])
red_wine_data['pH_category'] = pH_bins
g = sns.FacetGrid(red_wine_data, col="pH_category")
g.map(sns.scatterplot, "alcohol", "quality")
g.fig.suptitle('Trellis Plot: Alcohol vs Quality Across Different pH Categories', y=1.03)
g.set_axis_labels("Alcohol", "Quality")
g.add_legend()
plt.show()
