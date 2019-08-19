#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
介绍：
把字符串中的空格替换成%20
'''
'''
过程:
用python的内置函数会比书中介绍的简单很多
'''
def replace_space(rep_str):
    rep_str=rep_str.replace(" ","%20")
    return rep_str
a="We all like python"
a=replace_space(a)
print(a)


# In[ ]:




