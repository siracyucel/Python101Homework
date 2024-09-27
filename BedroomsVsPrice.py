import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("Housing.csv")

avg_price_bedrooms = housing_data.groupby("bedrooms")["price"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(avg_price_bedrooms["bedrooms"], avg_price_bedrooms["price"], color="blue", edgecolor="black")

plt.title("Average House Prices Based on Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price")

plt.ticklabel_format(style="plain", axis="y")

plt.show()
