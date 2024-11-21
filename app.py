import streamlit as st
import sqlite3
import pandas as pd

# Function to connect to the SQLite database
def get_data_from_sql():
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM users"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to initialize the database with sample data
def init_db():
    conn = sqlite3.connect('database.db')
    with open('database.sql', 'r') as f:
        conn.executescript(f.read())
    conn.close()

# Initialize the database
init_db()

# Streamlit UI
st.title("Streamlit with SQLite Example")
st.write("This app fetches data from a SQLite database and displays it below.")

# Fetch data from SQLite
data = get_data_from_sql()

# Display data in a table
st.dataframe(data)

# Allow user to add new data
st.subheader("Add New User")
name = st.text_input("Enter Name")
age = st.number_input("Enter Age", min_value=18, max_value=100)

if st.button("Add User"):
    if name and age:
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
        st.success("User added successfully!")
    else:
        st.error("Please provide both name and age.")


