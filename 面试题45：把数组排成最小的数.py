#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接处的所有数字中最小的一个。例如，输入数组{3,32,321}，则打印出这三个数字能排成的最小数字321323

# In[ ]:


'''
思路：

根据题目的要求，两个数字m和n能拼接成数字nm和mn。如果mn<nm，那么我们应该打印出mn，也就是m应该排成n的前面，我们定义此时m小于n；反之，如果nm<mn，则我们定义n小于m；如果mn=nm，则m等于n。
接下来考虑怎么去拼接数字，即给出数字m和n，怎么得到数字nm和mn并比较它们的大小。直接用数值去计算不难办到，但需要考虑的一个潜在问题就是m和n都在int能表达的范围内，但把它们拼接起来的数字mn和nm用int表示就有可能溢出了，所以这还是一个隐形的大数问题。
一个非常直观的解决大数问题的方法就是把数字转换成字符串。另外，由于把数字m和n拼接起来得到mn和nm，它们的位数肯定是相同的，因此比较它们的大小只需要按照字符串大小的比较规则就可以了
'''
def comp(str1,str2):
    c1=str1+str2
    c2=str2+str1
    return cmp(c1,c2)

def PrintMinNumber(numbers):
    if not numbers:
        return ""
    strs=map(str,numbers)
    strs.sort(cmp=comp)
    return ''.join(strs)
    

