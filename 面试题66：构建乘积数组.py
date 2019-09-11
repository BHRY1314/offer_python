#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 给定一个数组A[0,1,2,……,n-1],请构建一个数组B[0,1,2,……,n-1]，其中B中的元素B[i]=A[0]xA[1]x……xA[i-1]xA[i+1]x……xA[n-1]。不能使用除法
# ![6_4](6.png)
# 

# In[ ]:


'''
思路：

可以把B[i]=A[0]*A[1]*……*A[i-1]*A[i+1]*……*A[n-1]看成A[0]*A[1]*……*A[i-1]和A[i+1]*……*A[n-2]*A[n-1]两部分的乘积。因此，数组B可以用一个矩阵来创建（见图6.4）在图中，B[i]为矩阵中第i行所有元素的乘积。
不妨定义C[i]=A[0]*A[1]*……*A[i-1],D[i]=A[i+1]*……*A[n-2]*A[n-1],C[i]可以用自上而下的顺序计算出来，即C[i]==C[i-1]*A[i-1]，类似的，D[i]=D[i+1]*A[i+1]
'''
def multiply(array1,array2):
    length1=len(array1)
    length2=len(array2)
    if length1==length2 and length2>1:
        array2[0]=1
        for i in range(length1):
            array2[i]=array2[i-1]*array1[i-1]
        temp=1
        for i in range(length1-2,-1,-1):
            temp*=array1[i+1]
            array2[i]*=temp


# In[ ]:


'''
Python使用一个数组做参数
'''
def multiply(A):
    if not A:
        return None
    B=[1]*len(A)
    temp1=1
    for i in range(1,len(A)):
        temp1*=A[i-1]
        B[i]=temp
    temp2=1
    for j in range(len(A)-2,-1,-1):
        temp2*=A[j+1]
        B[j]*=temp2
    return B

