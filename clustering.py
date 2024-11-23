import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# Load the data
file_path = "Other_data.csv"  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Replace empty strings with NaN and drop rows with NaN values in 'VALUE' column
data['VALUE'] = data['VALUE'].replace("", pd.NA)  # Convert empty strings to NaN
data.dropna(subset=['VALUE'], inplace=True)  # Drop rows where 'VALUE' is NaN (formerly empty)

# Normalize the 'VALUE' field using MinMaxScaler
scaler = MinMaxScaler()
data['VALUE'] = scaler.fit_transform(data[['VALUE']])  # Normalize only the 'VALUE' column

# Preprocessing: Aggregate data by 'GEO' and 'Field of study'
aggregated_data = data.groupby(['GEO',"REF_DATE"])['VALUE'].mean().reset_index()

# Pivot the table to create a matrix where rows are 'GEO' and columns are 'Field of study'
pivot_table = aggregated_data.pivot(index='GEO', columns = "REF_DATE",values='VALUE').fillna(0)

# Standardize the data for clustering
scaler = StandardScaler()
scaled_data = scaler.fit_transform(pivot_table)

# Determine the optimal number of clusters using the Elbow method
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Optimal k')
plt.show()

# Perform K-means clustering with optimal number of clusters (choose k based on Elbow curve)
optimal_k = 4  # Replace with the chosen value of k
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to the original data
pivot_table['Cluster'] = clusters
print(pivot_table)

# Save the results to a CSV file
pivot_table.to_csv("other_clustered_data.csv")
