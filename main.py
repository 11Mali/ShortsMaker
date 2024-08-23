import streamlit as st
from pytube import YouTube
import moviepy.editor as mpe
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import requests
import re
import os
import time
from datetime import date, datetime
import random

from description_grabber import chapther_grabber
# Set the title of the app
st.title("My Streamlit App")


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


