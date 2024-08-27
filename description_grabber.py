from pytube import YouTube
import moviepy.editor as mpe
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import requests
import re
import os
import time
from datetime import date, datetime
import random


def chapther_grabber(video_link):
    #record start time
    start_time = time.time()

    yt = YouTube(video_link)
    print("Video found")

    #saved the description in a string variable. want to remove the chapterstamps out into its own list
    url = requests.get(video_link).text
    search = re.search(r'shortDescription":"', url)
    description = ""
    print("Description found")

    count = search.start() + 19  # adding the length of the 'shortDescription":"
    while True:
        # get the letter at current index in text
        letter = url[count]
        if letter == "\"":
            if url[count - 1] == "\\":
                # this is case where the letter before is a backslash, meaning it is not real end of description
                description += letter
                count += 1
            else:
                break
        else:
            description += letter
            count += 1

    print(f'Description: {description}')

    #length of video - converted to timestamp format
    video_len = yt.length

    seconds = video_len % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    video_len = ("%02d:%02d" % (minutes, seconds)) # Format --> MM:SS

    print(f"Length of video {video_len} min")

    #extract timestamps
    timestamps = re.findall(r"\d+:\d+",description)
    print(f"Found {len(timestamps)} timestamps")

    #record end time
    end_time = time.time()

    print(f"The time of execution of above program is : {round((end_time-start_time),2)} s")
    
    return timestamps , video_len
