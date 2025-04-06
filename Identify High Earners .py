import pandas as pd

# Load the dataset
df = pd.read_csv('your_file.csv')  # Replace with your actual file path

# Filter high earners who didn't purchase
high_earners_no_purchase = df[(df['EstimatedSalary'] > 100000) & (df['Purchased'] == 0)]

# Display the results
print("High earners who didn't purchase the product:")
print(high_earners_no_purchase)
