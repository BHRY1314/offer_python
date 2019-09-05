#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物

# In[ ]:


'''
思路：

我们先用递归的思路来分析。我们先定义第一个函数f(i,j)表示到达坐标为(i,j)的格子时能拿到的礼物总和的最大值。根据题目要求，我们有两种可能的途径到达坐标为(i,j)的格子：通过格子（i-1,j）或者(i,j-1)。所以f(i,j)=max(f(i-1,j),f(i,j-1)+gift[i,j])。gift[i,j]表示坐标为(i,j)的格子里的礼物的价值

相比而言，循环的效率要比递归高很多。为了缓存中间计算结果，我们需要一个辅助的二维数组。数组中坐标为(i,j)的元素表示到达坐标为(i,j)的格子时能拿到礼物价值总和的最大值
'''
def getMaxValue(values,rows,cols):
    if not value or rows<=0 or cols<=0:
        return 0
    maxValues=[[0]*cols for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            left=0
            up=0
            if i>0:
                up=maxValue[i-1][j]
            if j>0:
                left=maxValue[i][j-1]
            maxValue[i][j]=max(left,up)+values[i*cols+j]
    maxValue=maxValue[rows-1][cols-1]
    return maxValue


# In[ ]:


'''
优化:

到达坐标为(i,j)的格子时能够拿到的礼物的最大价值只依赖坐标为(i-1,j)和(i,j-1)的两个格子，因此第i-2行及更上面的所有格子礼物的最大价值实际上没有必要保存下来。我们可以用一个一维数组来替代前面代码中的二维矩阵maxValue。该一维数组的长度为棋盘的列数n。当我们计算达到坐标为(i,j)的格子时能够拿到的礼物的最大价值f(i,j)，数组中前j个数字分别是f(i,0),f(i,1),……,f(i,j-1)，数组从下标为j的数字开始到最后一个数字，分别为f(i-1,j),f(i-1,j+1),……,f(i-1,n-1)。也就是说，该数组前面j个数字分别是当前第i行前面j个格子礼物的最大价值，而之后的数字分别保存前面第i-1行n-j个格子礼物的最大价值
'''
def getMaxValue(values,rows,cols):
    if not values or rows<=0 or cols<=0:
        return 0
    maxValues=[0]*cols
    for i in range(rows):
        for j in range(cols):
            left=0
            up=0
            if i>0:
                up=maxValue[i]
            if j>0:
                left=maxValue[j-1]
            maxValue[j]=max(left,up)+values[i*cols+j]
    maxValue=maxValues[cols-1]
    return maxValue

