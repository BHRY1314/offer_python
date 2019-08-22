#!/usr/bin/env python
# coding: utf-8

# #### 实现快速排序

# In[46]:


'''
根据书中源码改写
'''

'''
实现快速排序的关键在于先在数组中选择一个数字，接下来把数组中的数字分为两部分，比选择的数
字小的数字移到数组的左边，比选择的数字大的数字移到数组的右边。这个函数如下所示
'''
import random
def Partition(data,start,end):
    if len(data)<=0:
        print("Wrong Parameters")
    #randrange用来生成一个在start和end之间的随机数
    index=random.randrange(start,end)
    
    #交换两个数字
    data[start],data[end]=data[end],data[start]
    small=start-1
    for index in range(start,end):
        if data[index]<data[end]:
            small+=1
            if small!=index:
                data[index],data[small]=data[small],data[index]
    small+=1
    data[small],data[end]=data[end],data[small]
    
    return small

'''
递归实现快速排序
'''
def QuickSort(data,start,end):
    if start==end:
        return data
    index=Partition(data,start,end)
    if index>start:
        QuickSort(data,start,index-1)
    if index<end:
        QuickSort(data,index+1,end)

a=[1,5,6,7,2,3,4,9]
start=0
end=len(a)-1
QuickSort(a,start,end)
print(a)


# #### 对年龄进行排序

# In[61]:


def SortAges(ages):
    if len(ages)<=0:
        return
    
    oldestAge=99
    timesOfAge=[0]*100
        
    for i in range(len(ages)):
        age=ages[i]
        if age<0 or age>oldestAge:
            print("age out of range")
        timesOfAge[age]+=1
    
    index=0
    for i in range(oldestAge+1):
        for j in range(0,timesOfAge[i]):
            ages[index]=i
            index+=1
    return ages

a=[15,22,44,33,35]
SortAges(a)


# # 题目
# 
# ###  把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1

# In[70]:


'''
思路：
    和二分查找法一样，我们用两个指针分别指向数组的第一个元素和最后一个元素。按照题目中
旋转的规则，第一个元素应该是大于或者等于最后一个元素的接着我们可以找到数组中间的元素。
如果该中间元素位于前面的递增子数组，那么它应该大于或者等于第一个指针指向的元素。此时数
组中最小的元素应该位于该中间元素的后面。我们可以把第一个指针指向该中间元素，这样可以缩
小寻找的范围。移动之后的第一个指针仍然位于前面的递增子数组。
    同样，如果中间元素位于后面的递增子数组，那么它应该小于或者等于第二个指针指向的元
素。此时该数组中最小的元素应该位于该中间元素的前面。我们可以把第二个指针指向该中间元
素，这样也可以缩小寻找的范围。移动之后的第二个指针仍然位于后面的递增子数组。
    不管是移动第一个指针还是第二个指针，查找范围都会缩小到原来的一半。接下来我们再用更
新之后的两个指针重复做新一轮的查找。
    按照上述思路，第一个指针总是指向前面递增数组的元素，而第二个指针总是指向后面递增数
组的元素。最终第一个指针将指向前面子数组的最后一个元素，而第二个指针会指向后面子数组的
第一个元素，也就是它们最终会指向两个相邻的元素，而第二个指针指向的刚好是最小的元素，这
就是循环结束的条件

（Python中没有指针，但是可以将指针认为是索引来进行理解）

'''
def Min_num(numbers):
    '''
    根据书中的C++代码改写
    '''
    
    if len(numbers)<=0:
        print("无效的参数")
    
    
    index1=0
    index2=len(numbers)-1
    indexMid=index1
    while numbers[index1]>=numbers[index2]:
        if index2-index1==1:
            indexMid=index2
            break
        
        indexMid=int((index1+index2)/2)
        if numbers[indexMid]>=numbers[index1]:
            index1=indexMid
        elif numbers[indexMid]<=numbers[index2]:
            index2=indexMid
    
    return numbers[indexMid]

a=[3,4,5,6,2]
Min_num(a)


# In[73]:


'''
额外情况：
    当第一个指针和第二个指针指向的数字都相同，并且两个指针的中间数字也相同时。在这种情
况下，中间数字可能位于后面的子数组也可能位于前面的子数组。因此，我们无法判断中间的数字
是位于前面的子数组还是后面的子数组，也就无法移动两个指针来缩小查找的范围，此时，我们不
得不采用顺序查找的方法
'''
'''
改进的代码
'''
def MinInOrder(numbers,index1,index2):
    result=numbers[index1]
    for i in range(index1,index2+1):
        if result>numbers[i]:
            result=numbers[i]
    return result

def Min_num_improve(numbers):
    '''
    根据书中的C++代码改写
    '''
    
    if len(numbers)<=0:
        print("无效的参数")
    
    index1=0
    index2=len(numbers)-1
    indexMid=index1
    
    while numbers[index1]>=numbers[index2]:
        if index2-index1==1:
            indexMid=index2
            break
        
        indexMid=int((index1+index2)/2)
        
        #如果下标为index1,index2,indexMid指向的三个数字相等，
        #则只能顺序查找
        if numbers[index1]==numbers[index2] and numbers[indexMid]==numbers[index1]:
            return MinInOrder(numbers,index1,index2)
        if numbers[indexMid]>=numbers[index1]:
            index1=indexMid
        elif numbers[indexMid]<=numbers[index2]:
            index2=indexMid
    return numbers[indexMid]

a=[1,0,1,1,1]
Min_num_improve(a)


# In[76]:


'''
纯python的取巧办法
'''
def Find_Min(numbers):
    if len(numbers)<=0:
        return None
    min_num=min(numbers)
    return min_num

a=[8,9,1,4,5,6]
Find_Min(a)


# In[ ]:




