import tkinter as tk
from tkinter import filedialog, messagebox

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
from video_editor import time_to_seconds
from video_editor import shortMaker
from video_downloader import ytv_downloader

#creating app
app = tk.Tk()
app.title("Short maker")

#file upload
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mov *.avi")])
    if file_path:
        video_path_entry.delete(0, tk.END)
        video_path_entry.insert(0, file_path)

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, directory_path)

#process the video
def process_video():
    video_path = video_path_entry.get()
    video_link = video_link_entry.get()
    save_path = save_path_entry.get()
    clip_length = int(clip_length_entry.get())
    download_video = download_var.get()

    if not video_path and not video_link:
        messagebox.showerror("Error", "Please provide either a video path or a youtube link")
        return

    if download_video and video_link:
        video_path = ytv_downloader(video_link)

    shortMaker(clip_length, video_path, video_link,save_path)
    messagebox.showinfo("Success", "Video processing completed")

#create video link widgets
tk.Label(app, text="YouTube video link:").grid(row=0, column=0, padx=10, pady=10)
video_link_entry = tk.Entry(app, width=50)
video_link_entry.grid(row=0, column=1, padx=10, pady=10)

#create video link widgets
tk.Label(app, text="Video file path:").grid(row=1, column=0, padx=10, pady=10)
video_path_entry = tk.Entry(app, width=50)
video_path_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=upload_file).grid(row=1, column=2, padx=10, pady=10)

#create save path widgets
tk.Label(app, text="Save path:").grid(row=2, column=0, padx=10, pady=10)
save_path_entry = tk.Entry(app, width=50)
save_path_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_directory).grid(row=2, column=2, padx=10, pady=10)

#create clip length widgets
tk.Label(app, text="Clip length (seconds):").grid(row=3, column=0, padx=10, pady=10)
clip_length_entry = tk.Entry(app, width=10)
clip_length_entry.grid(row=3, column=1, padx=10, pady=10)

download_var = tk.BooleanVar()
tk.Checkbutton(app, text="Download video from youtube", variable=download_var).grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(app, text="Process video", command=process_video).grid(row=5, column=0, columnspan=3, pady=20)

#run the app
app.mainloop()