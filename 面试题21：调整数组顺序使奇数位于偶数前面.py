#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
# 

# In[12]:


'''
只完成基本功能的代码
'''
'''
思路:

我们使用两个指针，第一个指针初始化时指向数组的第一个数字，它只向后移动，第二个指针
初始化时指向数组的最后一个数字，它只向前移动。在两个指针相遇之前，第一个指针总是位于
第二个指针的前面。如果第一个指针指向的数字是偶数，并且第二个指针指向的数字是奇数，则
交换这两个数字
'''
def ReorderOddEvent(pData):
    if len(pData)<=0:
        return
    start=0
    end=len(pData)-1
    while start<end:
        #向后移动start，直到它指向偶数
        while start<end and (pData[start]%2)!=0:
            start+=1
        #向前移动end,直到它指向奇数
        while start<end and (pData[end]%2)==0:
            end-=1
        if start<end:
            temp=pData[start]
            pData[start]=pData[end]
            pData[end]=temp

    return pData

ReorderOddEvent([1,2,3,4,5])


# In[13]:


'''
扩展的解法
'''

'''
思路：

把两个while的逻辑框架抽象出来，用函数来进行处理，这样能很方便的把解决方案扩展到同类
问题上去
'''
def isEvent(n):
    return (n&1)==0
def Reorder(pData):
    if len(pData)<=0:
        return
    start=0
    end=len(pData)-1
    while start<end:
        #向后移动start，直到它指向偶数
        while start<end and not isEvent(pData[start]):
            start+=1
        #向前移动end,直到它指向奇数
        while start<end and isEvent(pData[end]):
            end-=1
        if start<end:
            temp=pData[start]
            pData[start]=pData[end]
            pData[end]=temp

    return pData

Reorder([1,2,3,4,5])


# In[14]:


'''
纯Python的解法
'''
def ReorderList(data):
    odd=[]
    even=[]
    for i in data:
        if i&0x1==0:
            even.append(i)
        else:
            odd.append(i)
    return odd+even

ReorderList([1,2,3,4,5])


# In[16]:


'''
大神的一行代码
'''
def ReorderData(data):
    return sorted(data,key=lambda x:x%2,reverse=True)

ReorderData([1,2,3,4,5,7,5,6,8,1])


# In[ ]:




