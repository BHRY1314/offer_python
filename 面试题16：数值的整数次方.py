#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 实现函数double Power(double base,int exponent),求base的exponent次方。不得使用库函数，同时不需要考虑大数问题

# In[22]:


import math
'''
全面但不够高效的解法
'''
g_InvalidInput=False

def PowerWithUnsignedExponent(base,exponent):
    result=1.0
    for i in range(exponent):
        result*=base
    return result

def Power(base,exponent):
    '''
    根据书中C++代码改写
    '''
    g_InvalidInput=False
    if math.isclose(base,0.0) and exponent<0:
        g_InvalidInput=True
        return 0.0
    absexponent=abs(exponent)
    result=PowerWithUnsignedExponent(base,absexponent)
    if exponent<0:
        result=1.0/result
    return result

Power(2,31)


# ###### 既全面又高效的解法
# 
# ###### 这个解法会用到下面的公式
# 
# $$a^{n}=\left\{\begin{matrix}
# a^{n/2}*a^{n/2} & n=2,4,6,8,10,..... \\ 
# a^{(n-1)/2}*a^{(n-1)/2}*a & n=1,3,5,7,9,.... 
# \end{matrix}\right.$$

# In[55]:


def Power(base,exponent):
    '''
    根据书中C++代码改写
    '''
    if exponent==0:
        return 1
    if exponent==1:
        return base
    absexponent=abs(exponent)
    #由于Python中似乎不能直接对负数进行位运算，所以这里加了一点点的修改，先对指数
    #进行绝对值处理，然后判断指数是否为负数，为负数的话就取倒数
    result=Power(base,absexponent>>1)
#     result=Power(base,exponent/2)

    result*=result

    #用位与运算符代替求余运算符（%）来判断奇偶数
    if exponent & 0x1==1:
        result*=base

    if exponent<0:
        result=1.0/result

    return result

Power(0,9)


# In[ ]:




