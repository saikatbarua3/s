import streamlit as st
import pandas as pd

# Load the CSV file
data = pd.read_csv('coaches_data.csv')

# Display the data
st.write("Data from the CSV file:")
st.dataframe(data)

def main():
    st.title("Coach Profile Viewer")
    conn = get_database_connection()

    if conn:
        #st.write("Database connected successfully.")
        
        # Fetch coach names and display them in a selectbox
        coach_names = get_coach_names(conn)
        if coach_names:
            selected_coach = st.selectbox("Select Coach", coach_names)

            if selected_coach:
                # Fetch and display the coach's profile
                coach_profile = get_coach_profile(conn, selected_coach)
                if coach_profile:
                    st.write(f"**{selected_coach} Profile**")

                    # Create two columns: one for the image and one for the text
                    col1, col2 = st.columns([1, 2])

                    # Display the image in the first column with width of 170px
                    with col1:
                        for profile in coach_profile:
                            if profile[6]:  # Check if Picture exists
                                image = Image.open(profile[6])
                                st.image(image, width=170)
                            else:
                                st.write("No picture available.")

                    # Display the text in the second column
                    with col2:
                        for profile in coach_profile:
                            st.markdown(f"**Coach Name:** {profile[1]}")
                            st.markdown(f"**Born In:** {profile[2]}")
                            st.markdown(f"**Age:** {profile[3]}")
                            #st.markdown(f"**Coaching Year:** {profile[4]}")
                            st.markdown(f"<p style='text-align: justify;'><strong>Status: {profile[5]}</strong></p>", unsafe_allow_html=True)

                    # Fetch and display the coaching career highlights
                    career_highlights = get_coaching_highlights(conn, selected_coach)
                    if career_highlights:
                        st.write(f"**Coaching Career Highlights of {selected_coach}:**")
                        for highlight in career_highlights:
                            if len(highlight) >= 2:
                               st.markdown(f"<p style='text-align: justify;'><strong>- {highlight[0]}:</strong> {highlight[1]}</p>", unsafe_allow_html=True)
                    else:
                        st.write(f"No coaching career highlights found for {selected_coach}")
                else:
                    st.write(f"No profile found for {selected_coach}")
        else:
            st.write("No coach names found.")
    else:
        st.write("Failed to connect to database.")

if __name__ == "__main__":
    main()
