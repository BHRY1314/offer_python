#!/usr/bin/env python
# coding: utf-8

# # 题目一：翻转单词顺序
# 
# ### 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串“I am a student”，则输出"student. a am I"。

# In[ ]:


'''
思路：

第一步翻转句子中所有的字符。比如翻转“I am a student”中所有的字符得到".tnenduts a ma I",此时不但翻转了句子中单词的顺序，连单词内的字符顺序也被翻转了。第二步再翻转每个单词中字符的顺序，就得到了“student. a am I”。这正是符合题目要求的输出.

这种思路的关键在于实现一个函数以翻转字符串中的一段。下面的函数可以完成这一功能
'''
# def Reverse(strs,pBegin,pEnd):
#     if not pBegin or not pEnd or not strs:
#         return None
#     while pBegin<pEnd:
#         temp=strs[pBegin]
#         strs[pBegin]=strs[pEnd]
#         strs[pEnd]=temp
#         pBegin+=1
#         pEnd+=1
'''
接着我们可以用这个函数先翻转整个句子，再翻转句子中的每个单词。
'''
# def ReverseSentence(pData):
#     if not pData:
#         return None
#     pBegin=0
#     pEnd=len(pData)-1
#     #翻转整个句子
#     Reverse(pData,pBegin,pEnd)
#     #翻转句子中的每个单词
#     pBegin=pEnd=0
#     while pBegin<len(pData):
#         if pData[pBegin]==" ":
#             pBegin+=1
#             pEnd+=1
#         elif pData[pEnd]==' ' or pEnd==len(pData)-1:
#             Reverse(pBegin,pEnd-1)
#             pBegin=pEnd+1
#         else:
#             pEnd+=1
        
#     return pData
'''
思路是对的，但是这个方法在python上运行有点问题，所以我们用更直观的python写法
'''


# In[1]:


'''
纯Python写法
'''
def Reverse(s):
    s=list(s.split(" "))
    s=s[::-1]
    return " ".join(s)

Reverse("Being deeply loved by someone gives you strength, loving someone deeply gives you courage.")


# # 题目二：左旋转字符串
# 
# ### 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串“abcdefg”和数字2，该函数将返回左旋转两位得到的结果"cdefgab"

# In[ ]:


'''
思路：

以“abcdefg”为例，我们可以把它分成两部分。由于想把它的前两个字符移到后面，我们就把前两个字符分到第一部分，把后面的所有字符分到第二部分。我们先分别翻转这两部分，于是就得到“bagfedc”,接下来翻转整个字符串，得到的“cdefgab”刚好就是把原始字符串左旋转两位的结果
'''
# def LeftRotateString(pStr,n):
#     if not pStr:
#         nLength=len(pStr)
#         if nLength>0 and n>0 and n<nLength:
#             pFirstStart=0
#             pFirstEnd=n-1
#             pSecondStart=n
#             pSecondEnd=nLength-1
            
#             Reverse(pStr,pFirstStart,pFirstEnd)
#             Reverse(pStr,pSecondStart,pSecondEnd)
#             Reverse(pStr,pFirstStart,pSecondEnd)
#     return pStr


# In[ ]:


'''
Python简洁的方法
'''
def LeftRotateString(s, n):
    if not s:
        return ""
    l1=list(s[n:])
    l2=list(s[:n])
    return "".join(l1+l2)

