from pytube import YouTube
import re

# pip install pytube3
# pip install pytube

DOWNLOAD_DIR = "E:\\YouTube\\Movie Trailers" # Download Locaion
VIDEO_LINK = "https://www.youtube.com/watch?v=TcMBFSGVi1c" # Your YouTube Video Link

video = YouTube(VIDEO_LINK)
yt = video.streams.get_highest_resolution() # For getting Quality available if PLaylist is Mixed
# yt = video.streams.get_by_resolution("720p") #360p
yt.download(output_path = DOWNLOAD_DIR)