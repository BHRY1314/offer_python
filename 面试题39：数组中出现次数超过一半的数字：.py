#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如，输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2

# In[ ]:


'''
思路：

数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现的次数的和还要多。因此，我们可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字；另一个是次数。当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数减1.如果次数为0，那么我们需要保存下一个数字，并把次数设为1.由于我们要找的数字出现的次数比其他所有数字出现的次数还要多，那么要找的数字肯定是最后一次把次数设为1时对应的数字。

'''
def CheckMoreThanHalf(numbers,number):
    times=0
    l=len(numbers)
    for i in range(0,l):
        if numbers[i]==number:
            times+=1
    isMoreThanHalf=True
    if times*2<=l:
        g_bInputInvalid=True
        isMoreThanHalf=False
    return isMoreThanHalf

def MoreThanHalfNumber(numbers):
    if len(numbers)<=0:
        return 0
    result=numbers[0]
    l=len(numbers)
    times=1
    for i in range(1,l):
        if times==0:
            result=numbers[i]
            times=1
        elif numbers[i]==result:
            times+=1
        else:
            times-=1
    if not CheckMoreThanHalf(numbers,result):
        result=0
    return result


# In[ ]:


'''
利用字典
'''
def MoreThanHalfNum_Solution(self, numbers):
    if not numbers:
        return 0
    if len(numbers)==1:
        return numbers[0]
    dic={}
    for i in range(len(numbers)):
        if numbers[i] not in dic:
            dic[numbers[i]]=1
        else:
            dic[numbers[i]]+=1
            if dic[numbers[i]]>(len(numbers)//2):
                return numbers[i]
    return 0

