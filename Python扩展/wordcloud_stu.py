# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 10:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wordcloud_stu.py
# @Software: PyCharm

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 也可以使用 PIL
wc = WordCloud(background_color='white')
string = 'Importance of relative word frequencies for font-size. With relative_scaling=0, only word-ranks are considered. With relative_scaling=1, a word that is twice as frequent will have twice the size. If you want to consider the word frequencies and not only their rank, relative_scaling around .5 often looks good.'

wc.generate(string)
wc.to_file('pic.png')
plt.imshow(wc)
plt.axis("off")
plt.show()