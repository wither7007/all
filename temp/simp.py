#!/usr/bin/python3.10
# Importing required module
# https://www.codespeedy.com/cut-or-trim-a-video-using-moviepy-in-python/
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from export import subdirs
import time
console = Console()
dp="/mnt/c/you/mcoding"
myf=[a for a in subdirs(dp)]
e=[' '.join(map(str, (a,b))) for a,b in enumerate(myf)][:30]
ur = [Panel(a , expand=True) for a in e]
console.print(Columns(ur))
sec = int(input('Let us wait for user input. Let me know how many seconds to sleep now.\n'))

print('Going to sleep for', sec, 'seconds.')

time.sleep(int(sec))
print(myf[sec])
print('Enough of sleeping, I Quit!')
quit()
clip='strum.mp4'
start=(4,35)
finish=(4,49)
from moviepy.editor import *
import os
import sys
searchD=r'.'
dp=os.environ.get('dir')
if dp is None:
    dp=searchD

res=[]
def subdirs(dp):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(dp):
        if entry.is_file():
            if 'mp' in entry.name:
                res.append(entry.name)
            yield entry.name

subdirs('.')
print([a for a in enumerate(res)])
# for x in subdirs(dp):
#     print(x)
# quit()
# uploading the video
video = VideoFileClip(clip)
  
video1 = video.subclip(start, finish)
video1.write_videofile('output.mp4',codec='libx264')
#time is always in seconds
# trimming some part of the video

# display clip
# video.ipython_display(width = 360)
# from moviepy.editor import *
# clip = VideoFileClip('Test_video.mp4')
# clip1 = clip.subclip((4,30),(5,15))
# clip1.write_videofile('edited.mp4',codec='libx264')
