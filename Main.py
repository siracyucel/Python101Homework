import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
housing_data = pd.read_csv("Housing.csv")

# --- 1. Average Price vs. Area (Scatter Plot) ---
plt.figure(figsize=(10, 6))
plt.scatter(housing_data["area"], housing_data["price"], color="blue", edgecolor="black")
plt.title("House Prices Based on Area")
plt.xlabel("Area")
plt.ylabel("Price")
plt.ticklabel_format(style="plain", axis="y")
plt.show()

# --- 2. Average Price vs. Bedrooms (Bar Plot) ---
avg_price_bedrooms = housing_data.groupby("bedrooms")["price"].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_price_bedrooms["bedrooms"], avg_price_bedrooms["price"], color="blue", edgecolor="black")
plt.title("Average House Prices Based on Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price")
plt.ticklabel_format(style="plain", axis="y")
plt.show()

# --- 3. Average Price vs. Stories (Bar Plot) ---
avg_price_stories = housing_data.groupby("stories")["price"].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_price_stories["stories"], avg_price_stories["price"], color="orange", edgecolor="black")
plt.title("Average House Prices Based on Number of Stories")
plt.xlabel("Number of Stories")
plt.ylabel("Average Price")
plt.ticklabel_format(style="plain", axis="y")
plt.show()

# --- 4. Correlation Matrix (Heatmap) ---
numeric_data = housing_data.select_dtypes(include=[float, int])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(10, 8))
plt.matshow(correlation_matrix, cmap="coolwarm", fignum=1)
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Correlation Matrix")
plt.show()
