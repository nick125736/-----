from googleapiclient.discovery import build
from API import api_key as apiKey

# 在 Google Cloud Console 中獲取的 API 金鑰

# 使用 Google API 構建 YouTube 服務
youtube = build('youtube', 'v3', developerKey=apiKey)

# 搜索類型為音樂的影片
request = youtube.search().list(
    q='流行歌曲',  # 搜索關鍵詞，例如流行歌曲
    part='snippet',
    type='video',
    maxResults=100  # 返回結果的最大數量，這裡設置為 100
)

# 執行搜索請求並獲取結果
response = request.execute()

# 提取搜索結果中的影片 ID
videoIds = [item['id']['videoId'] for item in response['items']]

