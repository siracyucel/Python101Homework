import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("Housing.csv")

avg_price_stories = housing_data.groupby("stories")["price"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(avg_price_stories["stories"], avg_price_stories["price"], color="orange", edgecolor="black")

plt.title("Average House Prices Based on Number of Stories")
plt.xlabel("Number of Stories")
plt.ylabel("Average Price")

plt.ticklabel_format(style="plain", axis="y")

plt.show()
