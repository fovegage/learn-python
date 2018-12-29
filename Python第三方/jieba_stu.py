# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 9:54
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : jieba_stu.py
# @Software: PyCharm

import jieba

text = "章子怡给王思聪买了微博热搜"
jieba.suggest_freq(("买了"), True)  # 自定义
jieba.suggest_freq(("微博"), True)
jieba.suggest_freq(("热搜"), True)
ret = jieba.cut(text)
print(list(ret))

jieba.load_userdict()  # 可以加载自定义分词

#读取标点符号库
f=open("utils/stopwords.txt","r")
stopwords={}.fromkeys(f.read().split("\n"))
f.close()
#加载用户自定义词典
jieba.load_userdict("./utils/jieba_user_dict.txt")
segs=jieba.cut(text)
mytext_list=[]
#文本清洗
for seg in segs:
    if seg not in stopwords and seg!=" " and len(seg)!=1:
        mytext_list.append(seg.replace(" ",""))
cloud_text=",".join(mytext_list)
