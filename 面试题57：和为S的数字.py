#!/usr/bin/env python
# coding: utf-8

# # 题目一:和为s的两个数字
# 
# ### 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s,则输出任意一对即可
# 

# In[ ]:


'''
思路：

我们以数组{1,2,4,7,11,15}及期待的和15为例详细分析一下这个过程。首先定义两个指针，第一个指针指向数组的第一个（最小的）数字1，第二个指针指向数组的最后一个（最大的）数字15，这两个数字的和16大于15，因此我们把第二个指针向前移动一个数字，让它指向11.这时候两个数字1与11的和时12，小于15,。接下来我们把第一个指针向后移动一个数字指向2，此时两个数字2与11的和是13，还是小于15.我们再次向后移动第一个指针，让它指向数字4，数字4与11的和是15，正是我们期待的结果。
'''
def FindNumbersWithSum(data,sum):
    if not data:
        return None
    length=len(data)
    ahead=length-1
    behind=0
    while ahead>behind:
        curSum=data[ahead]+data[behind]
        if curSum==sum:
            return [data[behind],data[ahead]]
        elif curSum>sum:
            ahead-=1
        else:
            behind+=1
    return []


# # 题目二：和为s的连续正数序列
# 
# ### 输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，打印出3个连续序列1\~5,4\~6和7~8

# In[ ]:


'''
思路：

有了解决前面问题的经验，我们也考虑用两个数small和big分别表示序列的最小值和最大值。首先把small初始化为1，big初始化为2。如果从small到big的序列的和大于s，则可以从序列中去掉最小的值，也就是增大small的值。如果从small到big的序列的和小于s,则可以增大big，让这个序列包含更多的数字。因为这个序列至少要有两个数字，我们一直增加small到（1+s）/2为止
以求和为9的所有连续序列为例，我们先把small初始化为1，big初始化为2。此时介入small和big之间的序列是{1,2}，序列的和为3，小于9，所以我们下一步要让序列包含更多的数字。我们把Big增加1边恒3，此时序列为1,2,3.由于序列的和时6，仍然小于9，我们接下来再增加big变成4，介于small和big之间的序列也随之变成{1,2,3,4}。由于序列的和10大于9，我们要删去序列中的一些数字，于是我们增加small变成2，此时得到的序列是{2,3,4}，序列的和正好是9，我们找到了第一个和为9的连续序列，把它打印出来。接下来我们再增加big，重复前面的过程，可以找到第二个和为9的连续序列{4,5}
'''
def PrintContinusSequence(small,big):
    for i in range(small,big+1):
        print("%d"%i)
    print("\n")

def FindContinusSequences(sum):
    if sum<3:
        return None
    small=1
    big=2
    res=[]
    middle=(1+sum)/2
    curSum=small+big
    while small<middle:
        if curSum==sum:
            PrintContinusSequence(small,big)
            res.append(list(range(small,big+1)))
        while curSum>sum and small<middle:
            curSum-=small
            small+=1
            if curSum==sum:
                PrintContinusSequence(small,big)
                res.append(list(range(small,big+1)))
        big+=1
        curSum+=big
    return res


# In[ ]:


'''
简化版的写法
'''
def FindContinuousSequence(tsum):
    res=[]
    for i in range(1,tsum//2+1):
        sum_num=i
        for j in range(i+1,tsum//2+2):
            sum_num+=j
            if sum_num==tsum:
                res.append(list(range(i,j+1)))
                break
            elif sum_num>tsum:
                break
    return res

