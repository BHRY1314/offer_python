#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
介绍：
找出数组中重复的数字，如a={2,3,1,0,2,5,3},则输出2或3，数组长度为n,所有数字都在0~n-1之间
'''

'''
思路：
从头到尾扫描这个数组中的每个数字，当扫描到下标为i的数字时，首先比较这个数字(m)是不是等于i，
如果是，则接着扫描下一个数字；如果不是，则拿他和第m个数字进行比较。如果它和第m个数字相等，
就找到了一个重复的数字（这个数字在下标为i和m的位置都出现了），如果它和第m个数字不相等，就
把第i个数字和第m个数字交换，把m放到属于它的位置。接下来在重复这个比较、交换的过程直到发现
第一个重复的数字
'''
def find_repeat(numbers):
    '''
    按照书中的C++代码重写
    '''
    temp=0
    if len(numbers)<=1:
        return None
    for i in numbers:
        if i<0 or i>(len(numbers)-1):
            return None
    for i in range(len(numbers)):
        while numbers[i]!=i:
            if numbers[i]==numbers[numbers[i]]:
                temp=numbers[i]
                return temp
            change=numbers[i]
            numbers[i]=numbers[change]
            numbers[change]=change
    return None

a=[2,3,1,0,4,5,6]
print(find_repeat(a))


# In[17]:


'''
纯python:利用第三方库
'''
from collections import Counter

def find_repeat1(numbers):
    c=Counter(numbers)
    for key,value in c.items():
        if value>1:
            return key
    return None
            

a=[2,3,1,0,2,3,6]
print(find_repeat1(a))


# In[23]:


'''
变种：
不修改数组找出重复的数字
'''

'''
思路：
我们吧从1~n的数字从中间的数字m分为两部分，前面一半为1~m,后面一半为m+1~n,如果1~m的数字
的数目超过m,那么这一半的区间里一定包含重复的数字，否则，另一半m+1~n的区间里一定包含
重复的数字。我们可以继续把包含重复数字的区间一分为二，直到找到一个重复的数字。这个过程
和二分查找算法很类似，只是多了一步统计区间里数字的数目
'''
def count_number(numbers,start,end):
    if len(numbers)<=0:
        return 0
    count=0
    for i in numbers:
        if i>=start and i<=end:
            count+=1
    return count

def find_repeat2(numbers):
    '''
    根据书中的C++代码重写
    '''
    if len(numbers)<=0:
        return None
    start=1
    end=len(numbers)-1
    while end>=start:
        middle=((end-start)>>1)+start
        count=count_number(numbers,start,middle)
        if end==start:
            if count>1:
                return start
            else:
                break
        if count>(middle-start+1):
            end=middle
        else:
            start=middle+1
    return None

a=[2,3,5,4,3,2,6,7]
print(find_repeat2(a))

'''
注：
这个算法不能保证找出所有重复的数字
'''


# In[ ]:




