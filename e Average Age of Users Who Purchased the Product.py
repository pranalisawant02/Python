import pandas as pd

# Load the dataset
df = pd.read_csv('your_file.csv')  # replace with your actual filename

# Filter users who purchased the product
purchased_users = df[df['Purchased'] == 1]

# Calculate average age
average_age = purchased_users['Age'].mean()

print(f"Average age of users who purchased the product: {average_age:.2f}")
