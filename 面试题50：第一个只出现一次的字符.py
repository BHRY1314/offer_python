#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，则输出“b”。

# In[8]:


'''
思路：

我们可以定义哈希表，哈希表的键值是字符，而值是该字符出现的次数。同时我们还需要从头开始扫描字符串两次，第一次扫描字符串时，每扫描到一个字符，就在哈希表的对应项中把次数加1.接下来第二次扫描时，每扫描到一个字符就能从哈希表得到该字符出现的次数。这样，第一个只出现一次的字符就是符合要求的输出
'''
def FirstNotRepeatingChar(pString):
    if not pString:
        return None
    hashTable=[0]*256
    for i in pString:
        hashTable[ord(i)]+=1
    for i in pString:
        if hashTable[ord(i)]==1:
            return i
            break
    return None

FirstNotRepeatingChar("googlle")


# In[10]:


'''
纯Python的代码
'''
def FirstNotRepeatingChar(pString):
    if not pString:
        return None
    for i in pString:
        if pString.count(i)==1:
            return i
    return None

FirstNotRepeatingChar("googlle")


# In[11]:


'''
更精简的一行代码
'''
def FirstNotRepearingChar(pString):
    return pString.index(list(filter(lambda c:pString.count(c)==1,pString))[0]) if pString else -1

FirstNotRepeatingChar("googlle")


# In[ ]:




