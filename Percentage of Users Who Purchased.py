import pandas as pd

# Sample DataFrame
# df = pd.DataFrame({
#     'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'purchased': [1, 0, 1, 1, 0]
# })

# Overall purchase percentage
overall_purchase_pct = df['purchased'].mean() * 100

# Purchase percentage by gender
gender_purchase_pct = df.groupby('gender')['purchased'].mean() * 100

# Output results
print(f"Overall purchase percentage: {overall_purchase_pct:.2f}%\n")
print("Purchase percentage by gender:")
print(gender_purchase_pct.round(2).astype(str) + '%')
