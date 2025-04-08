import pandas as pd

# Sample DataFrame
# df = pd.DataFrame({
#     'age': [22, 27, 34, 45, 51, 23, 40, 29],
#     'purchased': [1, 0, 1, 1, 0, 1, 0, 1]
# })

# Define age brackets
bins = [18, 25, 35, 45, float('inf')]
labels = ['18-25', '26-35', '36-45', '46+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

# Calculate purchase rate by age group
purchase_rate = df.groupby('age_group')['purchased'].mean()

# Find the age group with the highest purchase rate
highest_group = purchase_rate.idxmax()
highest_rate = purchase_rate.max()

print(f"Age group with highest purchase rate: {highest_group} ({highest_rate:.2%})")
