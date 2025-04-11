import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create a KDE plot for petal width by species
sns.kdeplot(data=iris, x="petal_width", hue="species", fill=True, common_norm=False, alpha=0.5, palette="Set2")

# Add a title
plt.title("KDE Plot of Petal Width by Iris Species")

# Show the plot
plt.show()
