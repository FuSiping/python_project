import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import os
import re



# 去掉停用词
def remove_stop_words(f):
    stop_words = ['你好', '已添加', '现在', '可以', '开始', '聊天', '当前', '群聊', '人数', '过多', '显示', '群成员', '昵称', '信息页', '关闭', '参与人',
                  '还有', '嗯', '的', '是', '他', '你', '了', '人', '我', '就']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f

# 生成词云
def create_word_cloud():
    print('生成词云!')
    # 设置本地的simhei字体文件位置
    FONT_PATH = os.environ.get("FONT_PATH", os.path.join(os.path.dirname(__file__), "simhei.ttf"))
    with open('test.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    text = remove_stop_words(text)
    cut_text = " ".join(jieba.cut(text, cut_all=False, HMM=True))
    maskIm = Image.open('love2.png')
    size = maskIm.size
    wc = WordCloud(
        font_path=FONT_PATH,
        background_color="white",
        max_words=100,
        width=size[0],
        height=size[1],
        mask=np.array(maskIm)
    )
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
# 将聊天记录生成词云
create_word_cloud()