
import googleapiclient.discovery as gac


video_id = "video_id"   #影片ID
api_key = "API_KEY"  #API KEY


#取得YT留言
def yt_comments(video_id, api_key):
    youtube = gac.build('youtube', 'v3', developerKey=api_key)
    
    comments = []
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    response = request.execute()
    
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        #將回覆留言算進去
        if 'replies' in item:
            for reply in item['replies']['comments']:
                reply_text = reply['snippet']['textDisplay']
                comments.append(reply_text)
    
    return comments



comments = yt_comments(video_id, api_key)


for idx, comment in enumerate(comments, start=1):
    print(f"Comment {idx}: {comment}")

# 完整API網址
# def get_youtube_comments_api_request(video_id, api_key):
#     youtube = gac.build('youtube', 'v3', developerKey=api_key)

#     request = youtube.commentThreads().list(
#         part="snippet,replies",
#         videoId=video_id,
#         maxResults=100,
#         textFormat="plainText"
#     )
    
#     return request
# api_request = get_youtube_comments_api_request(video_id, api_key)


# print(api_request.uri)