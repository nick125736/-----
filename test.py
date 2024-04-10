import requests
from textblob import TextBlob
import matplotlib.pyplot as plt

video_id = "ID"
api_key = "API"

def fetch_youtube_comments(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet,replies&videoId={video_id}&key={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    comments = []
    for item in data['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        
        if 'replies' in item:
            for reply in item['replies']['comments']:
                reply_text = reply['snippet']['textDisplay']
                comments.append(reply_text)
    
    return comments



