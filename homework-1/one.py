import os
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# ------------------- Setup -------------------
# Load dataset
iris = pd.read_csv("homework-1/archive/Iris.csv")  # lowercase folder, capital I in file

# Display first few rows asd
print(iris.head())

# Check for any missing values
print("Any missing values?", iris.isnull().values.any())

# Ensure the folder 'images' exists
os.makedirs("homework-1/images", exist_ok=True)

# ------------------- 1. Joint Plot -------------------
# joint = sns.jointplot(x="SepalLengthCm", y="PetalLengthCm", data=iris, kind="scatter")
# joint.savefig("homework-1/images/jointplot.png")
# print("Joint plot saved as homework-1/images/jointplot.png")

# ------------------- 2. FacetGrid Plot -------------------
# g = sns.FacetGrid(iris, col="Species")
# g.map_dataframe(sns.scatterplot, x="SepalLengthCm", y="PetalLengthCm")
# g.savefig("homework-1/images/facetgrid.png")
# print("FacetGrid plot saved as homework-1/images/facetgrid.png")

# ------------------- 3. Boxplot -------------------
# plt.figure(figsize=(8,6))
# sns.boxplot(x="Species", y="SepalLengthCm", data=iris, palette="pastel")
# plt.title("Boxplot of Sepal Length by Species")
# plt.savefig("homework-1/images/boxplot.png")
# plt.close()
# print("Boxplot saved as homework-1/images/boxplot.png")

# ------------------- 4. Strip Plot -------------------
# plt.figure(figsize=(8,6))
# sns.stripplot(x="Species", y="SepalLengthCm", data=iris, color="darkblue", jitter=True, size=4)
# plt.title("Strip Plot of Sepal Length by Species")
# plt.savefig("homework-1/images/stripplot.png")
# plt.close()
# print("Strip plot saved as homework-1/images/stripplot.png")

# ------------------- 5. Combined Box + Strip Plot -------------------
# plt.figure(figsize=(8,6))
# sns.boxplot(x="Species", y="SepalLengthCm", data=iris, whis=1.5, palette="pastel")
# sns.stripplot(x="Species", y="SepalLengthCm", data=iris, color="darkblue", jitter=True, size=4)
# plt.title("Combined Box and Strip Plot of Sepal Length by Species")
# plt.savefig("homework-1/images/box_strip_combined.png")
# plt.close()
# print("Combined Box + Strip plot saved as homework-1/images/box_strip_combined.png")

# ------------------- 6. Violin Plot -------------------
# plt.figure(figsize=(8,6))
# sns.violinplot(x="Species", y="SepalLengthCm", data=iris, palette="pastel")
# plt.title("Violin Plot of Sepal Length by Species")
# plt.savefig("homework-1/images/violinplot_sepal_length.png")
# plt.close()
# print("Violin plot saved as homework-1/images/violinplot_sepal_length.png")

# ------------------- 7. Pair Plot -------------------
# pairplot = sns.pairplot(iris, hue="Species", diag_kind="hist", palette="pastel")
# pairplot.savefig("homework-1/images/pairplot.png")
# plt.close()
# print("Pair plot saved as homework-1/images/pairplot.png")

# ------------------- 8. Correlation Heatmap -------------------
# numeric_cols = iris.select_dtypes(include=['float64', 'int64'])
# corr_matrix = numeric_cols.corr()
# plt.figure(figsize=(8,6))
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation Heatmap of Iris Dataset")
# plt.savefig("homework-1/images/correlation_heatmap.png")
# plt.close()
# print("Correlation heatmap saved as homework-1/images/correlation_heatmap.png")

# ------------------- 9. Distribution Plot -------------------
# plt.figure(figsize=(8,6))
# sns.histplot(iris["SepalLengthCm"], kde=True, color="skyblue", bins=15)
# plt.title("Distribution Plot of Sepal Length")
# plt.xlabel("Sepal Length (cm)")
# plt.ylabel("Frequency")
# plt.savefig("homework-1/images/distribution_sepal_length.png")
# plt.close()
# print("Distribution plot saved as homework-1/images/distribution_sepal_length.png")

# ------------------- 10. Swarm Plot -------------------
# plt.figure(figsize=(8,6))
# sns.swarmplot(x="Species", y="SepalLengthCm", data=iris, palette="pastel", size=5)
# plt.title("Swarm Plot of Sepal Length by Species")
# plt.xlabel("Species")
# plt.ylabel("Sepal Length (cm)")
# plt.savefig("homework-1/images/swarmplot_sepal_length.png")
# plt.close()
# print("Swarm plot saved as homework-1/images/swarmplot_sepal_length.png")
