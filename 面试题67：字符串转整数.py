#!/usr/bin/env python
# coding: utf-8

# In[2]:


def StrToInt(s):
    if not s:
        return 0
    res=0
    mult=1
    flag=1
    if s[0]=='-' or s[0]=='+':
        if s[0]=='-':
            flag=-1
        s=s[1:]
    for i in range(len(s)-1,-1,-1):
        if '9'>=s[i]>='0':
            res+=(ord(s[i])-48)*mult
            print("mult:",mult)
        else:
            return 0
    return res*flag


# In[ ]:


'''
利用正则表达式
'''
def StrToInt(s):
    if not s:
        return 0
    pattern = r'^[-+]{0,1}[0-9]{1,}$'
    if re.match(pattern,s):
        return int(s)
    else:
        return 0

