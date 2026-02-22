# # ============================================================
# # Task 5: Interactive Business Dashboard using Streamlit
# # Dataset: Global Superstore Dataset
# # Objective: Analyze Sales, Profit & Segment-wise Performance
# # ============================================================

# # -------------------------
# # 1. Import Required Libraries
# # -------------------------
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # -------------------------
# # 2. Page Configuration
# # -------------------------
# st.set_page_config(
#     page_title="Global Superstore Dashboard",
#     layout="wide"
# )

# st.title("📊 Global Superstore Business Dashboard")
# st.markdown("Interactive dashboard for Sales & Profit Analysis")

# # -------------------------
# # 3. Load Dataset (Cached for Performance)
# # -------------------------
# @st.cache_data
# def load_data():
#     """
#     Load the dataset and return a cleaned dataframe.
#     Caching improves performance by avoiding reloading on every refresh.
#     """
#     df = pd.read_csv("Global_Superstore.csv", encoding="latin1")
#     return df

# df = load_data()

# # -------------------------
# # 4. Data Cleaning & Preparation
# # -------------------------

# # Convert Order Date to datetime format
# df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# # Remove rows with missing values (basic cleaning)
# df.dropna(inplace=True)

# # -------------------------
# # 5. Sidebar Filters (User Interactivity)
# # -------------------------
# st.sidebar.header("🔎 Filter Data")

# # Region Filter
# region_filter = st.sidebar.multiselect(
#     "Select Region",
#     options=df["Region"].unique(),
#     default=df["Region"].unique()
# )

# # Category Filter
# category_filter = st.sidebar.multiselect(
#     "Select Category",
#     options=df["Category"].unique(),
#     default=df["Category"].unique()
# )

# # Sub-Category Filter
# sub_category_filter = st.sidebar.multiselect(
#     "Select Sub-Category",
#     options=df["Sub-Category"].unique(),
#     default=df["Sub-Category"].unique()
# )

# # Apply Filters to Dataset
# filtered_df = df[
#     (df["Region"].isin(region_filter)) &
#     (df["Category"].isin(category_filter)) &
#     (df["Sub-Category"].isin(sub_category_filter))
# ]

# # -------------------------
# # 6. KPI Section (Key Performance Indicators)
# # -------------------------

# # Calculate KPIs
# total_sales = filtered_df["Sales"].sum()
# total_profit = filtered_df["Profit"].sum()

# # Display KPIs in columns
# kpi1, kpi2 = st.columns(2)

# kpi1.metric(
#     label="💰 Total Sales",
#     value=f"${total_sales:,.2f}"
# )

# kpi2.metric(
#     label="📈 Total Profit",
#     value=f"${total_profit:,.2f}"
# )

# # -------------------------
# # 7. Sales by Category (Bar Chart)
# # -------------------------
# st.subheader("📊 Sales by Category")

# sales_by_category = (
#     filtered_df.groupby("Category")["Sales"]
#     .sum()
#     .reset_index()
# )

# fig1 = px.bar(
#     sales_by_category,
#     x="Category",
#     y="Sales",
#     color="Category",
#     title="Total Sales by Category"
# )

# st.plotly_chart(fig1, use_container_width=True)

# # -------------------------
# # 8. Profit by Region (Pie Chart)
# # -------------------------
# st.subheader("🌍 Profit Distribution by Region")

# profit_by_region = (
#     filtered_df.groupby("Region")["Profit"]
#     .sum()
#     .reset_index()
# )

# fig2 = px.pie(
#     profit_by_region,
#     names="Region",
#     values="Profit",
#     title="Profit Share by Region"
# )

# st.plotly_chart(fig2, use_container_width=True)

# # -------------------------
# # 9. Top 5 Customers by Sales
# # -------------------------
# st.subheader("🏆 Top 5 Customers by Sales")

# top_customers = (
#     filtered_df.groupby("Customer Name")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(5)
#     .reset_index()
# )

# fig3 = px.bar(
#     top_customers,
#     x="Sales",
#     y="Customer Name",
#     orientation="h",
#     title="Top 5 Customers",
# )

# st.plotly_chart(fig3, use_container_width=True)

# # -------------------------
# # 10. Footer
# # -------------------------
# st.markdown("---")
# st.markdown("Developed using Streamlit for Business Intelligence Dashboarding.")

# ============================================================
# ADVANCED BUSINESS DASHBOARD - STREAMLIT
# Dataset: Global Superstore Dataset
# Author: Mubashir Naeem
# ============================================================

# -------------------------
# 1. Import Libraries
# -------------------------
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# 2. Page Configuration
# -------------------------
st.set_page_config(
    page_title="Advanced Superstore Dashboard",
    layout="wide"
)

st.title("📊 Advanced Global Superstore Dashboard")
st.markdown("### Business Intelligence & KPI Analytics")

# -------------------------
# 3. Load Dataset (Cached)
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Global_Superstore.csv", encoding="latin1")
    return df

df = load_data()

# -------------------------
# 4. Data Cleaning
# -------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df.dropna(inplace=True)

# Create Month-Year column for trend analysis
df["Month-Year"] = df["Order Date"].dt.to_period("M").astype(str)

# -------------------------
# 5. Sidebar Filters
# -------------------------
st.sidebar.header("🔎 Filter Data")

# Date Range Filter
start_date = st.sidebar.date_input(
    "Start Date",
    df["Order Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Order Date"].max()
)

# Region Filter
region_filter = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

# Category Filter
category_filter = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

# Sub-Category Filter
sub_category_filter = st.sidebar.multiselect(
    "Select Sub-Category",
    df["Sub-Category"].unique(),
    default=df["Sub-Category"].unique()
)

# -------------------------
# 6. Apply Filters
# -------------------------
filtered_df = df[
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date)) &
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Sub-Category"].isin(sub_category_filter))
]

# -------------------------
# 7. KPI Calculations
# -------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

profit_margin = (total_profit / total_sales * 100) if total_sales != 0 else 0

# Display KPIs in 4 columns
k1, k2, k3, k4 = st.columns(4)

k1.metric("💰 Total Sales", f"${total_sales:,.2f}")
k2.metric("📈 Total Profit", f"${total_profit:,.2f}")
k3.metric("🧾 Total Orders", total_orders)
k4.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# -------------------------
# 8. Monthly Sales Trend
# -------------------------
st.subheader("📅 Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby("Month-Year")["Sales"]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    monthly_sales,
    x="Month-Year",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

# -------------------------
# 9. Sales by Category
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Sales by Category")
    sales_by_category = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig_cat = px.bar(
        sales_by_category,
        x="Category",
        y="Sales",
        color="Category"
    )
    st.plotly_chart(fig_cat, use_container_width=True)

# -------------------------
# 10. Segment-wise Performance
# -------------------------
with col2:
    st.subheader("👥 Sales by Segment")
    sales_by_segment = (
        filtered_df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig_seg = px.pie(
        sales_by_segment,
        names="Segment",
        values="Sales"
    )
    st.plotly_chart(fig_seg, use_container_width=True)

# -------------------------
# 11. Top 5 Customers
# -------------------------
st.subheader("🏆 Top 5 Customers by Sales")

top_customers = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

fig_top = px.bar(
    top_customers,
    x="Sales",
    y="Customer Name",
    orientation="h"
)

st.plotly_chart(fig_top, use_container_width=True)

# -------------------------
# 12. Download Filtered Data
# -------------------------
st.markdown("### 📥 Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download as CSV",
    data=csv,
    file_name="filtered_superstore_data.csv",
    mime="text/csv"
)

# -------------------------
# 13. Footer
# -------------------------
st.markdown("---")
st.markdown("🚀 Developed using Streamlit | Business Intelligence Dashboard Project")