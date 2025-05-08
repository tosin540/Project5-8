import streamlit as st
import pandas as pd

st.set_page_config(page_title="🌍 World Happiness Report 2019", layout="wide")
st.title("🌍 World Happiness Report 2019 Dashboard")

# 🧠 Safe function to deduplicate column names
def deduplicate_columns(columns):
    seen = {}
    result = []
    for col in columns:
        if col in seen:
            seen[col] += 1
            result.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            result.append(col)
    return result

# 📁 File uploader
uploaded_file = st.file_uploader("📂 Upload your 2019 World Happiness Report CSV", type="csv")

if uploaded_file is not None:
    st.success("✅ File successfully uploaded!")

    # Load and deduplicate columns
    df = pd.read_csv(uploaded_file)
    df.columns = deduplicate_columns(df.columns)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Data Summary")
    st.dataframe(df.describe())

    st.subheader("🔎 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox("Select a value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.dataframe(filtered_df)

    st.subheader("📈 Plot Data (Line Chart Only)")
    numeric_columns = filtered_df.select_dtypes(include='number').columns.tolist()

    if len(numeric_columns) < 2:
        st.warning("Need at least two numeric columns to plot.")
    else:
        x_column = st.selectbox("Select X-axis", numeric_columns)
        y_column = st.selectbox("Select Y-axis", numeric_columns)

        if st.button("Generate Line Chart"):
            try:
                chart_data = filtered_df[[x_column, y_column]].dropna().sort_values(by=x_column)
                st.line_chart(chart_data.set_index(x_column))
            except Exception as e:
                st.error(f"⚠️ Could not generate chart: {e}")
else:
    st.info("👈 Please upload your 2019 World Happiness Report CSV to begin.")
