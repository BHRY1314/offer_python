#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2\~10为数字本身，A为1，J为11，Q为12，K为13，而大小王可以看成任意数字

# In[ ]:


'''
思路：

我们可以把5张牌看成由5个数字组成的数组。大、小王是特殊的数字，我们不妨把它们都定义为0，这样就能和其他扑克牌区分开来了。
接下来我们分析怎么判断5个数字是不是连续的，最直观的方法是把数组排序。值的注意的是，由于0可以当成任意数字，我们可以用0去补满数组中的空缺。如果排序之后的数组不是连续的，即相邻的两个数字相隔若干个数字，那么只要我们有足够的0可以补满这两个数字的空缺，这个数组实际上还是连续的。举个例子，数组排序之后为{0，1,3,4,5}，在1和3之间空缺了一个2，刚好我们有一个0，也就是我们可以把它当成2去填补这个空缺。
于是我们需要做3件事情：首先把数组排序，其次统计数组中0的个数，最后统计排序之后的数组中相邻数字之间的空缺总数。如果空缺的总数小于或者等于0的个数，那么这个数组就是连续的，反之则不连续。
最后我们还需要注意一点，如果数组中的非0数字重复出现，则该数组不是连续的。换成扑克牌的描述方式就是：如果一副牌里含有对子，不可能是顺子
'''
def IsContinuous(numbers):
    if not numbers:
        return False
    numbers.sort()
    numberOfZero=0
    numberOfGap=0
    lenght=len(numbers)
    #统计数组中0的格式
    for i in range(length):
        if numbers[i]==0:
            numberOfZero+=1
    #统计数组中的间隔数目
    small=numberOfZero
    big=small+=1
    while big<length:
        #两个数相等，有对子，不可能是顺子
        if numbers[small]==numbers[big]:
            return False
        numberOfGap+=numbers[big]-numbers[small]-1
        small=big
        big+=1
    return False if numberOfGap>numberOfZero else True


# In[ ]:


链接：https://www.nowcoder.com/questionTerminal/762836f4d43d43ca9deb273b3de8e1f4
来源：牛客网

def IsContinuous(self, numbers):
 
    if not numbers:return False
    numbers.sort()
    zeroNum = numbers.count(0)
    for i, v in enumerate(numbers[:-1]):
        if v != 0:
            if numbers[i+1]==v:return False
            zeroNum = zeroNum - (numbers[i + 1] - v) + 1
            if zeroNum < 0:
                return False
    return True


# In[ ]:


'''
Python简写版
'''
def IsContinuous(numbers):
    if not numbers:
        return False
    numbers.sort()
    numberOfZero=numbers.count(0)
    for i,v in enumerate(numbers[:-1]):
        if v!=0:
            if numbers[i+1]==v:
                return False
            numberOfZero=numberOfZero-(numbers[i+1]-v)+1
            if numberOfZero<0:
                return False
    return True

