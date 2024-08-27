# Shorts maker for creators

**This is a present to my brother.**

He enjoys coding and sharing his work on Twitch.tv. The issue lies in him not being the best editor or having the time to edit.

---

# Usage

How to use in version 1. Pointing out the elephant in the room first. The elephant being dimension of videos. Short/clips are usually in the format 9:16 (portrait), and longform are generally 16:9 (landscape).

- The method is too export two video, one in landscape and one portrait. Thereafter post the landscape like usual with description and chapters.

- Thereafter input the video link in the app, where the description has chapter stamps.

- Select shorts/clips path and portrait video paths. 

- Process the video and save shorts/clips.

PS: In case of lost footage or longer streams which have not been saved. it is possible to download with video link

---

### Aim 

 - Make longer form content(+60 min) to shorter videos that can be uploaded.

In the first iteration of the code i aim to make shorts(60 s) clips from his streams, before aiming for full youtube videos(+10 min).

### Challenge

 - Define what content in the stream is worth repurposeing.

How do i define worth? currently i havent figured it out leading into the next question. 
What does the market do? Currently the market extracts the audio from the videos, which is then analysed by a language model.
Using an Openai model and defining a prompt may be a resonable solution.


### Limitation
- The limitations i have encountered while searching for this solution prior to determining that i would code it myself are:

- Web Applications Only - All current solutions are web applications. I haven’t found any desktop applications that offer the features I need.
- Slow Processing Time - During testing, I noticed that one of the web apps had a very long processing time.
- Audio-Only Content Analysis - The current web apps analyze content using audio only.
- Output Video Length Limit - The current web apps have a maximum output video length of 3 minutes.
- Cost - Subscribtion service with tiered system.

---

### Journal 

The long proccessing time when downloading video occurs when downloading from youtube using a link.

Anothor point to think about is dimention sizing. Videos on youtube are generally 16:9 and short are generally 9:16
                  
The aim currently is to seperate the video into chapter segments based on the videos timestamps before thinking about content analysis. Call it iteration 1!

The solution for indentifying chapters based on timestamps can be improved. Current solution http requests.

Pytube yt.download function is currently not working.To fix the problem, you have to add some lines in their package
The solution is here (Forum): https://github.com/pytube/pytube/issues/1954

In this version i added random noise to vary the length of the outcome clips. This was added to see if my brothers clips would perform better at different duration. There is only duration changes at the end of the clips as the clips start at the begining of a chapter segment.

I identified why the existing web applications that provide the same service take soo long. They are downloading the video as it is not able to manipulate the video without a temporary clone.
Therefore they recommend using shorter video (+-15).

---

### Future

Future improvements will include:
- The possibility to download from different video sharing plattforms
- Adding custom timestamps in the GUI or import a text file.
- Creating a cleaner GUI (Not my best area).
- Templates for the output shorts which would would create subtitle or write a title on the output
- Adding machine learning for audio and video processing /content analysis (Alternative to chapter segmentation)

Further usertesting will be needed prior to starting on iteration 2.

**Here you go lil bro!!!**
