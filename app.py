# ===============================
# Sales Revenue Analysis Dashboard
# ===============================

# Step 1: Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Page Configuration
st.set_page_config(
    page_title="Sales Revenue Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Step 3: App Title
st.title("📊 Sales Revenue Analysis Dashboard")
st.write(
    "Analyze sales, profit, and top products from your own Superstore dataset."
)

# Step 4: File Upload
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"],
    help="Upload your Superstore CSV file (e.g., Sample - Superstore.csv)"
)

if uploaded_file is not None:
    # Step 5: Load Data
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')
        st.success("✅ Data loaded successfully!")
        st.write("Dataset Preview:")
        st.dataframe(df.head())

        # Step 6: Basic Metrics
        total_sales = df['Sales'].sum()
        total_profit = df['Profit'].sum()
        st.subheader("📌 Key Metrics")
        col1, col2 = st.columns(2)
        col1.metric("Total Sales", f"${total_sales:,.2f}")
        col2.metric("Total Profit", f"${total_profit:,.2f}")

        # Step 7: Sales by Category
        st.subheader("Sales by Category")
        sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
        plt.figure(figsize=(8,5))
        sns.barplot(x=sales_by_category.values, y=sales_by_category.index, palette='viridis')
        plt.xlabel("Sales")
        plt.ylabel("Category")
        st.pyplot(plt.gcf())
        plt.clf()

        # Step 8: Profit by Region
        st.subheader("Profit by Region")
        profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
        plt.figure(figsize=(8,5))
        sns.barplot(x=profit_by_region.values, y=profit_by_region.index, palette='magma')
        plt.xlabel("Profit")
        plt.ylabel("Region")
        st.pyplot(plt.gcf())
        plt.clf()

        # Step 9: Top Products by Profit
        st.subheader("Top 10 Products by Profit")
        top_products_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(10,6))
        sns.barplot(x=top_products_profit.values, y=top_products_profit.index, palette='coolwarm')
        plt.xlabel("Profit")
        plt.ylabel("Product")
        st.pyplot(plt.gcf())
        plt.clf()

        # Step 10: Sales Distribution by State
        st.subheader("Sales Distribution by State")
        sales_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(15)
        plt.figure(figsize=(10,6))
        sns.barplot(x=sales_by_state.values, y=sales_by_state.index, palette='plasma')
        plt.xlabel("Sales")
        plt.ylabel("State")
        st.pyplot(plt.gcf())
        plt.clf()

        st.success("📈 Dashboard generated successfully!")

    except Exception as e:
        st.error(f"Error loading data: {e}")
else:
    st.info("Please upload a CSV file to see the dashboard.")
