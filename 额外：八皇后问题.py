#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 在8\*8的国际象棋上摆放8个皇后，使其不能相互攻击，即任意两个皇后不得处于同一列、同一行或者同一条对角线上。问：有多少种摆法

# In[6]:


'''
思路：

由于8个皇后的任意两个不能处于同一行，那么肯定是每一个皇后占据一行。于是我们可以定义一个数组Column[8],数组中的第i个数字表示位于第i行的皇后的列号。先把数组的8个数字分别用0~7初始化，然后对数组进行全排列。只需判断每一个排列对应的8个皇后是不是在同一条对角线上，也就是对于数组的两个下标i和j，是否有i-j=Column[i]-Column[j]或者j-i=Column[j]-Column[i]
'''
def check(board,row,col):
    i=0
    while i<row:
        if abs(col-board[i]) in (0,abs(row-i)):
            return False
        i+=1
    return True

def queen(board,row):
    l=len(board)
    if row==l:
        print(board)
        return True
    col=0
    while col<l:
        if check(board,row,col):
            board[row]=col
            if queen(board,row+1):
                pass
        col+=1
    return False

a=[0]*8
queen(a,0)


# In[ ]:




