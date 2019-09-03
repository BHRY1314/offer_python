#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入n个整数，找出其中最小的k个数。例如，输入4、5、1、6、2、7、3、8这8个数，则最小的4个数字是1、2、3、4

# In[ ]:


'''
思路：
简单来说只要将输入的整数进行排序，然后取出前k个即可
'''

'''
快速排序
'''
def GetLastNumbers(number,k):
    def quick_sort(nList):
        if not nList:
            return []
        pivot=nList[0]
        left=quick_sort([x for x in nList[1:] if x<pivot])
        right=quick_sort([x for x in nList[1:] if x>pivot])
        return left+[pivot]+right
    if not number or k>len(number):
        return []
    result=quick_sort(nList)
    return result[:k]


# In[ ]:


'''
归并排序
'''
def GetLastNumbers(number,k):
    def merge_sort(nList):
        if len(nList)<=1:
            return nList
        mid=len(nList)//2
        left=merge_sort(nList[:mid])
        right=merge_sort(nList[mid:])
        return merge(left,right)
    def merge(left,right):
        l,r,res=0,0,[]
        while l<len(left) and r<len(right):
            if left[l]<=right[r]:
                res.append(left[l])
                l+=1
            else:
                res.append(right[l])
                r+=1
        res+=left[l:]
        res+=right[r:]
        return res
    if number==[] or k>len(numer):
        return []
    result=merge_sort(number)
    return result[:k]


# In[ ]:


'''
堆排序
'''
def GetLastNumbers(number,k):
    def siftup(nList,temp,begin,end):
        if nList==[]:
            return []
        i=begin
        j=begin*2+1
        while j<end:
            if j+1<end and nList[j+1]>nList[j]:
                j+=1
            elif temp>nList[j]:
                break
            else:
                nList[i]=nList[j]
                i,j=j,2*j+1
    def heap_sort(nList):
        if nList==[]:
            return []
        end=len(nList)
        for i in range((end//2)-1,-1,-1):
            siftup(nList,nList[i],i,end)
        for i in range(end-1,0,-1):
            temp=nList[i]
            nList[i]=nList[0]
            siftup(nList,temp,0,i)
        return nList
    if number==[] or k>len(numer):
        return []
    result=heap_sort(number)
    return result[:k]


# In[ ]:


'''
冒泡排序
'''
def GetLastNumbers(number,k):
    def bubble_sort(nList):
        if nList==[]:
            return []
        for i in range(len(nList)):
            for j in range(1,len(nList)-i):
                if nList[j-1]>nList[j]:
                    nList[j-1],nList[j]=nList[j],nList[j-1]
        return nList
    if number==[] or k>len(numbers):
        return []
    result=bubbler_sort(number)
    return result[:k]


# In[ ]:


'''
直接选择排序
'''
def GetLastNumbers(number,k):
    def select_sort(nList):
        if nList==[]:
            return []
        for i in range(len(nList)-1):
            smallest=i
            for j in range(i,len(nList)):
                if nList[j]<nList[smallest]:
                    smallest=j
            nList[i],nList[smallest]=nList[smallest],nList[i]
        return nList
    if number==[] or k>len(number):
        return []
    result=select_sort(number)
    return result[:k]


# In[ ]:


'''
插入排序
'''
def GetLastNumbers(number,k):
    def Insert_sort(nList):
        if nList==[]:
            return []
        for i in range(1,len(nList)):
            temp=nList[i]
            j=i
            while j>0 and temp<nList[j-1]:
                nList[j]=nList[j-1]
                j-=1
            nList[i]=temp
        return nList
    if number==[] or k>len(number):
        return []
    result=Insert_sort(number)
    return result[:k]


# In[ ]:


'''
最简洁的写法
'''
def GetLastNumbers(number,k):
    if number==[] or k>len(number):
        return []
    number=sorted(number)
    return number[:k]

