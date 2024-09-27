import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("Housing.csv")

avg_price_area = housing_data.groupby("area")["price"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(avg_price_area["area"], avg_price_area["price"], color="blue", edgecolor="black")

plt.title("Average House Prices Based on Area")
plt.xlabel("Area")
plt.ylabel("Average Price")

plt.ticklabel_format(style="plain", axis="y")

plt.show()
