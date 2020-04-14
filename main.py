import nltk
import random
import json
import re
import urllib.request
from pytube import YouTube

api_key=""
video_id=""
url= f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

json_url =urllib.request.urlopen(url)
data=json.loads(json_url.read())
print(data)
