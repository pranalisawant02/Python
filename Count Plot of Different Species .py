 import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create a count plot
sns.countplot(x='species', data=iris, palette="Set2")

# Add a title
plt.title("Count of Each Iris Species")

# Show the plot
plt.show()
