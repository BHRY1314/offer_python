#!/usr/bin/env python
# coding: utf-8

# # 题目一：数字在排序数组中出现的次数
# 
# ### 统计一个数字在排序数组中出现的次数。例如，输入排序数组{1,2,3,3,3,3,4,5}和数字3，由于3在这个数组中出现了4次，因此输出4

# In[ ]:


'''
思路：

根据排序树组的特性，我们可以用二分查找算法来寻找。我们先分析如何用二分查找算法在数组中找到第一个k(需要寻找的数字)。二分查找算法总是先拿数组中间的数字和k作比较。如果中间的数字比k大，那么k只有可能出现在数组的前半段，下一轮我们只在数组的前半段查找就可以了。如果中间的数字比k小，那么k只有可能出现在数组的后半段，下一轮我们只在数组的后半段查找就可以了。如果中间的数字和k相等呢？我们先判断这个数字是不是第一个k。如果中间的数字的前面一个数字不是k,那么此时中间的数字刚好就是第一个k。如果中间数字的前面一个数字也是k,那么第一个k肯定在数组的前半段，下一轮我们仍然需要在数组的前半段查找。

以下的代码用递归的思路找到排序数组中的第一个k
'''
def GetFirstK(data,length,k,start,end):
    if start>end:
        return -1
    middleIndex=(start+end)/2
    middleData=data[middleIndex]
    if middleData==k:
        if (middleIndex>0 and data[middleIndex-1]!=k) or middleIndex==0:
            return middleIndex
        else:
            end=middleIndex-1
    elif middleData>k:
        end=middleIndex-1
    else:
        start=middleIndex+1
    return GetFirstK(data,length,k,start,end)
'''
我们可以用同样的思路在排序数组中找到最后一个k。如果中间数字比k大，那么k只能出现在数组的前半段。如果中间数字比k小，那么k只能出现在数组的后半段。如果中间数字等于k呢？我们需要判断这个k是不是最后一个k,也就是中间数字的下一个数字是不是也是k。如果下一个数字不是k，则中间数字就是最后一个k,否则下一轮我们还是要在数组的后半段中去查找。
'''
def GetLastK(data,length,k,start,end):
    if start>end:
        return -1
    middleIndex=(start+end)/2
    middleData=data[middleIndex]
    if middleData==k:
        if (middleIndex<length-1 and data[middleIndex+1]!=k) or middleIndex==length-1:
            return middleIndex
        else:
            start=middleIndex+1
    elif middleData<k:
        start=middleIndex+1
    else:
        end=middleIndex-1
    return GetLastK(data,length,k,start,end)
'''
在分别找到第一个k和最后一个k的下标之后，我们就能计算出k在数组中出现的次数
'''
def GetNumbersOfK(data,k):
    number=0
    length=len(data)
    if data:
        first=GetFirstK(data,length,k,0,length-1)
        last=GetLastK(data,length,k,0,length-1)
        if first>-1 and last>-1:
            number=last-first+1
    return number


# In[ ]:


'''
Python的一行代码
'''
def GetNumbersOfK(data,k):
    return data.count(k)


# In[ ]:


'''
另一种思路，运用双指针
'''
def GetNumberOfK(data, k):
    if len(data)==1:
        return 1 if data[0]==k else 0
    left=0
    right=len(data)-1
    while left<right:
        if data[left]!=k:
            left+=1
        if data[right]!=k:
            right-=1
        if data[right]==k and data[left]==k:
            return right-left+1
    return 0


# # 题目二：0~n-1中缺失的数字
# 
# ### 一个长度n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0\~n-1之内。在范围0\~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字

# In[ ]:


'''
最简单的方法：

我们可以先用公式n(n-1)/2求出数字0~n-1的所有数字之和，记为s1，接着求出数组中所有数字的和，记为s2，那个不在数组中的数字就是s1-s2的差。这种解法需要O（n）的时间求数组中所有数字的和。缺点是时间复杂度过大

比较好的思路：

因为0~n-1这些数字在数组中是排序的，因此数组中开始的一些数字与它们的下标相同。也就是说，0在下标为0的位置，1在下标为1的位置，以此类推。如果不在数组中的那个数字记为m,那么所有比m小的数字的下标都与它们的值相同。

由于m不在数组中，那么m+1处于下标为m的位置，m+2处于下标为m+1的位置，以此类推。我们发现m正好是数组中第一个数值和下标不相等的下标，因此这个问题转换成在排序数组中找出第一个值和下标不相等的元素。

我们可以基于二分查找的算法用如下过程查找：如果中间元素的值和下标相等，那么下一轮查找只需要查找右半边：如果中间元素的值和下标不相等，并且它前面一个元素和它的下标相等，这意味着这个中间的数字正好是第一个值和下标不相等的元素，它的下标就是在数组中不存的数字；如果中间元素的值和下标不相等，并且它前面一个元素和它的下标不相等，这意味着下一轮查找我们只需要在左半边查找即可
'''
def GetMissingNumber(numbers):
    if not numbers:
        return -1
    length=len(nums)
    left=0
    right=length-1
    while left<=right:
        middle=(right+left)>>1
        if numbers[middle]!=middle:
            if middle==0 or numbers[middle-1]==middle-1:
                return middle
            right=middle-1
        else:
            left=middle+1
    if left==length:
        return length
    return -1


# # 题目三：数组中数值和下标相等的元素
# 
# ### 假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。例如，在数组{-3，-1,1,3,5}中，数字3和它的下标相等
# 

# In[ ]:


'''
思路：

由于数组是单调递增排序的，因此我们可以尝试用二叉查找算法来进行。假设我们某一步抵达数组中的第i个数字。如果我们很幸运，该数字的值刚好也是i，那么我们就找到了一个数字和其下标相等

那么当数字的值和下标不相等的时候，假设数字的值为m,我们先考虑m大于i的情形，即数字的值大于它的下标，由于数组中的所有数字都唯一并且单调递增，那么对于任意大于0的k,位于下标i+k的数字的值大于或等于m+k。另外，因为m>i，所以m+k>i+k。因此，位于下标i+k的数字的值一定大于它的下标。这意味着如果第i个数字的值大于i,那么它右边的数字都大于对应的下标，我们都可以忽略。下一轮查找我们只需要从它左边的数字中查找即可

数字的值m小于它的下标i的情形和上面类似。它左边的所有数字的值都小于对应的下标，我们也可以忽略
'''
def GetNumberSameAsIndex(numbers):
    if not numbers:
        return -1
    left=0
    right=len(numbers)-1
    while left<=right:
        middle=left+((right-left)>>1)
        if numbers[middle]==middle:
            return middle
        if numbers[middle]>middle:
            right=middle-1
        else:
            left=middle+1
    return -1

