 import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with your actual file name)
df = pd.read_csv('your_dataset.csv')

# Display the first five rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

# Display basic info about dataset
print("\nDataset Info:")
print(df.info())
