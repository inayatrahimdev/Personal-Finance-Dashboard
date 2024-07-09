import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page layout
st.set_page_config(layout="wide")

# Title and Description
st.title("Personal Finance Dashboard")
st.write("""
This dashboard helps you track your expenses, visualize your spending habits, and manage your budget effectively.
""")

# Upload CSV file
st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.sidebar.write("File uploaded successfully!")

    # Display the dataframe
    st.write("### Uploaded Data")
    st.dataframe(df)

    # Show summary statistics
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.write("### Visualizations")

    # Spending by Category
    st.write("#### Spending by Category")
    if 'Category' in df.columns and 'Amount' in df.columns:
        fig, ax = plt.subplots()
        sns.barplot(x=df['Category'], y=df['Amount'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Monthly Spending
    st.write("#### Monthly Spending")
    if 'Date' in df.columns and 'Amount' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y", errors='coerce')
        df = df.dropna(subset=['Date'])  # Remove rows with invalid dates
        df['Month'] = df['Date'].dt.to_period('M')
        monthly_spending = df.groupby('Month')['Amount'].sum().reset_index()
        fig, ax = plt.subplots()
        sns.lineplot(x=monthly_spending['Month'].astype(str), y=monthly_spending['Amount'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Spending Over Time
    st.write("#### Spending Over Time")
    if 'Date' in df.columns and 'Amount' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y", errors='coerce')
        df = df.dropna(subset=['Date'])  # Remove rows with invalid dates
        daily_spending = df.groupby('Date')['Amount'].sum().reset_index()
        fig, ax = plt.subplots()
        sns.lineplot(x=daily_spending['Date'], y=daily_spending['Amount'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
else:
    st.sidebar.write("Please upload a CSV file to proceed.")
