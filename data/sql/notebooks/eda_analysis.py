import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/retail_sales.csv')

# Basic Info
print("Dataset Overview:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Total Revenue
total_revenue = df['total_amount'].sum()
print(f"\nTotal Revenue: {total_revenue}")

# Revenue by Category
category_revenue = df.groupby('product_category')['total_amount'].sum()
print("\nRevenue by Category:")
print(category_revenue)

# Plot Revenue by Category
category_revenue.plot(kind='bar')
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# Monthly Trend
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['total_amount'].sum()

monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
