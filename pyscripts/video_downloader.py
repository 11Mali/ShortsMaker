from pytube import YouTube
import moviepy.editor as mpe
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import requests
import re
import os
import time
from datetime import date, datetime
import random


def ytv_downloader(video_link):
    #record start time
    start_time = time.time()

    # Specify the folder path, 
    SAVE_PATH = "/home/mali/repurpose/videofolder" # this folder will be accessed in video_chop.py
    ytv = YouTube(video_link)

    video_name = f"{ytv.title}_clip.mp4"
    audio_name = f"{ytv.title}_audio.mp3"

    # Download video and rename
    video = ytv.streams.filter(subtype='mp4', res="1080p").first()
    print("downloading video...")
    video_path = video.download(output_path = SAVE_PATH)
    new_video_path = os.path.join(SAVE_PATH, video_name)
    os.rename(video_path, new_video_path)
    print("video finished downloading.")

    # Download audio and rename
    audio = ytv.streams.filter(only_audio=True).first()
    print("downloading audio...")
    audio_path = audio.download(output_path = SAVE_PATH)
    new_audio_path = os.path.join(SAVE_PATH, audio_name)
    os.rename(audio_path, new_audio_path)
    print("audio finished downloading.")

    # Setting the audio to the video
    video = mpe.VideoFileClip(new_video_path)
    audio = mpe.AudioFileClip(new_audio_path)
    final = video.set_audio(audio)

    # Output result
    output_name = f"{ytv.title}_concat.mp4"
    output_path = os.path.join(SAVE_PATH, output_name)
    final.write_videofile(output_path)

    # Delete video and audio to keep the result
    os.remove(new_video_path)
    os.remove(new_audio_path)


    print(f"here is the url {video_link}")
    
    #record end time
    end_time = time.time()

    print(f"The time of execution of above program is : {round((end_time-start_time),2)} s")
    return video_link

#the only global variable is the link
#ytv_url = ytv_downloader("https://www.youtube.com/watch?v=phOkyQo7rjo")