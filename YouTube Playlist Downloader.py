from pytube import Playlist
from pytube import YouTube
import re

# pip install pytube3
# pip install pytube

DOWNLOAD_DIR = "E:\\YouTube\\Movie Trailers" # Download Locaion
PLAYLIST_LINK = "https://www.youtube.com/playlist?list=PLPajMbLqLKBIvSZkDFmkzkPwZj2HcSWyh" # Your YouTube Playlist Link

playlist = Playlist(PLAYLIST_LINK)
print(len(playlist.video_urls)) # It's Print Howmany Videos in Playlist

count = 1
for url in playlist.video_urls:
    video = YouTube(url)
    yt = video.streams.get_highest_resolution() # For getting Quality available if PLaylist is Mixed 
    # yt = video.streams.get_by_resolution("720p") #360p
    yt.download(output_path = DOWNLOAD_DIR, filename = None, filename_prefix = f"{count} ") # Delete filename_prefix if you want as it is name
    count += 1