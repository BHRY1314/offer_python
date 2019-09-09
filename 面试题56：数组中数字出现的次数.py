#!/usr/bin/env python
# coding: utf-8

# # 题目一：数组中只出现一次的两个数字
# 
# ### 一个整型数组里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O（n）,空间复杂度是O（1），例如，输入数组{2,4,3,6,3,2,5,5}，因为只有4和6这两个数字出现了一次，其他数字都出现了两次，所以输出4和6
# 

# In[ ]:


'''
思路：

我们可以使用异或运算的一个性质：任何一个数字异或它自己都等于0.也就是说，如果我们从头到尾以此异或数组的每个数字，那么最终的结果刚好是那个只出现一次的数字，因为那些成对出现两次的数字全部在异或中抵消了。

我们试着把原数组分为两个子数组，使得每个子数组包含一个只出现一次的数字，而其他数字都成对出现两次。如果能够这样拆分成两个数组，那么我们就可以按照前面的方法分别找出两个只出现一次的数字了。

我们还是从头到尾以此异或数组中的每个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果，因为其他数字都出现了两次，在异或中全部抵消了。由于这两个数字肯定不一样，那么异或的结果肯定不为0，也就是说，在这个结果数字的二进制表示中至少有一位为1.我们在结果数字中找到第一个为1的位的位置，记为第n位。现在我们以第n位是不是1位标准把原数组中的数字分为两个子数组，第一个子数组中每个数字的第n位都是1，而第二个子数组中每个数字的第n位都是0.由于我们分组的标准是数字中的某一位是1还是0，那么出现了两次的数字肯定被分配到同一个子数组。因为两个相同的数字的任意一位都是相同的，我们不可能把两个相同的数字分配到两个子数组中去，于是我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其他数字都出现了两次。我们已经知道如何在数组中找出唯一一个只出现一次的数字，因此，到此为止所有的问题都已经解决了。

'''
def IsBit1(num,indexBit):
    num=num>>indexBit
    return num&1
def FindNumsAppearOnce(data):
    if not data:
        return data
    temp=0
    for i in data:
        temp^=i
    #获取temp中最低位1的位置
    index=0
    while temp&1==0:
        temp>>=1
        index+=1
    num1=num2=0
    for i in data:
        if IsBit1(i,index):
            num1^=i
        else:
            num2^=i
    return [num1,num2]


# In[ ]:


'''
大神的一行代码
'''
from collections import Counter
def FindNumsAppearOnce(data):
    return list(map(lambda c:c[0],Counter(data).most_common()[-2:]))


# # 题目二：数组中唯一只出现一次的数字
# 
# ### 在一个数组中除一个数字只出现一次之外，其他数字都出现了三次，请找出那个只出现一次的数字

# In[ ]:


'''
思路：

我们可以沿用位运算的思路。如果一个数字出现三次，那么它的二进制表示的每一位（0或者1）也出现三次。如果把所有出现三次的数字的二进制表示的每一位都分别加起来，那么每一位的和都能被3整除。

我们把数组中所有数字的二进制表示的每一位都加起来。如果某一位的和能被3整除，那么那个只出现一次的数字二进制表示中对应的那一位就是0，否则就是1
'''
def FindNumberAppearingOnce(numbers):
    if not numbers:
        return None
    bitSum=[0]*32
    length=len(numbers)
    for i in range(length):
        bitMask=1
        for j in range(31,-1,-1):
            bit=numbers[i]&bitMask
            if bit!=0:
                bitSum[j]+=1
            bitMask=bitMask<<1
    result=0
    for i in range(32):
        result=result<<1
        result+=bitSum[i]%3
    return result


# In[ ]:


'''
更简洁的写法
'''
def FindNUmberAppearingOnce(nums):
    count=[0]*32
    for i in nums:
        temp=0
        while temp<32:
            count[temp]+=num>>temp&1
            temp+=1
    res=0
    for i in range(32):
        # 因为其他数字都出现了三次，只有一个数字出现了一次
        # 也就说明count[i]%3等于0或1
        res+=count[i]%3*2**i
    return res

