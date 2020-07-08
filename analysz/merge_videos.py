import os
try:
    from moviepy.editor import *
except:
    os.system("pip install moviepy")
    from moviepy.editor import *

video_paths = ['./vis/demo1.mp4', './vis/demo2.mp4', './vis/demo3.mp4']  # in-order
print('[*] ====> merge videos <=====')
final_clip = concatenate_videoclips(video_paths)
final_clip.to_videofile("./target.mp4", fps=20, remove_temp=False)
