#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[24]:


'''
思路：
首先查找矩阵右上角的那个数，如果大于我们要找的数A,则证明这一列一定不会存在A，则把这一列删去（坐标左移）
如果小于A，则证明这一行一定不会存在A，则把这一行删除（坐标下移），重复这个步骤直到找到A或者计算完整个矩阵
'''
def Find(matrix,columns,rows,number):
    if (rows>0 and columns>0):
        row=0
        column=columns-1
        while(row<rows and column>=0):
            if matrix[row][column]==number:
                return True
            elif matrix[row][column]>number:
                column-=1
            else:
                row+=1
    return False
a=np.arange(0,30,2)
a=a.reshape(3,5)
print(Find(a,5,3,30))


# In[33]:


#取巧的办法
def Find_improve(matrix,number):
    if len(matrix)>0:
        if matrix[matrix==number]:
            return True
        else:
            return False
    else:
        return False
a=np.arange(0,30,2)
a=a.reshape(3,5)
print(Find_improve(a,7))


# In[ ]:




