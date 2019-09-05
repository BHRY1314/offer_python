#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个整数，求1\~n这n个整数的十进制表示中1出现的次数。例如，输入12,1~12这些整数中包含1的数字有1、10、11和12,1一共出现了5次。

# In[ ]:


'''
思路：

我们用一个稍微大一点的数字如21345来寻找规律。我们把1~21345的所有数字分为两段，一段是1~1345，另一端是1246~21345

我们先看1346~21345中1出现的次数。1的出现分为两种情况。首先分析1出现在最高位（本例是万位）的情况。在1346~21345的数字中，1出现在10000~19999这10000个数字的万位中，一共出现了10000次。

值的注意的是，并不是对所有5位数而言在万位出现的次数都是10000簇，对于万位是1的数字如输入12345,1只出现在10000~12345的万位，出现的次数不是10000次，而是2345次，也就是除去最高数字之后剩下的数字再加上1（12345-10000+1=2346次）

接下来分析1出现在除最高位之外的其他4位数中的情况。例子中1346~21345这20000个数字中后4位中1出现的次数是8000次。由于最高位是2，我们可以再把1346~21345分为两段：1346~11345和11346~21345.每一段剩下的4位数字中，选择其中一位是1，其余三位可以在0~9这10个数字中任意选择，因此根据排列组合原则，总共出现的次数是2*4*10^3=8000次。

至于在1~1345中1出现的次数，我们就可以用递归求得了。这也是我们为什么要把1~21345分为1~1345和1346~21345两段的原因。因为把21345的最高位去掉就变成1345，便于我们采用递归的思路(为了编程方便，我们先把数字转换成字符串)
'''
# def PowerBase10(n):
#     result=1
#     for i in range(n):
#         return*=10
#     return result
# i=0
# def NumberOf1(strN):
#     if not strN or strN[0]<'0' or strN[0]>'9':
#         return 0
#     first=int(strN[0]-'0')
#     l=len(strN)
#     if l==1 and first==0:
#         return 0
#     if l==1 and first>0:
#         return 1
#     #假设strN是'21345'
#     #numberFirstDigit是数字，10000~19999的第一位中的数目
#     numFirstDigit=0
#     if first>1:
#         numberFirstDigit=PowerBase10(l-1)
#     elif first==1:
#         numberFirst=int(str[i+i:])+1
#     #numberOtherDigit是1346~21345除第一位之外的数位中的数目
#     numOtherDigits=first*(l-1)*PowerBase10(l-2)
#     #numberRecursive是1~1345中的数目
#     numRecursive=NumberOf1(str[i+1:])
    
#     return numFirstDigit+numOtherDigits+numRecursive

# def NumberOf1Between1AndN(n):
#     if n<=0:
#         return 0
#     strN=str(n)
#     return NumberOf1(strN)


# In[ ]:


'''
更简洁的解法
'''
def NumberOf1Between1AndN(n):
    count=0
    nums=n
    base=1
    while nums:
        last=nums%10
        nums=nums/10
        count+=nums*last
        if last==1:
            count+=n%base+1
        elif last>1:
            count+=base
        base*=10
    return count


# In[ ]:


'''
Python取巧的方法
'''
def NumberOf1Between1AndN(n):
    if n<0:
        return 0
    return ''.join([str(i) for i in range(1, n+1)]).count('1')

