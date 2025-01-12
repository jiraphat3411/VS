# from moviepy.editor import VideoFileClip
from moviepy import VideoFileClip

videoClip = VideoFileClip("Av-new_0.mp4")
videoClip.write_gif("export.gif")