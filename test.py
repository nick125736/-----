import requests
from textblob import TextBlob
import matplotlib.pyplot as plt

video_id = "ID"
api_key = "API"

def fetch_youtube_comments(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet,replies&videoId={video_id}&key={api_key}"
    
    # 发送API请求
    response = requests.get(url)
    data = response.json()
    
    # 提取评论
    comments = []
    for item in data['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        
        # 提取回复
        if 'replies' in item:
            for reply in item['replies']['comments']:
                reply_text = reply['snippet']['textDisplay']
                comments.append(reply_text)
    
    return comments

def analyze_sentiment(comment):
    blob = TextBlob(comment)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

comments = fetch_youtube_comments(video_id, api_key)


for idx, comment in enumerate(comments, start=1):
    sentiment = analyze_sentiment(comment)
    print(f"Comment {idx}: {comment} - Sentiment: {sentiment}")

sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
for comment in comments:
    sentiment = analyze_sentiment(comment)
    sentiments[sentiment] += 1

# 绘制柱状图
labels = list(sentiments.keys())
counts = list(sentiments.values())

plt.bar(labels, counts, color=['green', 'red', 'blue'])
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis of YouTube Comments')
plt.show()