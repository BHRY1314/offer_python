#!/usr/bin/env python
# coding: utf-8

# #  题目
# 
# ### 求斐波那契数列的第n项

# ###  斐波那契数列
# $$ f(n)\begin{cases}
#  0& \text n=0 \\ 
#  1& \text n=1 \\ 
#  f(n-1)+h(n-2)& \text n>1 
# \end{cases}$$

# In[5]:


'''
最简单的递归形式
但是存在严重的效率问题
'''
def Fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)

Fibonacci(10)


# In[6]:


'''
使用循环
改进的版本，时间复杂度O(n)
'''
def Fibonacci1(n):
    result=[0,1]
    if n<2:
        return result[n]
    fibNMinusOne=1
    fibNMinusTwo=0
    finbN=0
    for i in range(2,n):
        fibN=fibMinusOne+fibMinusTwo
        fibMinusTwo=fibMinusOne
        fibMinusOne=fibN
    return fibN

Fibonacci(10)


#  ## 时间复杂度O(logn)但是不实用的解法（了解即可）
#  
#  ### 这种方法需要使用一个数学公式：
#  $$\begin{bmatrix}
# f(n) & f(n-1) \\ 
# f(n-1) & f(n-1) 
# \end{bmatrix}
# =\begin{bmatrix}
# 1 & 1 \\ 
# 1 & 0 
# \end{bmatrix}^{n-1}$$
# ### 我们只需求解得这个$$\begin{bmatrix}
# 1 & 1 \\ 
# 1 & 0 
# \end{bmatrix}^{n-1}$$ 
# ### 就可以得到f(n),现在的问题转换为如何求矩阵的乘方。如果只是简单地从0开始循环，n次方需要n次运算，则时间复杂度任然是O(n),并不比前面的方法块。但我们可以考虑乘方的以下性质
# 
# $$a^{n}=\begin{cases}
# a^{n/2}*a^{n/2} & \text n=2,4,6,8,... \\ 
# a^{(n-1)/2}*a^{(n-1)/2}*a & \text n=1,3,5,7,...
# \end{cases}$$
# 
# ### 从这个公式我们可以看出，想要求得n次方，就要先求的n/2次方，再把n/2次方的结果平方一下即可，这可以用递归的思路实现

# 
# ### ---------------------------------------------------------------------------------------
# 
# #  题目2：青蛙跳台阶问题
# 
# ### 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶，求该青蛙跳上一个n级的台阶总共有多少种跳法
# 

# In[7]:


'''
实际就是斐波那契数列的计算，代码可以参考上面的例子
'''
def Fibonacci1(n):
    result=[0,1]
    if n<2:
        return result[n]
    fibNMinusOne=1
    fibNMinusTwo=0
    finbN=0
    for i in range(2,n):
        fibN=fibMinusOne+fibMinusTwo
        fibMinusTwo=fibMinusOne
        fibMinusOne=fibN
    return fibN

Fibonacci(10)

