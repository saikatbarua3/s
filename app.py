import streamlit as st
import pandas as pd

# Load the CSV file
data = pd.read_csv('coaches_data.csv')

# Display the data
st.write("Data from the CSV file:")
st.dataframe(data)

