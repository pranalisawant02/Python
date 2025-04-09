
import pandas as pd

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Group by species and find average petal width
result = df.groupby('species')['petal width (cm)'].mean()

# Find the species with the largest average
print(result.idxmax(), result.max())
