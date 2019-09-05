#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 数字以012345789101112131415……的格式序列化一个字符序列中。在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一个函数，求任意第n位对应的数字

# In[ ]:


'''
思路：

我们用一个具体的例子来分析，比如，序列的第1001位是什么？

序列的前10位是0~9这10个只有一位的数字。显然第1001位在这10个数字之后，因此这10个数字可以直接跳过。我们再从后面紧跟着的序列中找第991（991=1001-10）位的数字

接下来180位数字是90个10~99的两位数。由于991>180,所以第991位在所有的两位数之后。我们再跳过90个两位数，继续从后面找881位（811=991-180）

接下来的2700位是900个100~999的三位数。由于811<2700，所以第811位是某个三位数的一位。由于811=270*3+1，这意味着第811位是从100开始的第270个数字即370的中间一位，也就是7
'''

'''
countOfIntergers得到m位的数字总共有多少个？例如。输入2，则返回两位数（10~99）的个数90；输入3，则返回三位数（100~999）的个数900
'''
def counOfIntegers(digits):
    if digits==1:
        return 10
    count=int(pow(10,digits-1))
    return 9*count
'''
当我们知道要找的那一位数字位于某m位数之中后，就可以用如下的函数找出那一位数字
'''
def digitAtIndex(index,digits):
    number=beginNumber(digits)+index/digits
    indexFromRight=digits-index%digits
    for i in range(indexFromRight):
        number/=10
    return number%10
'''
第一个m位数可以用如下函数求得
'''
def beginNumber(digits):
    if digits==1:
        return 0
    return int(pow(10,digits-1))

'''
主函数
'''
def digitAtIndex(index):
    if index<0:
        return -1
    digits=1
    while True:
        numbers=countOfIntegers(digits)
        if index<numbers*digits:
            return digitAtIndex(index,digits)
        index-=digits*number
        digits+=1
    return -1

