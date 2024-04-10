from snownlp import SnowNLP
from textblob import TextBlob

text = "the song is so beautifulllllllll"


blob = TextBlob(text)
snow = SnowNLP(text)

# 分析情感
sentiment_score = blob.sentiment
sentiment_score1 = snow.sentiments


# # 判斷情感
# if sentiment_score > 0:
#     sentiment = "正面"
# elif sentiment_score < 0:
#     sentiment = "負面"
# else:
#     sentiment = "中性"

# 輸出結果
print(f"情感分數: {sentiment_score}")
# print(f"情感: {sentiment}")
print(f"情感分數: {sentiment_score1}")

