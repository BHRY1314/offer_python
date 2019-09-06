#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 我们把只包含因子2、3和5的数称作丑数。求按从小到大的顺序的第1500个丑数。例如，6、8都是丑数，但14不是，因为它包含因子7

# In[ ]:


'''
思路：

根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。因此，我们可以创建一个数组，里面的数字是排好序的丑数，每个丑数都是前面的丑数乘以2、3或者5得到的。

这种思路的关键在于怎样确保数组里面的丑数是排好序的。假设数组中已经有若干个排好序的丑数，并且把已有最大的丑数记做M，接下来分析如何生成下一个丑数。该丑数肯定是前面某一格丑数乘以2、3或者5的结果，所以我们首先考虑把已有的每个丑数乘以2.在乘以2的时候，能得到若干个小于或者等于M的结果。由于是按照顺序生成的，小于或者等于M肯定已经在数组中了，我们不需再次考虑，还会得到若干个大于M的结果，但我们只需要第一个大于M的结果，因为我们希望丑数是按从小到大的顺序生成的，其他更大的结果以后再说。我们把得到的第一个乘以2后大于M的结果记为M2.同样，我们把已有的每个丑数乘以3和5，能得到第一个大于M的结果M3和M5。那么下一个丑数应该是M2，M3和M5这三个数的最小者。

在前面分析的时候提到把已有的每个丑数分别乘以2、3和5.事实上这不是必需的，因为已有的丑数是按照顺序存放在数组中的。对于乘以2而言，肯定存在某一个丑数T2，排在它在之前的每个丑数乘以2得到的结果都会小于已有最大的丑数，在它之后的每个丑数乘以2得到的结果都会太大。我们只需记下这个丑数的位置，同时每次生成新的丑数的时候去更新这个T2即可。对于乘以3和5而言，也存在同样的T3和T5。
'''
def Min(number1,number2,number3):
    min_num=number1 if number1<number2 else number2
    min_num=min_num if min_num<number3 else number3
    return min_num

def GetUglyNumber(index):
    if index<=0:
        return 0
    pUglyNumbers=[1]*index
    nextUglyIndex=1
    
    pMultiply2=0
    pMultiply3=0
    pMultiply5=0
    
    while nextUglyIndex<index:
        min_num=Min(pUglyNumbers[pMultiply2]*2,pUglyNumbers[pMultiply3]*3,pUglyNumbers[pMultiply5]*5)
        pUglyNumbers[nextUglyIndex]=min_num
        while pUglyNumbers[pMultiply2]*2<=pUglyNumbers[nextUglyIndex]:
            pMultiply2+=1
        while pUglyNumbers[pMultiply3]*3<=pUglyNumbers[nextUglyIndex]:
            pMultiply3+=1
        while pUglyNumbers[pMultiply5]*5<=pUglyNumbers[nextUglyIndex]:
            pMultiply5+=1
        nextUglyIndex+=1
    ugly=pUglyNumbers[nextUglyIndex-1]
    return ugly


# In[ ]:


'''
大神的Python代码
缺点：时间复杂性和空间复杂性比较高
'''
def GetUglyNumbers_soultion2(index):
    res=[2**i*3**j*5**k  for i in range(30)  for j in range(20)   for k in range(15)]
    res.sort()
    return res[index-1] if index else 0

