import pandas as pd
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Compute average sepal length for each species
avg_sepal_length = df.groupby('species')['sepal length (cm)'].mean()
print(avg_sepal_length)
