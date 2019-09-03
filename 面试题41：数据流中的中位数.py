#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数的值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据例会中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值

# In[ ]:


'''
思路:

用一个最大堆实现左边的数据容器，用一个最小堆实现右边的数据容器。往堆中插入一个数据的时间效率是O（logn）。由于只需要O（1）时间就可以得到位于堆顶的数据，因此得到中位数的时间复杂度是O（1）

接下来考虑用最大堆和最小堆实现的一些细节。首先要保证数据平均分配到两个堆中，因此两个堆中数据的数目之差不能超过1.为了实现平均分配，可以在数据的总数目是偶数时把新数据插入最小堆，否则插入最大堆。

还要保证最大堆中的所有数据都要小于最小堆中的数据。当数据的总数目是偶数时，按照前面的分配规则会把新的数据插入最小堆。如果此时这个新的数据比最大堆中的一些数据要小，可以先把这个新的数据插入最大堆，接着把最大堆中最大的数字拿出来插入最小堆，由于最终插入最小堆的数字是原最大堆中最大的数字，这样就保证了最小堆中所有数字都大于最大堆中的数字。

'''
from heapq import *
class Solution:
    def __init__(self):
        self.heaps = [], []
    def Insert(self, num):
        # write code here
        min_heap,max_heap = self.heaps
        heappush(min_heap, -heappushpop(max_heap, num))#将num放入最大堆，并弹出最大堆的最小值，取反，即取最大值，放入最小堆
        if len(large) < len(min_heap):
            heappush(max_heap, -heappop(min_heap)) #弹出最小堆中最小的值，取反，即最大的值，放入最大堆
    def GetMedian(self):
        # write code here
        min_heap,max_heap = self.heaps
        if len(max_heap) > len(min_heap):
            return float(max_heap[0])
        return (max_heap[0] - min_heap[0]) /2.0


# In[ ]:


'''
简洁的方法
'''
def __init__(self):
    self.nums= []
def Insert(self, num):
    self.nums.append(num)
    self.arr.sort()
def GetMedian():
    length = len(self.nums)
    if length % 2 == 1:
        return self.nums[length // 2]
    return (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2.0

