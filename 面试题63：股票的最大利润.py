#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 假设把某股票价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？例如，一只股票在某些时间节点的价格为{9、11、8、5、7、12、16、14}。如果我们能在价格为5的时候买入在价格为16时卖出，则能收获最大的利润11。

# In[4]:


'''
思路：

我们先定义函数diff(i)为当卖出价为数组中第i个数字时可能获得的最大利润。显然，在卖出价固定时，买入价越低获得的利润越大。也就是说，如果扫描到数组中的第i个数字时，只要我们能够记住之前的i-1个数字中的最小值，就能算出在当前价位卖出时可能得到的最大利润。
'''
def MaxDiff(numbers):
    if not numbers:
        return 0
    min_num=numbers[0]
    maxDiff=numbers[1]-min_num
    if maxDiff<0:
        maxDiff=0
    length=len(numbers)
    for i in range(2,length):
        if numbers[i-1]<min_num:
            min_num=numbers[i-1]
        currentDiff=numbers[i]-min_num
        if currentDiff>maxDiff:
            maxDiff=currentDiff
    return maxDiff

MaxDiff([7,6,5,4,3,2,1])


# In[6]:


'''
更简洁的方法
'''
def MaxDiff(prices):
    if not prices:
        return 0
    res=0
    min_num=prices[0]
    for i in prices[1:]:
        min_num=min(min_num,i)
        if res<i-min_num:
            res=i-min_num
    return res
MaxDiff([7,6,5,4,3,2,1])


# In[ ]:




