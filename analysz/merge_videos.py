import os
try:
    from moviepy.editor import *
except:
    os.system("pip install moviepy")
    from moviepy.editor import *

video_paths = ['./vis/demo1.mp4', './vis/demo2.mp4', './vis/demo3.mp4']  # in-order
temp = [VideoFileClip(i) for i in video_paths]

print('[*] ====> merge videos <=====')
final_clip = concatenate_videoclips(temp)
final_clip.to_videofile("./target.mp4", fps=20, remove_temp=False)
