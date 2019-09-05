#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含'a'\~'z'的字符。例如，在字符串'arabcacfr'中，最长的不含重复字符的子字符串是'acfr',长度为4

# In[ ]:


'''
思路：

首先定义函数f(i)表示以第i个字符为结尾的不包含重复字符的子字符串的最长长度。我们从左到右逐一扫描字符串中的每个字符。当我们计算以第i个字符为结尾的不包含重复字符的子字符串的最长长度f(i)时，我们已经知道f(i-1)了。

如果第i个字符之前没有出现过，那么f(i)=f(i-1)+1。例如，在字符串'arabcacfr'中，显然f(0)等于1。在计算f(1)时，下标为1的字符'r'之前没有出现过，因此f(1)等于2，即f(1)=f(0)+1。到目前为止，最长的不含除服字符的子字符串是'ar'。

如果第i个字符之前已经出现过，那情况就要复杂一点了。我们先计算第i个字符和它上次出现在字符串中的位置的距离，并记为d，接着分两种情况分析。第一种情形是d小于或者等于f(i-1),此时第i个字符上次出现在f(i-1)对应的最长子字符串之中，因此f(i)=d。同时这也意味着在第i个字符出现两次所夹的子字符串中再也没有其他重复的字符了。在前面的例子中，我们继续计算f(2)，即以下标为2的字符'a'为结尾的不含重复字符的子字符串的最长长度。我们注意到字符'a'在之前出现过，该字符上一次出现在下标为0的位置，它们之间的距离d为2，也就是字符'a'出现在f(1)对应的最长不含重复字符的子字符串'ar'中，此时f(2)=d,即f(2)=2,对应的最长不含重复字符的子字符串是'ra'。

第二种情形是d大于f(i-1),此时第i个字符上次出现在f(i-1)对应的最长字符串之前，因此仍然有f(i)=f(i-1)+1。我们接下来分析以字符串'arabcacfr'字后一个字符'r'为结尾的最长不含重复字符的子字符串的长度，即求f(8)。以它前一个字符'f'为结尾的最长不含重复字符的子字符串是'acf',因此f(7)=3。我们注意到最后一个字符'r'之前在字符串'arabcacfr'中出现过，上一次出现在下标为1的位置，因此两次出现的距离d等于7，大于f(7)。此时把字符'r'拼接到'acf'的后面也不会出现重复字符。因此f(8)=f(7)+1,即f(8)=4
'''
def longestSubstringWithoutDuplication(strs):
    curLength=0
    maxLength=0
    position=[-1]*26
    for i in range(len(strs)):
        prevIndex=position[strs[i]-'a']
        if prevIndex<0 or i-prevIndex>curLength:
            curLength+=1
        else:
            if curLength>maxLength:
                maxLength=curLength
            curLength=i-prevIndex
        position[strs[i]='a']=i
    if curLength>maxLength:
        maxLength=curLength
    return maxLength

