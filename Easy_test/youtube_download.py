from pytube import YouTube

link = ""
video = YouTube(link)
#video.bypass_age_gate()
stream = video.streams.get_highest_resolution()
stream.download()