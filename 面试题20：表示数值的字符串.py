#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串“+100”、“5e2”、“-123”，“3.1416”及"-1E16"都表示数值，但“12e”,"1a3.14"、"1.2.3"、“+-5”及"12e+5.4"都不是

# In[19]:


'''
思路:

    表示数值的字符串遵循模式A[.[B]][e|EC]或者.B[e|EC]，其中A为数值的整数部分，B紧跟着
小数点为数值的小数部分，C紧跟着'e'或者'E'为数值的指数部分。在小数里可能没有数值的整数
部分。例如，小数.123等于0.123。因此A部分不是必需的。如果一个数没有整数部分，那么它的小数
部分不能为空
    判断一个字符串是否符合上述模式时，首先尽可能多地扫描0~9的数位（有可能在起始处有+或者-），
也就是前面模式中表示数值整数的A部分。如果遇到小数点'.'，则开始扫描表示数值小数部分的B部分。
如果遇到'e'或者'E'，则开始扫描表示数值指数的C部分
'''

'''
由于原来的C++代码使用了字符指针，所以没有很明白原文代码中的索引移动，导致这个方法
存在错误，如果知道怎么修改望告知，感激不尽。
'''


#函数ScanUnsignedInterger用来扫描字符串中0~9的数位（类似于一个无符号整数），可以用来
#匹配前面数值模式中的B部分
def scanUnsignedInteger(str):
    before=0
    num=0
    i=0
    while i<len(str):
        if str[i] and str[i]>='0' and str[i]<='9':
            i+=1
        else:
            break
    return i>before

#函数scanInteger扫描可能以表示正负“+”或者“-”为起始的0~9数位（类似于一个可能带
#正负符号的整数），用来匹配前面数值模式中的A和C部分
def scanInteger(str):
    i=0
    if str[i]=="+" or str[i]=="-":
        i+=1
    return scanUnsignedInteger(str[i:])

#主代码
def isNumber(str):
    if len(str)<=0:
        return False
    numeric=scanInteger(str)
    i=0
    if str[i]=='.':
        i+=1
        #下面一行代码用或(or)的原因:
        #1.小数可以没有整数部分，如.123=0.123
        #2.小数点后面可以没有数字，如233.等于233.0
        #3.当然，小数点前面和后面可以都有数字，如233.666
        numeric=scanUnsignedInteger(str[i:]) or numeric
    #如果出现'e'或者'E',则接下来是数字的指数部分
    if str[i]=='e' or str[i]=='E':
        i+=1
        #下面一行代码用且(and)的原因
        #1.当e或E前面没有数字时，整个字符串不能表示数字，如.e1,e1
        #2.当e或者E后面没有数字时，整个字符串不能表示数字，如12e、12e+5.4
        numeric=numeric and scanInteger(str[i:])
        
    return numeric

isNumber('e2')


# In[24]:


'''
使用正则表达式
'''
import re

def isNumber_re(str):
    if not str:
        return False
    result=bool(re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$',str))
    return result

isNumber_re("22")


# In[ ]:




