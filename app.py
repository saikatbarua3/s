# import streamlit as st
# import sqlite3
# import pandas as pd

# # Function to connect to the SQLite database
# def get_data_from_sql():
#     conn = sqlite3.connect('database.db')
#     query = "SELECT * FROM users"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Function to initialize the database with sample data
# def init_db():
#     conn = sqlite3.connect('database.db')
#     with open('database.sql', 'r') as f:
#         conn.executescript(f.read())
#     conn.close()

# # Initialize the database
# init_db()

# # Streamlit UI
# st.title("Streamlit with SQLite Example")
# st.write("This app fetches data from a SQLite database and displays it below.")

# # Fetch data from SQLite
# data = get_data_from_sql()

# # Display data in a table
# st.dataframe(data)

# # Allow user to add new data
# st.subheader("Add New User")
# name = st.text_input("Enter Name")
# age = st.number_input("Enter Age", min_value=18, max_value=100)

# if st.button("Add User"):
#     if name and age:
#         conn = sqlite3.connect('database.db')
#         conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
#         conn.commit()
#         conn.close()
#         st.success("User added successfully!")
#     else:
#         st.error("Please provide both name and age.")


# import mysql.connector
# import streamlit as st
# from PIL import Image

import streamlit as st
import pandas as pd

# Load the CSV file
data = pd.read_csv('coaches_data.csv')

# Display the data
st.write("Data from the CSV file:")
st.dataframe(data)



# def get_database_connection():
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",  # Your MySQL host, e.g., 'localhost' or an IP address
#             user="root",       # Your MySQL username
#             password="sa0Oat", # Your MySQL password
#             database="cricket_db"  # Your database name
#         )
#         return conn
    # except mysql.connector.Error as e:
    #     st.error(f"Error connecting to database: {e}")
    #     return None

# def get_coach_names(conn):
#     try:
#         query = "SELECT DISTINCT Coach_Name FROM Coaches"
#         cursor = conn.cursor()
#         cursor.execute(query)
#         result = cursor.fetchall()
#         #st.write(f"Fetched coach names: {result}")  # Debugging output
#         return [row[0] for row in result]  # Only extracting Coach_Name
#     except mysql.connector.Error as e:
#         st.error(f"Error fetching coach names: {e}")
#         return []

# def get_coach_profile(conn, coach_name):
#     try:
#         query = "SELECT Coach_ID, Coach_Name, Born_in, Age, Coaching_Year, Status, Picture FROM Coaches WHERE Coach_Name = %s"
#         cursor = conn.cursor()
#         cursor.execute(query, (coach_name,))
#         result = cursor.fetchall()
#         cursor.close()
#         #st.write(f"Fetched coach profile: {result}")  # Debugging output
#         return result
#     except mysql.connector.Error as e:
#         st.error(f"Error fetching coach profile: {e}")
#         return []

# def get_coaching_highlights(conn, coach_name):
#     try:
#         query = "SELECT section_title, section_content FROM coaching_career_highlights WHERE Coach_Name = %s"
#         cursor = conn.cursor()
#         cursor.execute(query, (coach_name,))
#         result = cursor.fetchall()
#         cursor.close()
#         #st.write(f"Fetched coaching highlights: {result}")  # Debugging output
#         return result
#     except mysql.connector.Error as e:
#         st.error(f"Error fetching coaching highlights: {e}")
#         return []

# def main():
#     st.title("Coach Profile Viewer")
#     conn = get_database_connection()

#     if conn:
#         #st.write("Database connected successfully.")
        
#         # Fetch coach names and display them in a selectbox
#         coach_names = get_coach_names(conn)
#         if coach_names:
#             selected_coach = st.selectbox("Select Coach", coach_names)

#             if selected_coach:
#                 # Fetch and display the coach's profile
#                 coach_profile = get_coach_profile(conn, selected_coach)
#                 if coach_profile:
#                     st.write(f"**{selected_coach} Profile**")

#                     # Create two columns: one for the image and one for the text
#                     col1, col2 = st.columns([1, 2])

#                     # Display the image in the first column with width of 170px
#                     with col1:
#                         for profile in coach_profile:
#                             if profile[6]:  # Check if Picture exists
#                                 image = Image.open(profile[6])
#                                 st.image(image, width=170)
#                             else:
#                                 st.write("No picture available.")

#                     # Display the text in the second column
#                     with col2:
#                         for profile in coach_profile:
#                             st.markdown(f"**Coach Name:** {profile[1]}")
#                             st.markdown(f"**Born In:** {profile[2]}")
#                             st.markdown(f"**Age:** {profile[3]}")
#                             #st.markdown(f"**Coaching Year:** {profile[4]}")
#                             st.markdown(f"<p style='text-align: justify;'><strong>Status: {profile[5]}</strong></p>", unsafe_allow_html=True)

#                     # Fetch and display the coaching career highlights
#                     career_highlights = get_coaching_highlights(conn, selected_coach)
#                     if career_highlights:
#                         st.write(f"**Coaching Career Highlights of {selected_coach}:**")
#                         for highlight in career_highlights:
#                             if len(highlight) >= 2:
#                                st.markdown(f"<p style='text-align: justify;'><strong>- {highlight[0]}:</strong> {highlight[1]}</p>", unsafe_allow_html=True)
#                     else:
#                         st.write(f"No coaching career highlights found for {selected_coach}")
#                 else:
#                     st.write(f"No profile found for {selected_coach}")
#         else:
#             st.write("No coach names found.")
#     else:
#         st.write("Failed to connect to database.")

# if __name__ == "__main__":
    main()






