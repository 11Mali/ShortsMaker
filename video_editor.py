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



def time_to_seconds(timestamps):
    minutes, seconds = map(int, timestamps.split(":"))
    return minutes * 60 + seconds


def shortMaker(clip_length,video_path, video_link,save_path):
    timestamps, video_len = chapther_grabber(video_link)
    #record start time
    start = time.time()

    #add current date to the output path
    current_date = date.today().strftime("%d-%m-%y")

    #convert timestamps to seconds
    timestamps_in_seconds = [time_to_seconds(t) for t in timestamps]

    #create output path for shorts videos
    SAVE_PATH = os.path.join(save_path, current_date)
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    for i in range(len(timestamps)):
        print("Processing subclip")
        noise = 0
        #determine start and end of clips
        noise = random.randint(0, min(40,clip_length))
        start_time = timestamps_in_seconds[i]
        end_time = (timestamps_in_seconds[i] + clip_length)  - noise

        print(f"Clip start:{start_time} clip end:{end_time} clip length:{end_time-start_time}")

        ffmpeg_extract_subclip(
                    video_path,
                    start_time,
                    end_time,
                    targetname=f"{SAVE_PATH}/short{i+1}.mp4")
            
        print(f"Clip{i} finished...")
    
    #record end time
    end = time.time()
    print(f"The time of execution of above program is : {round((end-start),2)} s")
