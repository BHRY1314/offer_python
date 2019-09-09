#!/usr/bin/env python
# coding: utf-8

# # 题目一：滑动窗口的最大值
# 
# ### 给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，它们的最大值分别为{4,4,6,6,6,5}

# In[ ]:


'''
思路：

一个滑动窗口可以看成一个队列。当窗口滑动时，处于窗口的第一个数字被删除，同时在窗口的末尾添加一个新的数字。这符合队列的“先进先出”特征。如果能从队列中找出它的最大值，那么这个问题也就解决了。
但是这样实现时间未必够用，我们可以换一种思路。我们并不把滑动窗口的每个数值都存入队列，而是只把有可能成为滑动窗口最大值的数值存入一个两端开口的队列。接着以输入数组{2,3,4,2,6,2,5,1}为例一步步分析。
数组的第一个数字是2，把它存入队列。第二个数字是3，由于它比前一个数字2大，因此2不可能成为滑动窗口中的最大值。先把2从队列里删除，再把3存入队列。此时队列中只有一个数字3.针对第三个数字4的步骤类似，最终队列中只剩下一个数字4。此时滑动窗口中已经有三个数字，而它的最大值4位于队列的头部。
接下来处理第四个数字2。2比队列中的数字4小，当4滑出窗口之后，2还是有可能成为滑动窗口中的最大值，因此把2存入队列的尾部。现在队列中有两个数字4和2，其中最大值4仍然位于队列的头部
第五个数字是6。由于它比队列中已有的两个数字4和2都大，因此这时4和2已经不可能成为滑动窗口中的最大值了。先把4和2从队列中删除，再把数字6存入队列。这时候最大值6仍然位于队列的头部。
第六个数字是2。由于它比队列中已有的数字6小，所以把2也存入队列的尾部。此时队列中有两个数字，其中最大值6位于队列的头部。
第七个数字是5。在队列中已有的两个数字6和2里，2小于5，因此2不可能是一个滑动窗口的最大值，可以把它从队列的尾部删除。删除数字2之后，再把数字5存入队列。此时队列里剩下两个数字6和5，其中位于队列头部的是最大值6
数组最后一个数字是1，把1存入队列的尾部。注意到位于队列头部的数字6是数组的第五个数字，此时滑动窗口已经不包括这个数字了，因此应该把数字6从队列中删除。那么怎么知道滑动窗口是否包括一个数字？应该在队列里存入是数字在数组里的下标，而不是数值。当一个数字的下标与之前处理的数字的下标之差大于或者等于滑动窗口的大小时，这个数字已经从窗口中滑出，可以从队列中删除了。
'''
def maxInWindow(num,size):
    maxInWindow=[]
    if len(num)>=size and size>=1:
        index=[]
        for i in range(size):
            while index and num[i]>=num[index[-1]]:
                index.pop()
            index.append(i)
        for i in range(size,len(num)):
            maxInWindow.append(num[index[0]])
            while index and num[i]>=num[index[-1]]:
                index.pop()
            if index and index[0]<=int(i-size):
                index.pop(0)
            index.append(i)
        maxInWindow.append(num[index[0]])
    return maxInWindows


# In[ ]:


'''
Python循环的方法
时间复杂度高
'''
def maxInWindows(num, size):
    if not num or size==0:
        return []
    if size>len(num):
        return []
    res=[]
    for i in range(len(num)-size+1):
        res.append(max(num[i:i+size]))
    return res


# In[ ]:


'''
另一种队列的写法
'''
def MaxInWindows(num,size):
    queue,res,i = [],[],0
    while size>0 and i<len(num):
        if len(queue)>0 and i-size+1 > queue[0]: #若最大值queue[0]位置过期 则弹出 
            queue.pop(0)
        while len(queue)>0 and num[queue[-1]]<num[i]: #每次弹出所有比num[i]的数字
            queue.pop()
        queue.append(i)
        if i>=size-1:
            res.append(num[queue[0]])
        i += 1
    return res

