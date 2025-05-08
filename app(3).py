import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" Interactive Data Dashboard")

#create file upload widget (an interactive UI element that allow users to provide input)
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())
    st.write(df.tail())
    
    st.subheader("Data Summary")
    st.write(df.describe()) 
    # gives a summary of the statistical properties on numerical data in the df dataframe eg. count, std(spread of the data), 25% - 25% of data falls below xx value
    
    st.subheader("Filter Data")
    columns = df.columns.tolist() #get all column names from the dataframe df as a simple list or regular python list.
    selected_column = st.selectbox("Select colum to filter by", columns)

    unique_values = df[selected_column].unique() #access all the values in a specific column of df and return non repeating columns
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value] #filter the df to show only the rows where the values in a specific column matches a certain value.
    st.write(filtered_df)

    st.header("Plot Data")
    x_column = st.selectbox("Select x_axis column", columns)
    y_column = st.selectbox("Select y_axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else: 
    st.write("waiting on file upload...")
