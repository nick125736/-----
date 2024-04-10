from googleapiclient.discovery import build
import re
from API import api_key as apiKey

# 在 Google Cloud Console 中獲取的 API 金鑰

# 使用 Google API 構建 YouTube 服務
youtube = build('youtube', 'v3', developerKey=apiKey)

# 搜索類型為音樂的影片
request = youtube.search().list(
    q='流行歌曲',  # 搜索關鍵詞，例如流行歌曲
    part='snippet',
    type='video',
    maxResults=50  # 返回結果的最大數量，這裡設置為 50
)

# 執行搜索請求並獲取結果
response = request.execute()

# 提取搜索結果中的影片 ID
videoIds = [item['id']['videoId'] for item in response['items']]

# 初始化影片 URL 列表
videoUrls = []

# 使用視頻詳細信息 API 獲取每個視頻的詳細信息
for videoId in videoIds:
    video_request = youtube.videos().list(
        part='contentDetails',
        id=videoId
    )
    video_response = video_request.execute()
    # 提取影片時長
    duration = video_response['items'][0]['contentDetails']['duration']
    # 使用正則表達式提取時長中的分鐘數
    match = re.search(r'PT(\d+)M', duration)
    if match:
        minutes = int(match.group(1))
        if minutes >= 1 and minutes <= 5:
            videoUrls.append(f'https://www.youtube.com/watch?v={videoId}')

# 將影片 URL 寫入文件
with open('videoUrls.txt', 'w') as f:
    for videoUrl in videoUrls:
        f.write(videoUrl + '\n')

#不能使用