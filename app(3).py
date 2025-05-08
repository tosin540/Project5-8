import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="📊 Interactive Data Dashboard", layout="wide")

st.title("📈 Interactive Data Dashboard")
st.markdown("""
Upload any CSV file to explore the data, filter it, and visualize it — all from your browser.  
Built with [Streamlit](https://streamlit.io/) 🚀  
""")

# Upload file
uploaded_file = st.file_uploader("📂 Upload your CSV file", type="csv", help="Make sure it's a clean .csv file.")

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

    st.markdown("### 📈 Plot Your Data")
    x_column = st.selectbox("Select X-axis", columns)
    y_column = st.selectbox("Select Y-axis", columns)

    chart_type = st.radio("Choose a chart type", ["Line Chart", "Bar Chart", "Area Chart"])

    if st.button("Generate Plot"):
        chart_data = filtered_df[[x_column, y_column]].dropna()
        chart_data = chart_data.set_index(x_column)

        if chart_type == "Line Chart":
            st.line_chart(chart_data)
        elif chart_type == "Bar Chart":
            st.bar_chart(chart_data)
        elif chart_type == "Area Chart":
            st.area_chart(chart_data)
else:
    st.warning("👈 Please upload a CSV file to get started.")
