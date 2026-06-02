import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("visualizations", exist_ok=True)

# Load Dataset
df = pd.read_csv("SampleSuperstore.csv")

print(df.head())
print(df.info())
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Sales by Category
sales_cat = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_cat.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png")
plt.close()

# Profit by Category
profit_cat = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_cat.plot(kind="bar")
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_category.png")
plt.close()

# Sales Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("visualizations/sales_distribution.png")
plt.close()

# Sales vs Profit
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Sales",
    y="Profit",
    data=df
)
plt.title("Sales vs Profit")
plt.tight_layout()
plt.savefig("visualizations/sales_vs_profit.png")
plt.close()

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.close()

print("Retail Analysis Completed")