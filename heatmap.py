import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
file_path = "other_clustered_data.csv"  # Replace with the path to your CSV
data = pd.read_csv(file_path)

# Assuming 'data' has columns: 'GEO', '2006/2007', '2007/2008', ..., '2021/2022'
# You can set 'GEO' as the index and transpose the data if necessary for the heatmap
pivot_data = data.set_index('GEO').transpose()

# Plotting the heatmap
plt.figure(figsize=(12, 8))  # Adjust the figure size as needed
sns.heatmap(pivot_data, annot=True, cmap='viridis', linewidths=0.5)

# Set the plot title and labels
plt.title('Heatmap of Values Across Regions and Years')
plt.xlabel('Regions')
plt.ylabel('Years')

# Show the heatmap
plt.show()

