import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("Housing.csv")

numeric_data = housing_data.select_dtypes(include=[float, int])

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(10, 8))

plt.matshow(correlation_matrix, cmap="coolwarm", fignum=1)

plt.colorbar()

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.title("Correlation Matrix")

plt.show()
