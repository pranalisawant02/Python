import pandas as pd

# Load the dataset
data = pd.read_csv("Social_Network_Ads.csv")

# Find the number of male and female users
gender_counts = data['Gender'].value_counts()

print(gender_counts)
