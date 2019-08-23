#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# #### 设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左，右，上，下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3x4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用下划线标出）。但矩阵中不包含字符“abfb”的路径，因为字符串的第一个字符b占据了矩阵的第一行第二个格子之后，路径不能再次进入这个格子
# 

# $$\begin{bmatrix}
# a & \underline{b} & t  & g \\ 
# c & \underline{f} & \underline{c} & s \\ 
# j & d & \underline{e} & h 
# \end{bmatrix}$$

# In[46]:


'''
思路：
首先，在矩阵中任选一个格子作为路径的起点。假设矩阵中某个格子的字符为ch,并且这个格子将对
应路径上的第i个字符。如果路径上的第i个字符不是ch，那么这个格子不可能处于路径上的第i个位
置。如果路径上的第i个字符正好是ch，那么到相邻的格子寻找路径上的第i+1个字符。除矩阵边界
上的格子之外，其他格子都有4个相邻的格子。重复这个过程，直到路径上的所有字符都在矩阵中
找到相应的位置。

由于回溯法的递归特性，路径可以被看成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，
在与第n个字符对应的格子的周围都没有找到第n+1个字符，这时候只好在路径上回到第N-1个字符，
重新定位第n个字符
'''
import numpy as np

def hasPathCore(matrix,rows,cols,row,col,strs,pathLength,visited):
    '''
    根据书中代码改写
    '''
    if pathLength>=len(strs):
        return True
    hasPath=False
    if row>=0 and row<rows and col>=0 and col<cols and matrix[row*cols+col]==strs[pathLength] and visited[row*cols+col]==False:
        pathLength+=1
        visited[row*cols+col]=True
        hasPath=hasPathCore(matrix,rows,cols,row,col-1,strs,pathLength,visited)        or hasPathCore(matrix,rows,cols,row-1,col,strs,pathLength,visited)        or hasPathCore(matrix,rows,cols,row,col+1,strs,pathLength,visited)        or hasPathCore(matrix,rows,cols,row+1,col,strs,pathLength,visited)
        if hasPath==False:
            pathLength-=1
            visited[row*cols+col]=False
    return hasPath

def hasPath(matrix,rows,cols,strs):
    if len(matrix)<=0 or rows<1 or cols<1 or len(strs)<=0:
        return False
    visited=np.array([0]*(rows*cols))
    pathLength=0
    for row in range(0,rows):
        for col in range(0,cols):
            if hasPathCore(matrix,rows,cols,row,col,strs,pathLength,visited):
                return True
            
    del visited
    return False

a=np.array(['a','b','t','g','c','f','c','s','j','d','e','h'])
hasPath(a,3,4,'btce')


# In[53]:


'''
重新改写了一下
'''
def FindPath(matrix,rows,cols,row,col,path,pathLength,visited):
    if pathLength>=len(path):
        return True
    hasPath=False
    if row>=0 and row<rows and col>=0 and col<cols and matrix[row*cols+col]==path[pathLength] and visited[row*cols+col]==False:
        pathLength+=1
        visited[row*cols+row]=True
        hasPath=FindPath(matrix,rows,cols,row,col-1,path,pathLength,visited) or FindPath(matrix,rows,cols,row-1,col,path,pathLength,visited) or FindPath(matrix,rows,cols,row,col+1,path,pathLength,visited) or FindPath(matrix,rows,cols,row+1,col,path,pathLength,visited)
        if not hasPath:
            pathLength-=1
            visited[row*rows+col]=False
    return hasPath

def hasPath(matrix,rows,cols,path):
    if path is None or path=='' or rows<=0 or cols<=0:
        return False
    visited=[False for i in range(rows*cols)]
    pathLength=0
    for i in range(rows):
        for j in range(cols):
            if FindPath(matrix,rows,cols,i,j,path,pathLength,visited):
                return True
    return False

a=np.array(['a','b','t','g','c','f','c','s','j','d','e','h'])
hasPath(a,3,4,'btce')


# In[ ]:




