#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n,打印出s的所有可能的值出现的概率

# In[16]:


'''
思路：

基于递归求解，缺点：时间复杂度高

要想求出n个骰子的点数和，可以先把n个骰子分成两堆：第一堆中已有一个；另一堆有n-1个。单独的那一个有可能出现1~6的点数。我们需要计算1~6的每一种点数和剩下的n-1个骰子来计算点数和。接下来把剩下的n-1个骰子仍然分成两堆：第一堆只有一个；第二堆有n-2个。我们把上一轮那个单独骰子的点数和这一轮单独骰子的点数想加，再和剩下的n-2个投机来计算点数和。不难看出，这是一个递归的思路
我们可以定义一个长度为6n-n+1的数组，将和为s的点数出现的次数保存到数组的第s-n个元素里
'''
g_MaxValue=6
def Probability(original,current,sum,pProbabilities):
    if current==1:
        pProbabilities[sum-original]+=1
    else:
        for i in range(1,g_MaxValue+1):
            Probability(original,current-1,i+sum,pProbabilities)

def GetProbability(number,pProbabilities):
    for i in range(1,g_MaxValue+1):
        Probability(number,number,i,pProbabilities)
def PrintProbability(number):
    if number<1:
        return None
    maxSum=number*g_MaxValue
    pProbabilities=[0]*(maxSum-number+1)
    
    GetProbability(number,pProbabilities)
    
    total=pow(g_MaxValue,number)
    for i in range(number,maxSum+1):
        ratio=pProbabilities[i-number]/total
        print("%d:%e\n"%(i,ratio))

PrintProbability(3)


# In[15]:


'''
基于循环求点数，时间效率好

可以换一种思路来解决这个问题。我们可以考虑用两个数组来存储骰子点数的每个总数出现的次数。在一轮循环中，第一个数组中的第n个数字表示骰子和为n出现的次数。在下一轮循环中，我们加上一个新的骰子，此时和为n的骰子出现的次数应该等于上一轮循环中骰子点数都和为n-1、n-2、n-3、n-4、n-5和n-6的次数的总和，所以我们把另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6个数字之和
'''
def PrintProbability(number):
    if number<1:
        return None
    pProbabilities=[[0]*(g_MaxValue*number+1),[0]*(g_MaxValue*number+1)]
    flag=0
    for i in range(1,g_MaxValue+1):
        pProbabilities[flag][i]=1
    for k in range(2,number+1):
        for i in range(k):
            pProbabilities[1-flag][i]=0
        for i in range(k,g_MaxValue*k+1):
            pProbabilities[1-flag][i]=0
            for j in range(1,i):
                pProbabilities[1-flag][i]+=pProbabilities[flag][i-j]
        flag=1-flag
    total=pow(g_MaxValue,number)
    for i in range(number,g_MaxValue*number+1):
        ratio=pProbabilities[flag][i]/total
        print("%d:%e\n"%(i,ratio))
    
PrintProbability(3)


# In[18]:


'''
Python使用动态规划
原文链接：http://www.ishenping.com/ArtInfo/1041907.html
'''
def offer60(n):
    # 第n个骰子得到k的次数由n-1个骰子 k-1 ~ k-6 的个数和所决定，动规递推式
    # f(n,k) = f(n-1,k-1) + f(n-1,k-2) + f(n-1,k-3)+ f(n-1,k-4)+ f(n-1,k-5)+ f(n-1,k-6)
    if n < 0: return
    number = [1 for _ in range(6)]
    total = 6 ** n
    for _ in range(2, n + 1):
        tmp = [number[0]]
        for i in range(1, len(number)):  # 这样的处理方式避免重复运算
            if i - 6 < 0:
                tmp.append(tmp[-1] + number[i])
            else:
                tmp.append(tmp[-1] - number[i - 6] + number[i])
        new = [number[-1]]  # 随着骰子数增多，每次多5种结果
        for i in range(-2, -6, -1):
            new.insert(0, new[i + 1] + number[i])
        # new = [(sum(number[-i:])) for i in range(5, 0, -1)]   这种处理冗余计算
        number = tmp + new
    return [i / total for i in number]
offer60(3)


# In[ ]:




