import pandas as pd

# Load the dataset from a CSV file
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display summary statistics for the dataset
print("\nSummary statistics:")
print(data.describe())

# Check for missing values in the dataset
print("\nMissing values in each column:")
print(data.isnull().sum())

# Filter the dataset to include only rows where column 'A' is greater than a certain value
filtered_data = data[data['A'] > 10]
print("\nFiltered dataset (where 'A' > 10):")
print(filtered_data)

# Group the data by column 'B' and calculate the mean of each group
grouped_data = data.groupby('B').mean()
print("\nMean values grouped by 'B':")
print(grouped_data)

# Save the filtered dataset to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)
print("\nFiltered dataset saved to 'filtered_data.csv'.")