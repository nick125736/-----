import googleapiclient.discovery as gac
import json

video_id = ""   #影片ID
api_key = ""  #API KEY


def yt_infor(video_id, api_key):
    youtube = gac.build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    
    return request


a = yt_infor(video_id, api_key)
response = a.execute()



print(json.dumps(response, indent=2, ensure_ascii=False))
print(a.uri)