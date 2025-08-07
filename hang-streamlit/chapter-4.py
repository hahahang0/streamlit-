import streamlit as st
import pandas as pd 

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your csv file", type=["csv"])
if file: 
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)


if file:
    st.subheader("Summary Status.")
    st.write(df.describe(include="all"))
if file:
    occupations = df["occupation"].unique()
    selected_occupation = st.selectbox("Filter by occupation",occupations)
    filtered_data = df[df["occupation"]==selected_occupation] 
    st.dataframe(filtered_data)

    cities = df["city"].unique()
    selected_city = st.selectbox("Filter by cities",cities)
    filtered_data_cities = df[df["city"]==selected_city] 
    st.dataframe(filtered_data_cities)
    
