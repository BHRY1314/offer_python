#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如，把9表示成二进制是1001，有2位是1。因此，如果输入9，则该函数输出2

# In[18]:


'''
常规解法：
首先把输入的数字n和1做与运算，判断n的最低位是不是1.接着把1左移一位得到2，再和n做
与运算，就能判断n的次低位是不是1....这样反复左移，每次都能判断n的其中一位是不是1.
'''
'''
由于python没有无符号整形，这个方法不适用（原书中的flag是定义成了unsigned int）
'''
# def NumberOf1(n):
#     count=0
#     flag=1
#     while flag<n:
#         if n&flag:
#             count+=1
#         flag=flag<<1
#     return count

# NumberOf1(2)


# In[15]:


'''
优化算法
'''
'''
思路：
把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0。那么一个整数的
二进制表示中有多少个1，就可以进行多少次这样的操作
'''
'''
书中没有指出是否考虑了负数的情况，在测试时，输入负数会陷入死循环，所以对书中的代码
进行了简单修改，添加了判断
'''
def NumberOf1(n):
    count=0
    if n < 0:
        n = n+(2**32)
        #另一种写法
        #n=n & 0xFFFFFFFF
    while n:
        count+=1
        n=n&(n-1)
    return count

NumberOf1(-2)


# In[14]:


'''
纯python实现
'''
def NumberOf1_solution2(n):
    count=0
    if n<0:
        n=pow(2,32)+n
    number=bin(n).replace("0b"," ").count("1")
    return number

NumberOf1_solution2(-2)


# In[ ]:




