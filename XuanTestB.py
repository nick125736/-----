import requests
from XuanTestA import apiKey, videoIds

    # 初始化音樂 URL 列表
audioUrls = []

    # 使用視頻詳細信息 API 獲取每個視頻的詳細信息
for videoId in videoIds:
    response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?id={videoId}&part=player&key={apiKey}')
    data = response.json()
        # 檢查是否有有效的視頻詳細信息
    if 'items' in data and len(data['items']) > 0:
            # 提取音頻 URL
        embedHtml = data['items'][0]['player']['embedHtml']
        audioUrl = embedHtml.split(' ')[3].split('"')[1]
        audioUrls.append(audioUrl)

    # 將音樂 URL 寫入文件
with open('audioUrls.txt', 'w') as f:
    for audioUrl in audioUrls:
        f.write(audioUrl + '\n')

#