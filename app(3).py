import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="🌍 2019 World Happiness Report", layout="wide")

st.title("🌍 2019 World Happiness Report Dashboard")
st.markdown("""
Explore, filter, and visualize data from the **2019 World Happiness Report**.  
Upload the dataset to get started — powered by [Streamlit](https://streamlit.io/) 🚀
""")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your '2019_world_happiness_report.csv' file", type="csv")

if uploaded_file is not None:
    st.success("✅ File successfully uploaded!")
    df = pd.read_csv(uploaded_file)

    with st.expander("🔍 Data Preview"):
        st.write("First 5 Rows:")
        st.dataframe(df.head())
        st.write("Last 5 Rows:")
        st.dataframe(df.tail())

    with st.expander("📊 Data Summary"):
        st.dataframe(df.describe())

    st.markdown("### 🔎 Filter the Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)

    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox(f"Select a value from '{selected_column}'", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.dataframe(filtered_df)

    st.markdown("### 📈 Line Chart Visualization")
    numeric_columns = filtered_df.select_dtypes(include='number').columns.tolist()

    if len(numeric_columns) < 2:
        st.warning("You need at least two numeric columns to plot a line chart.")
    else:
        x_column = st.selectbox("Select X-axis (must be numeric)", numeric_columns)
        y_column = st.selectbox("Select Y-axis", numeric_columns)

        if st.button("Generate Line Chart"):
            try:
                chart_data = filtered_df[[x_column, y_column]].dropna()
                # Fix: Reset index so X-axis is 1-dimensional
                chart_data = chart_data.sort_values(by=x_column)
                st.line_chart(chart_data.set_index(x_column))
            except Exception as e:
                st.error(f"⚠️ Could not generate chart: {e}")
else:
    st.warning("👈 Please upload the 2019 World Happiness Report CSV to begin.")
