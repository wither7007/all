#important 
# C:\Python39\python.exe
# keep to slice mp4 videos
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob
from my import *

files = glob.glob("*.mp4")
f1 = []
# print the glob
for count, value in enumerate(files):
    f1.append(f"{count} {value}")
col_print(f1)
# input and cut
filenumber = int(input("File number: "))
start = int(input("Start: "))
end = int(input("End: "))

fname = f"{start}_{end}{files[filenumber]}"
ffmpeg_extract_subclip(files[filenumber], start, end, targetname=fname)
