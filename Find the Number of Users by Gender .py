import pandas as pd

# Load the dataset (replace 'your_file.csv' with your actual file path)
df = pd.read_csv('your_file.csv')

# Display the first few rows to understand the structure
print(df.head())

# Assuming the gender column is named 'gender', count values
gender_counts = df['gender'].value_counts()

print("Number of users by gender:")
print(gender_counts)
