#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 给你一根长度为n的绳子，请把绳子剪成m段（m,n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],……,k[m],请问k[0]xk[1]xk[2]x……xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积为18

# In[8]:


'''
动态规划
'''

'''
思路：
    首先定义函数f(n)为把长度n的绳子剪成若干段后各段长度乘积的最大值。在剪第一刀的时
候，我们有n-1种可能的选择，也就是剪出来的第一段绳子的可能长度分别为1,2，……，n-1。
因此f(n)=max(f(i)*f(n-i)),其中0<i<n
    这是一个从上至下的递归公式。由于递归会有很多重复的子问题，从而有大量不必要的重复
计算。一个更好的办法是按照从下而上的顺序计算，也就是说我们先得到f(2),f(3)，再得到
f(4),f(5)，直到得到f(n)
    当绳子的长度为2时，只可能剪成长度都为1的两段，因此f(2)等于1。当绳子的长度为3时，
可能把绳子剪成长度分别为1和2的两段或者长度都为1的三段，由于1x2>1x1x1,因此f(3)=2
'''
def maxProductAfterCutting(length):
    '''
    根据书中C++代码改写
    '''
    if length<2:
        return 0
    if length==2:
        return 1
    if length==3:
        return 2
    product=[0]*(length+1)
    '''
    基本长度(这里和上面的有所不同，可以理解为当绳子长度大于等于4时，1,2,3是基本的
    长度值，比如4可以由1和3以及2和2组成，当数组小标大于4时，存储的就是长度乘积的
    最大值)（自己的理解，不知道对不对━━(￣ー￣*|||━━）
    '''
    product[0]=0
    product[1]=1
    product[2]=2
    product[3]=3
    
    max=0
    for i in range(4,length+1):
        max=0
        for j in range(1,(int(i/2)+1)):
            temp=product[j]*product[i-j]
            if max<temp:
                max=temp
            product[i]=max
    max=product[length]
    return max
'''
在上述代码中，子问题的最优解存储在数组product里。数组中的第i个元素表示把长度为i的
绳子剪成若干段之后各段长度乘积的最大值，即f(i)。我们注意到代码中第一个for循环变量
i是顺序递增的，这意味着计算顺序是自下而上的。因此在求f(i)之前，对于第一个j(0<i<j)
而言，f(j)都已经求解出来了，并且结果保存在product[j]里。为了求解f(i),我们需要求
出所有可能的f(j)xf(i-j)并比较得出它们的最大值。这就是代码中第二个for循环的功能
'''

maxProductAfterCutting(8)


# In[11]:


'''
贪婪算法
'''

'''
思路：
    如果我们按照如下的策略来剪绳子，则得到的各段绳子的长度的乘积将最大：当n≥5时，
我们尽可能多地剪长度为3的绳子；当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子。
'''
def maxProduct(length):
    if length<2:
        return 0
    if length==2:
        return 1
    if length==3:
        return 2
    
    #尽可能多地剪去长度为3的绳子段
    timesOf3=int(length/3)
    
    #当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段
    #此时更好的方法是把绳子剪成长度为2的两段，因为2x2>3x1
    if (length-timesOf3*3==1):
        timesOf3-=1
    
    timesOf2=(length-timesOf3*3)/2
    
    return (int(pow(3,timesOf3)))*(int(pow(2,timesOf2)))

'''
首先，当n≥5的时候，我们可以证明2(n-2)>n并且3(n-3)>n，也就是说，当绳子剩下的长度
大于等于5的时候，我们就把它剪成长度为3或者2的绳子段。另外，当n≥5时，3(n-3)>2(n-2),
旖旎次我们应该尽可能地多剪长度为3的绳子段
'''

maxProduct(8)    


# In[ ]:




