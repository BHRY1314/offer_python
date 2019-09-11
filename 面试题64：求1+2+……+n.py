#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 求1+2+3+……+n,要求不能使用乘除法、for、while、if else、switch case等关键字以及条件判断语句（A？B：C）

# In[ ]:


'''
Python利用内置函数
'''
def Sum_solution(n):
    n=range(1,n+1)
    return sum(n)


# In[ ]:


'''
利用短路求值原理
利用短路 && 来实现 if的功能
'''
def Sum_solution(n):
    res=n
    temp=res and Sum_soluton(n-1)
    res=res+temp
    return res

