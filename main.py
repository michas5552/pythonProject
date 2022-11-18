# Import the necessary modules.
import matplotlib.pyplot as plt
import pandas as pd


# Initialize the lists for X and Y
data = pd.read_csv('finance_liquor_sales.csv')
df = pd.DataFrame(data)

x = list(df.iloc[:, 6])
y = list(df.iloc[:, 20])

# plot scatter plot with x and y data
plt.scatter(x, y)
plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()

