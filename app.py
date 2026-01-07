# sales_analysis_dashboard/app.py

# ===============================
# Step 1: Import Libraries
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Sales Revenue Dashboard", layout="wide")

# ===============================
# Step 2: Load Data
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("data/Sample_Superstore.csv", encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# ===============================
# Step 3: Date Filter
# ===============================
start_date = df['Order Date'].min()
end_date = df['Order Date'].max()

selected_dates = st.slider(
    "Select Order Date Range:",
    min_value=start_date,
    max_value=end_date,
    value=(start_date, end_date)
)

filtered_df = df[(df['Order Date'] >= selected_dates[0]) &
                 (df['Order Date'] <= selected_dates[1])]

# ===============================
# Step 4: Metrics Overview
# ===============================
st.title("Sales Revenue Analysis Dashboard")

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders}")

# ===============================
# Step 5: Sales by Category
# ===============================
st.subheader("Sales by Category")
sales_by_category = filtered_df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=sales_by_category.values, y=sales_by_category.index, palette='viridis', ax=ax)
ax.set_xlabel("Total Sales")
ax.set_ylabel("Category")
st.pyplot(fig)

# ===============================
# Step 6: Profit by Region
# ===============================
st.subheader("Profit by Region")
profit_by_region = filtered_df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(x=profit_by_region.values, y=profit_by_region.index, palette='magma', ax=ax2)
ax2.set_xlabel("Total Profit")
ax2.set_ylabel("Region")
st.pyplot(fig2)

# ===============================
# Step 7: Top Products by Profit
# ===============================
st.subheader("Top 10 Products by Profit")
top_products_profit = filtered_df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots(figsize=(10,6))
sns.barplot(x=top_products_profit.values, y=top_products_profit.index, palette='coolwarm', ax=ax3)
ax3.set_xlabel("Profit")
ax3.set_ylabel("Product")
st.pyplot(fig3)

# ===============================
# Step 8: Revenue Distribution by State
# ===============================
st.subheader("Revenue Distribution by State")
sales_by_state = filtered_df.groupby('State')['Sales'].sum().sort_values(ascending=False)

fig4, ax4 = plt.subplots(figsize=(10,8))
sns.barplot(x=sales_by_state.values, y=sales_by_state.index, palette='rocket', ax=ax4)
ax4.set_xlabel("Sales")
ax4.set_ylabel("State")
st.pyplot(fig4)

st.markdown("---")
st.markdown("**Note:** All charts update dynamically based on the selected date range.")
