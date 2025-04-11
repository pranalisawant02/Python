import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(iris, hue="species", palette="Set2")

# Show the plot
plt.show()
