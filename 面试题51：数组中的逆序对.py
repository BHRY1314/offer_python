#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字构成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。例如，在数组{7,5,6,4}中，一共存在5个逆序对，分别是（7,6）、（7,5）、（7,4）、（6,5）和（5,4）

# ###### 思路
# 
# ###### 如图5.2(a)和图5.2(b)所示，我们先把数组分解成两个长度为2的子数组，再把这两个子数组分别拆分成两个长度为1的子数组。接下来一边合并相邻的子数组，一边统计逆序对的数目。在第一对长度为1的子数组{7}，{5}中，7大于5，因此{7,5}组成一个逆序对。同样，在第二队长度为1的子数组{6}、{4}中，也有逆序对（6，4）。由于我们已经统计了这两对子数组内部的逆序对，因此需要把这两对子数组排序，如图5.2（c）所示，以免在以后的统计过程中再重复统计
# ![title](5_2.png)
# ###### 接下来我们统计两个长度为2的子数组之间的逆序对。我们在图5.3中细分图5.2（d）的合并子数组及统计逆序对的过程。
# ![title](5_3.png)
# ###### 注：图中省略了最后一步，即复制第二个子数组最后剩余的4到辅助数组。（a）P1指向的数字大于P2指向的数字，表明数组中存在逆序对。P2指向的数字是第二个子数组的第二个数字，因此第二个子数组中有两个数组比7小。把逆序对数目加2，并把7复制到辅助数组，向前移动P1和P3。（b）P1指向的数字小于P2指向的数字，没有逆序对。把P2指向的数字复制到辅助数组，并向前移动P2和P3.（c）P1指向的数字大于P2指向的数字，因此存在逆序对。由于P2指向的数字是第二个子数组的第一个数字，子数组只有一个数字比5小。把逆序对数目加1，并把5复制到辅助数组，向前移动P1和P3

# In[ ]:


'''
我们先用两个指针分别指向两个子数组的末尾，并每次比较两个指针指向的数字。如果第一个子数组中的数字大于第二个子数组中的数字，则构成逆序对，并且逆序对的数目等于第二个子数组中剩余数字的个数，如图5.3(a)和图5.3(c)所示。如果第一个数组的数字小于或等于第二个数组中的数字，则不构成逆序对，如图5.3(b)所示。每次比较的时候，我们都把较大的数字从后往前复制到一个辅助数组，确保数组中的数字是递增排序的，在把较大的数字复制到辅助数组之后，把对应的指针向前移动一位，接下来进行下一轮比较。
'''
def InversePairsCore(data,copy,start,end):
    if start==end:
        copy[start]=data[start]
        return 0
    length=(end-start)/2
    left=InversePairsCore(copy,data,start,start+length)
    right=InversePairsCore(copy,data,start+length+1,end)
    #i初始化为前半段最后一个数字的下标
    i=start+length
    #j初始化为后半段最后一个数字的下标
    j=end
    indexCopy=end
    count=0
    while i>=start and j>=start+length+1:
        if data[i]>data[j]:
            indexCopy-=1
            i-=1
            copy[indexCopy]=data[i]
            count+=j-start-length
        else:
            indexCopy-=1
            j-=1
            copy[indexCopy]=data[j]
    for i in range(start,-1,-1):
        indexCopy-=1
        copy[indexCopy]=data[i]
    for j in range(start+length+1,-1,-1):
        indexCopy-=1
        copy[indexCopy]=data[j]
    return left+right+count

def InverseParis(data):
    if not data:
        return 0
    length=len(data)
    copy=[0]*length
    for i in range(length):
        copy[i]=data[i]
    count=InversePairsCore(data,copy,0,length-1)
    return count


# In[ ]:


'''
Python简写版
'''
def __init__(self):
    self.count = 0
def mergeSort(self, data):
    if len(data) < 2: 
        return data:
    mid = len(data)//2
    left = self.mergeSort(data[:mid])
    right = self.mergeSort(data[mid:])
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            self.count += (len(left)-i)
    return res + left[i:] + right[j:]
def InversePairs(self, data):
    # write code here
    if len(data) < 2: 
        return 0
    self.mergeSort(data)
    return self.count % 1000000007

