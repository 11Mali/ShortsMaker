import streamlit as st

# Set the title of the app
st.title("My Streamlit App")

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("You can add widgets here")

# Main content area
st.write("Welcome to my Streamlit app!")

# Example of adding a slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"The selected value is {slider_value}")


# User input for YouTube video link
video_link = st.text_input("Enter YouTube video link")

if video_link:
    timestamps, video_len = chapter_grabber(video_link)
    st.write("Timestamps:", timestamps)
    st.write("Video Length:", video_len)


# Example of adding a button
if st.button("Click me"):
    st.write("Button clicked!")

# Example of adding a text input
user_input = st.text_input("Enter some text")
st.write(f"You entered: {user_input}")


