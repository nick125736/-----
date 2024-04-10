from textblob import TextBlob


# 歌詞
lyrics = """
I love you like a love song baby
I, I love you like a love song baby
I, I love you like a love song baby
And I keep hitting re-peat-peat-peat-peat-peat-peat

I love you like a love song baby
I, I love you like a love song baby
I, I love you like a love song baby
And I keep hitting re-peat-peat-peat-peat-peat-peat
"""

blob = TextBlob(lyrics)

# 名詞、動詞、形容詞
nouns = [word for (word, tag) in blob.tags if tag.startswith('NN')]
verbs = [word for (word, tag) in blob.tags if tag.startswith('VB')]
adjectives = [word for (word, tag) in blob.tags if tag.startswith('JJ')]

# 情感相關詞語
emotional_words = ['love', 'baby', 'repeat']
emotional_words_count = sum(blob.words.count(word) for word in emotional_words)

# 積極、消極還是中性
sentiment = blob.sentiment.polarity
a=blob.sentiment
if sentiment > 0:
    sentiment_label = 'Positive'
elif sentiment < 0:
    sentiment_label = 'Negative'
else:
    sentiment_label = 'Neutral'

# 分類歌詞主題
themes = {
    'Love and Relationships': ['love', 'baby'],
    'Self-Exploration and Growth': ['repeat'],
    'Social and Political Issues': [],
    'Nature and Environment': [],
    'Music and Art': []
}

topic = ''
for theme, words in themes.items():
    for word in words:
        if word in lyrics.lower():
            topic = theme
            break
    if topic:
        break

# 輸出結果
print(a)
print("名詞數量：", len(nouns))
print("動詞數量：", len(verbs))
print("形容詞數量：", len(adjectives))
print("情感相關詞語數量：", emotional_words_count)
print("情感：", sentiment_label)
print("主題：", topic)