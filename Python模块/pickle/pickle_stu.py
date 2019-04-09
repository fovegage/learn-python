# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:56
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : pickle_stu.py
# @Software: PyCharm
import pickle

data = {
    'a':'Gage',
    'man':True
}

pkl = open('data.pkl', 'wb')
pickle.dump(data, pkl)
pkl.close()

pkl_file = open('data.pkl', 'rb') # connect to the pickled data
data = pickle.load(pkl_file) # load it into a variable
print(data)
pkl_file.close()