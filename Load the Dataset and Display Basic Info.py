import pandas as pd

# Load the dataset
data = pd.read_csv("Social_Network_Ads.csv")

# Display the first 5 rows
print(data.head())

# Display summary information
print(data.info())
print(data.describe())
