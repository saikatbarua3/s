import streamlit as st
import pandas as pd
from PIL import Image, UnidentifiedImageError
import os

def main():
    st.title("Coach Profile Viewer")
    
    # Replace this with the path to your CSV file
    data_file = "coaches_data.csv"

    try:
        # Load the CSV data
        data = pd.read_csv(data_file)
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
                    image_path = coach_profile.iloc[0]['Picture']

                    # Debugging outputs for image path
                    st.write("Image Path:", image_path)
                    st.write("Current Working Directory:", os.getcwd())

                    try:
                        image = Image.open(image_path)
                        st.image(image, width=170, caption=f"{selected_coach}'s Picture")
                    except FileNotFoundError:
                        st.warning(f"Image file not found: {image_path}")
                    except UnidentifiedImageError:
                        st.warning(f"Could not identify image format: {image_path}")
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

            # Display career highlights (optional field)
            if 'Highlights' in coach_profile.columns and not pd.isna(coach_profile.iloc[0]['Highlights']):
                st.write(f"**Career Highlights:** {coach_profile.iloc[0]['Highlights']}")
            else:
                st.write(f"No career highlights found for {selected_coach}")
        else:
            st.warning(f"No profile information found for {selected_coach}")

if __name__ == "__main__":
    main()
