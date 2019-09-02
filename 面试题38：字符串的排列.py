#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个字符串，打印出该字符串中字符的所有排列。例如，输入字符串，则打印出有字符a,b,c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba

# In[ ]:


'''
思路：

我们求整个字符串的排列，可以看成两步。第一步求所有可能出现在第一个位置的字符，即把第一个字符和后面所有的字符交换。第二步固定第一个字符，求后面所有字符的排列。这时候我们仍把后面的所有字符分成两部分：后面字符的第一个字符，以及这个字符之后的所有字符。然后把第一个字符逐一和它后面的字符交换。这其实是典型的递归思路
'''
# 由于原题使用了指针来传递，在Python中不知道怎么弄，所以没有用这种方法
# def PermutationCore(pStr,pBegin):
#     if not pBegin:
#         print("%s"%pStr)
#     else:
#         j=0
#         for i in pBegin:
#             temp=i
#             i=pBegin[j]
#             pBegin[j]=temp
            
#             PermutationCore(pStr,pBegin[j+1:])
            
#             temp=i
#             i=pBegin[j]
#             pBegin[j]=temp
            
#             j+=1

# def Permutation(pStr):
#     if not pStr:
#         return None
    
#     PermutationCore(pStr,pStr)
            


# In[ ]:


'''
纯Python的解法
'''
import itertools
def Permutation(s):
    if not s:
        return []
    result=[]
    res=itertools.permutations(s)
    for i in res:
        if "".join(i) not in result:
            result.append("".join(i))
    return result


# In[ ]:


'''
递归解法
'''
def Permutation(s):
    if len(s)<=1:
        return s
    res=set()
    for i in range(s):
        for j in Permutation(s[:i]+s[i+1:]):
            res.add(s[i]+j)
    return sorted(res)

