#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:


import re
import jieba
import numpy as np
import pandas as pd


# In[17]:


wb=pd.read_csv("weibo1.csv",encoding="gb18030",delimiter="\t")


# In[18]:


wb.head()


# In[28]:


text0 = '@肖战工作室 你还行不行！诗写好了没！想看帅哥 ?'
# text0 = fi.read()  # 获取文本内容
text1 = re.sub("@([\s\S]*?):", "", text0)  # 去除@ ...：
text2 = re.sub("\[([\S\s]*?)\]", "",text1)  # [...]：
text3 = re.sub("@([\s\S]*?)", "", text2)  # 去除@...
text4 = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", text3)  # 去除标点及特殊符号
text5 = re.sub("[^\u4e00-\u9fa5]", "", text4)  # 去除所有非汉字内容（英文数字）
new_text = jieba.cut(text5, cut_all=False)  # 精确模式
str_out = ' '.join(new_text)
str_out


# [参考文档](https://www.squncle.com/article/2020/4/23/19864.html)

# In[ ]:





# In[ ]:




