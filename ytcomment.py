
import googleapiclient.discovery as gac
from textblob import TextBlob as tb
import re
import csv
import os
from API import api_key


video_id = "vk_xq1P7vIU"   #影片ID



#取得YT留言
def yt_comments(video_id, api_key, max_results=100):
    youtube = gac.build('youtube', 'v3', developerKey=api_key)
    
    comments = []
    nextPageToken = None
    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            maxResults=min(100, max_results - len(comments)),
            textFormat="plainText",
            pageToken=nextPageToken
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
        
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken or len(comments) >= max_results:
            break
    
    return comments
#清理留言
def clean_comment(comment):
    # 移除表情符號
    clean_comment = re.sub(r'[^\x00-\x7F]+', ' ', comment)
    # 移除非英文字符
    clean_comment = re.sub(r'[^a-zA-Z\s]', '', clean_comment)
    # 移除多餘的空格
    clean_comment = re.sub(r'\s+', ' ', clean_comment).strip()
    return clean_comment

comments = yt_comments(video_id, api_key, max_results=500)

cleaned_comments = [clean_comment(comment) for comment in comments if clean_comment(comment)]


polarities = []
subjectivities = []


for comment in comments:
    cleaned_comment = clean_comment(comment)
    if cleaned_comment:
        analysis = tb(cleaned_comment).sentiment
        polarity = analysis.polarity
        subjectivity = analysis.subjectivity
        if polarity != 0 or subjectivity != 0:
            cleaned_comments.append(cleaned_comment)
            polarities.append(polarity)
            subjectivities.append(subjectivity)

cleaned_comments = cleaned_comments[:100]
polarities = polarities[:100]
subjectivities = subjectivities[:100]


os.makedirs('csv', exist_ok=True)

csv_file_path = os.path.join('csv', f'{video_id}.csv')
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['serial_number', 'comment', 'polarities', 'subjectivities'])
    for idx, (comment, polarity, subjectivity) in enumerate(zip(cleaned_comments, polarities, subjectivities), start=1):
        writer.writerow([idx, comment, polarity, subjectivity])
        print(f"Comment {idx}: {comment}")
        print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")


# #完整API網址
# def get_youtube_comments_api_request(video_id, api_key):
#     youtube = gac.build('youtube', 'v3', developerKey=api_key)

#     request = youtube.commentThreads().list(
#         part="snippet,replies",
#         videoId=video_id,
#         maxResults=200,
#         textFormat="plainText"
#     )
    
#     return request
# api_request = get_youtube_comments_api_request(video_id, api_key)


# print(api_request.uri)

