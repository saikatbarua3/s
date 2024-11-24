import streamlit as st
import pandas as pd
from PIL import Image, UnidentifiedImageError
import os

def main():
    st.title("Coach Profile Viewer")

    # Path to the CSV file
    data_file = "coaches_data.csv"

    try:
        # Load the CSV data with a specific encoding
        data = pd.read_csv(data_file, encoding='cp1252')
    except FileNotFoundError:
        st.error("The coaches data file was not found. Please check the file path.")
        return
    except Exception as e:
        st.error(f"Error loading the data: {e}")
        return

    # Extract unique coach names
    coach_names = data['Coach_Name'].unique().tolist()

    # Display the coach names in a selectbox
    selected_coach = st.selectbox("Select a Coach", coach_names)

    if selected_coach:
        # Filter the data for the selected coach
        coach_profile = data[data['Coach_Name'] == selected_coach]

        if not coach_profile.empty:
            st.write(f"**{selected_coach} Profile**")

            # Create two columns for image and profile details
            col1, col2 = st.columns([1, 2])

            # Display image in the first column
            with col1:
                if not pd.isna(coach_profile.iloc[0]['Picture']):  # Check if the picture column is not empty
                    relative_image_path = coach_profile.iloc[0]['Picture']
                    
                    # Prepend 'assets/images/' to the relative image path if not already included
                    if not relative_image_path.startswith("assets/images/"):
                        relative_image_path = os.path.join("assets/images", relative_image_path)
                    
                    # Check for .JPG or .jpg
                    if not os.path.isfile(relative_image_path):
                        relative_image_path = relative_image_path.replace(".jpg", ".JPG")

                    # Debugging: Display the image path
                    st.write(f"Image Path: {relative_image_path}")

                    try:
                        # Open and display the image
                        image = Image.open(relative_image_path)
                        st.image(image, width=170, caption=f"{selected_coach}'s Picture")
                    except FileNotFoundError:
                        st.warning(f"Image file not found: {relative_image_path}")
                    except UnidentifiedImageError:
                        st.warning(f"Could not identify image format: {relative_image_path}")
                    except Exception as e:
                        st.error(f"Error displaying image: {e}")
                else:
                    st.write("No picture available.")

            # Display profile details in the second column
            with col2:
                st.markdown(f"**Coach Name:** {coach_profile.iloc[0]['Coach_Name']}")
                st.markdown(f"**Born In:** {coach_profile.iloc[0]['Born_in']}")
                st.markdown(f"**Age:** {coach_profile.iloc[0]['Age']}") 
                st.markdown(f"**Status:** {coach_profile.iloc[0]['Status']}")

            # Display career highlights (formatted as a bullet-pointed list)
            if 'Highlights' in coach_profile.columns and not pd.isna(coach_profile.iloc[0]['Highlights']):
                highlights = coach_profile.iloc[0]['Highlights']
                
                # Split highlights into list items, assuming they are separated by ". " or newline
                highlights_list = highlights.split(". ")
                st.write("**Career Highlights:**")
                for highlight in highlights_list:
                    if highlight.strip():  # Avoid empty strings
                        st.write(f"- {highlight.strip()}")
            else:
                st.write(f"No career highlights found for {selected_coach}")
        else:
            st.warning(f"No profile information found for {selected_coach}")

if __name__ == "__main__":
    main()
