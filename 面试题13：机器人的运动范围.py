#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# #### 地上有一个m行n列的方格。一个机器人从坐标（0,0）的格子开始移动，它每次可以向左，右，上，下移动一格，但不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7=18,。但它不能进入方格（35,38），因为3+5+3+8=10.请问机器人能够达到多少个格子

# In[4]:


'''
思路：

这道题目和之前的类似，同样可以使用回溯法来解决。这个方格可以看做一个mxn的矩阵。同样，
在这个矩阵中，除边界上的格子之外，其他格子都有4个相邻的格子

机器人从坐标（0,0）开始移动。当它进入坐标为（i,j）的格子时，通过检查坐标的数位和来判
断机器人是否能够进入。如果机器人能够进入坐标为（i,j）的格子，则再判断它能够进入4个相
邻的格子(i,j-1)、(i-1,j)、(i,j+1)和(i+1,j)。
'''

'''
check用来判断机器人能够进入坐标为(row,col)的方格，而函数getDigitSum用来得到一个数字
的数位之和
'''
def getDigitSum(number):
    sum=0
    while number>0:
        sum+=number%10
        number/=10
    return sum

def check(threshold,rows,cols,row,col,visited):
    if row>=0 and row<rows and col>=0 and col<cols and getDigitSum(row)+getDigitSum(col)<=threshold and visited[row*cols+col]==False:
        return True
    return False

'''
实现回溯法
'''
def movingCountCore(threshold,rows,cols,row,col,visited):
    count=0
    if check(threshold,rows,cols,row,col,visited):
        visited[row*cols+col]=True
        count=1+movingCountCore(threshold,rows,cols,row-1,col,visited)+movingCountCore(threshold,rows,cols,row,col-1,visited)+movingCountCore(threshold,rows,cols,row+1,col,visited)+movingCountCore(threshold,rows,cols,row,col+1,visited)
    return count

def movingCount(threshold,rows,cols):
    if threshold<=0 or rows<=0 or cols<=0:
        return 0
    visited=[False for i in range(rows*cols)]
    count=movingCountCore(threshold,rows,cols,0,0,visited)
    del visited
    return count

movingCount(18,40,40)


# In[ ]:




