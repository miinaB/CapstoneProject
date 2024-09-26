from pytube import YouTube
from pytube. innertube import _default_clients

_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]

# where to save
SAVE_PATH = "./videos" #to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=_KPrTIK5zPs"

try:
    # object creation using YouTube
    yt = YouTube(link)
except:
    #to handle exception
    print("Connection Error")

# Get all streams and filter for mp4 files
d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# get the video with the highest resolution
# d_video = mp4_streams[-1]

try:
    # downloading the video
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except:
    print("Some Error!")