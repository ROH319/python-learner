import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


with open('governmentreport.txt', 'r', encoding='utf-8') as file:
    text = file.read()



words = jieba.lcut(text)


stopwords = set(['的', '了', '和', '是', '就', '都', '而', '及', '与', '着', '等', '以及', '其他', '左右', '以上', '报告', '增长', '减少', '约', '前后'])


words_cleaned = [word for word in words if word not in stopwords and word.strip() != '' and len(word.strip()) > 1]


word_freq = {}
for word in words_cleaned:
    word_freq[word] = word_freq.get(word, 0) + 1


font_path = 'C:/Windows/Fonts/msyh.ttc'  
wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate_from_frequencies(word_freq)


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.show()
