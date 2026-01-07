# ===============================
# Sales Revenue Analysis Dashboard (User CSV Upload)
# ===============================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# Step 1: App Title
# ===============================
st.title("📊 Sales Revenue Analysis Dashboard")
st.write("Upload your CSV file to explore sales and profit trends interactively.")

# ===============================
# Step 2: Upload CSV
# ===============================
uploaded_file = st.file_uploader("Upload your CSV file (CSV only)", type="csv")

if uploaded_file is not None:
    # Load CSV into DataFrame
    df = pd.read_csv(uploaded_file, encoding='latin1')
    
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    # ===============================
    # Step 3: Total Sales & Profit Overview
    # ===============================
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    
    st.subheader("📈 Total Overview")
    st.metric("Total Sales", f"${total_sales:,.2f}")
    st.metric("Total Profit", f"${total_profit:,.2f}")
    
    # ===============================
    # Step 4: Sales by Category
    # ===============================
    st.subheader("🛍️ Sales by Category")
    sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(8,5))
    sns.barplot(x=sales_by_category.values, y=sales_by_category.index, palette='viridis')
    plt.xlabel("Total Sales")
    plt.ylabel("Category")
    st.pyplot(plt)
    plt.clf()
    
    # ===============================
    # Step 5: Profit by Region
    # ===============================
    st.subheader("💰 Profit by Region")
    profit_by_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(8,5))
    sns.barplot(x=profit_by_region.values, y=profit_by_region.index, palette='magma')
    plt.xlabel("Total Profit")
    plt.ylabel("Region")
    st.pyplot(plt)
    plt.clf()
    
    # ===============================
    # Step 6: Top Products by Profit
    # ===============================
    st.subheader("🏆 Top Products by Profit")
    top_products_profit = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_products_profit.values, y=top_products_profit.index, palette='coolwarm')
    plt.xlabel("Profit")
    plt.ylabel("Product")
    st.pyplot(plt)
    plt.clf()
    
    # ===============================
    # Step 7: Optional Filters (Region/Category)
    # ===============================
    st.subheader("🔍 Filter & Explore")
    selected_region = st.multiselect("Select Region(s)", df['Region'].unique(), default=df['Region'].unique())
    selected_category = st.multiselect("Select Category(s)", df['Category'].unique(), default=df['Category'].unique())
    
    filtered_df = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category))]
    st.write(f"Filtered Data Preview ({len(filtered_df)} rows):")
    st.dataframe(filtered_df.head())
    
    st.success("Dashboard ready! Use the filters to explore your data dynamically.")
    
else:
    st.info("🔹 Please upload a CSV file to get started.")
