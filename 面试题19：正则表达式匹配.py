#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请事先一个函数用来匹配包含'.'和'\*'的正则表达式。模式中的字符'.'表示一个字符。而'\*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串'aaa'与模式'a.a'和'ab\*ac\*a'匹配，但与'aa.a'和'ab\*a'均不匹配

# In[34]:


'''
思路：

每次从字符串里拿出一个字符和模式中的字符去匹配。先来分析如何匹配一个字符。如果模式
中的字符ch是'.'，那么它可以匹配字符串中的任意字符。如果模式中的字符ch不是'.',而且字
符串中的字符也是ch,那么它们相互匹配。当字符串中的字符和模式中的字符相匹配时，接着匹
配后面的字符
相对而言，当模式中的第二个字符不是'*'时，问题要简单得多。如果字符串中的第一个字符和
模式中的第一个字符相匹配，那么在字符串和模式上都向后移动一个字符，然后匹配剩余的字
符串和模式。如果字符串中的第一个字符和模式中的第一个字符不相匹配，则直接返回False

当模式中的第二个字符是'*'时，问题要复杂一些，因为可能多种不同的匹配方式。一种选择
是在模式上向后移动两个字符。这相当于'*'和它前面的字符被忽略了，因为'*'可以匹配字
符串中的0个字符。如果模式中的第一个字符和字符串中的第一个字符相匹配，则在字符串上
向后移动一个字符，而在模式上有两种选择：可以在模式上向后移动两个字符，也可以保持
模式不变
'''
def matchCore(strs,pattern):
    if strs==pattern:
        return True
    if not pattern:
        return False
    if len(pattern)>1 and pattern[1]=='*':
        if (strs and pattern[0]==strs[0]) or (pattern[0]=='.' and strs):
            #move on the next state
            return matchCore(strs[1:],pattern[2:]) or matchCore(strs[1:],pattern) or matchCore(strs,pattern[2:])
        else:
            return matchCore(strs,pattern[2:])
    elif strs and (strs[0]==pattern[0] or pattern[0]=='.'):
        return matchCore(strs[1:],pattern[1:])
    return False

def match(strs,pattern):
    if strs is None and pattern is None:
        return False
    return matchCore(strs,pattern)

match("aaa","ab*a")

