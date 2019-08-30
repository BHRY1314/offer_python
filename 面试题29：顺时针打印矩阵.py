#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。例如，如果输入如下矩阵

# $$\begin{bmatrix}
# 1 &2  &3  &4 \\ 
# 5 &6  &7  &8 \\ 
# 9 &10  &11  &12 \\ 
# 13 &14  &15  &16 
# \end{bmatrix}$$

# ### 则依次打印出数字1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# In[ ]:


'''
思路；

通过画图，我们可以发现左上角的坐标中行标和列标总是相同的，于是可以在矩阵中选取左上角为（start,start）的一圈作为我们分析的目标。
对于一个5x5的矩阵而言，最后一圈只有一个数字，对应的坐标为（2,2）。我们发现5>2x2.对于一个6x6的矩阵而言，最后一圈有4个数字，其左上角的坐标仍然为（2,2）。我们发现6>2x2依然成立。于是可以得出，让循环继续的条件是columns>startX*2而且rows>startY*2.所以我们可以使用如下的循环
'''
def PrintMatrixClockwisely(numbers,columns,rows):
    if not numbers or columns<=0 or rows<=0:
        return
    start=0
    while columns<start*2 and rows>start*2:
        PrintMatrixInCircle(numbers,columns,rows,start)
        start+=1

'''
我们可以把打印一圈分为四步：第一步，从左到右打印一行；第二步，从上到下打印一列；第三步，从右到左打印一行；第四部，从下到上打印一列。每一步我们根据起始坐标和中职坐标用一个循环就能打印出一行或者一列。
我们要仔细分析打印时每一步的前提条件。第一步总是需要的，因为打印一圈至少有一步。如果只有一行，那就不用第二步了。也就是需要第二步的前提条件是终止行号大于起始行号。需要第三步打印的前提条件是圈内至少有两行两列，也就是说，除了要求终止行号大于起始行号，还要求终止列号大于起始列号。同理，需要打印第四步的前提条件是至少有三行两列，因此要求终止行号比起始行号至少大2，同时终止列号大于起始列号
'''
def PrintMatrixCircle(numbers,columns,rows,start):
    endX=columns-1-start
    endY=rows-1-start
    #从左到右打印一行
    for i in range(start,endX+1):
        number=numbers[start][i]
        printNumber(number)
    #从上到下打印一列
    if start<endY:
        for i in range(start+1,endY+1):
            number=numbers[i][endX]
            printNumber(number)
    #从右到左打印一行
    if start<endX and start<endY:
        for i in range(endX-1,start+1,-1):
            number=numbers[endY][i]
            printNumber(number)
    #从下到上打印一列
    if start<endX and start<endY-1:
        for i in range(endY-1,start+1,-1):
            number=numbers[i][start]
            printNumber(number)


# In[7]:


'''
用旋转魔方的方式，一直取出第一行；
 
例如
 
    1 2 3
    4 5 6
    7 8 9
输出并删除第一行后，变为
 
    4 5 6
    7 8 9
再进行一次逆时针旋转，就变成：
 
    6 9
    5 8
    4 7
继续重复上述操作即可。
'''
def printMatrix(matrix):
    result=[]
    while matrix:
        result+=matrix[0]
        del matrix[0]
        matrix=zip(*matrix)[::-1]
        print("matrix:",matrix)
    return result


# In[ ]:




