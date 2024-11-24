import streamlit as st
import pandas as pd
from PIL import Image, UnidentifiedImageError
import os

def main():
    st.title("Coach Profile Viewer")

    # Path to the CSV files
    profile_file = "coaches_data.csv"
    batting_file = "all_coaches_batting.csv"
    bowling_file = "All_Coach_Bowling_Stats.csv"

    # Load the CSV files
    try:
        profile_data = pd.read_csv(profile_file, encoding='cp1252')
        batting_data = pd.read_csv(batting_file)
        bowling_data = pd.read_csv(bowling_file)
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return
    except Exception as e:
        st.error(f"Error loading the data: {e}")
        return

    # Ensure consistent matching: lowercase all names
    profile_data['Coach_Name'] = profile_data['Coach_Name'].str.lower()
    batting_data['Player Name'] = batting_data['Player Name'].str.lower()
    bowling_data['Player Name'] = bowling_data['Player Name'].str.lower()

    # Extract unique coach names
    coach_names = sorted(profile_data['Coach_Name'].unique())

    # Select a coach
    selected_coach = st.selectbox("Select a Coach", coach_names)

    if selected_coach:
        # Filter the selected coach profile
        coach_profile = profile_data[profile_data['Coach_Name'] == selected_coach]

        # Debugging: Show the filtered data for verification
        #st.write(f"**Debugging Selected Coach:** {selected_coach}")
        #st.write("Coach Profile Data:")
        #st.write(coach_profile)

        if not coach_profile.empty:
            st.write(f"**{selected_coach.title()} Profile**")

            # Create two columns for image and profile details
            col1, col2 = st.columns([1, 2])

            # Display image in the first column
            with col1:
                image_path = coach_profile.iloc[0].get('Picture', None)
                if image_path:
                    if not image_path.startswith("assets/"):
                        image_path = os.path.join("assets", "images", "Abbas Ali Baig.JPG")
                    try:
                        image = Image.open(image_path)
                        st.image(image, width=170, caption=f"{selected_coach.title()}'s Picture")
                    except F	ileNotFoundError:
                        st.warning(f"Image not found: {image_path}")
                    except UnidentifiedImageError:
                        st.warning(f"Invalid image format: {image_path}")
                    except Exception as e:
                        st.error(f"Error displaying image: {e}")
                else:
                    st.write("No picture available.")

            # Display profile details in the second column
            with col2:
                st.markdown(f"**Coach Name:** {coach_profile.iloc[0]['Coach_Name'].title()}")
                st.markdown(f"**Born In:** {coach_profile.iloc[0]['Born_in']}")
                st.markdown(f"**Age:** {coach_profile.iloc[0]['Age']}") 
                st.markdown(f"**Status:** {coach_profile.iloc[0]['Status']}")

            # Career highlights
            highlights = coach_profile.iloc[0].get('Highlights', None)
            if highlights:
                st.write("**Career Highlights:**")
                for highlight in highlights.split(". "):
                    if highlight.strip():
                        st.write(f"- {highlight.strip()}")
            else:
                st.write("No career highlights available.")

        # Batting stats
        batting_profile = batting_data[batting_data['Player Name'] == selected_coach]
        #st.header(f"{selected_coach.title()} Batting Stats")
        if not batting_profile.empty:
            key_batting_columns = ['Format', 'Runs', 'Ave', '100s', '50s', 'Strike_Rate', 'HS']
            other_batting_columns = ['Format', 'Mat', 'Inns', 'BF', 'Catch', 'Stump']
            
            st.subheader("Key Batting Stats during cricket career")
            st.table(batting_profile[key_batting_columns])
            
            st.subheader("Other Batting Stats")
            st.table(batting_profile[other_batting_columns])
        else:
            st.warning(f"No batting stats found for {selected_coach.title()}.")

        # Bowling stats
        bowling_profile = bowling_data[bowling_data['Player Name'] == selected_coach]
        #st.header(f"{selected_coach.title()} Bowling Stats")
        if not bowling_profile.empty:
            key_bowling_columns = ['Format', 'Wkts', 'BBI', 'Ave', 'Econ', 'SR', '5w', '10w']
            other_bowling_columns = ['Format', 'Mat', 'Inns', 'Balls', 'Runs', 'BBM', '4w', 'Tournament', 'Teams']
            
            st.subheader("Key Bowling Stats during cricket career")
            st.table(bowling_profile[key_bowling_columns])
            
            st.subheader("Other Bowling Stats")
            st.table(bowling_profile[other_bowling_columns])
        else:
            st.warning(f"No bowling stats found for {selected_coach.title()}.")

if __name__ == "__main__":
    main()
