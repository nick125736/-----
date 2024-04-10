import googleapiclient.discovery as gac
import json
import requests
from API import api_key

video_id = "vk_xq1P7vIU"   #影片ID
api = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"

def yt_infor(video_id, api_key):
    youtube = gac.build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    
    return request


a = yt_infor(video_id, api_key).execute()

api = requests.get(api).json()

dislikes = api['dislikes']
likes = api['likes']
viewcount = api['viewCount']

print(dislikes, likes, viewcount)


