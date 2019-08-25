#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入数字n，按顺序打印出1到最大的n为十进制。比如输入3，则打印1、2、3一直到最大的3位数999

# In[4]:


'''
最简单的方法
'''
'''
在书中提到，C++整型有限制，当n过大时，整型会溢出，因此无法使用这个方法
但是在Python中，整型可以认为是无限大，所以使用这个方法不会有问题
'''
def Print1nToMaxOfN(n):
    number=1
    i=0
    while i<n:
        number*=10
        i+=1
    for i in range(number):
        print("%d"%i)

Print1nToMaxOfN(1)


# In[120]:


'''
由于在Python中字符串不能修改，所以这里用列表来代替，但是原来的代码不太好修改，所以
这个方法不太能用，当N>2时就会死循环。
'''

'''
在字符串上模拟数字加法
'''

'''
1.函数Increment
这个函数实现在表示数字的字符串上增加1，同时判断是不是已经达到的最大的n位数，当
达到最大时，函数返还True。判断的方式则是根据进位。只有对“99999....9999”加1的时候，
才会在第一个字符（下标为0）的基础上产生进位，而其他情况都不会在第一个字符上产生进位。
因此，当我们发现在加1时第一个字符产生了进位，则已经是最大的n位数
'''
def Increment(number):
    isOverflow=False
    nTakeOver=0
    nLength=len(number)
    for i in range(nLength-1,-1,-1):
        nSum=int(number[i])+nTakeOver
        if i==(nLength-1):
            nSum+=1
            if nSum>=10:
                if i==0:
                    isOverflow=True
                else:
                    nSum-=10
                    nTakeOver=1
                    number[i]=str(nSum)
            else:
                number[i]=str(nSum)
                break
    return isOverflow

'''
2.函数PrintNumber
对字符串进行打印。前面提到，当数字不够n位时，在数字前面补0，打印的时候这些补位的0
不应该打印出来。在这个函数里，只有在碰到第一个非0的字符之后才开始打印，直至字符串
的结尾
'''
def PrintNumber(number):
    isBeginning0=True
    nLength=len(number)
    for i in range(nLength):
        if isBeginning0 and number[i]!='0':
            isBeginning0=False
        if not isBeginning0:
            print("%c"%number[i])
    print("")

'''
3.主函数
'''
def Print1ToMaxOfn(n):
    if n<=0:
        return
    number=['0']*n
    while not (Increment(number)):
        PrintNumber(number)

Print1ToMaxOfn(1)


# In[108]:


'''
把问题转换成数字排列

思路：

如果我们在数字前面补0，就会发现n位所有十进制其实就是n个从0到9的全排列。也就是说，我们
把数字的每一位都从0到9排列以便，就得到了所有的十进制数。只是在打印的时候，排在前面的0
不打印出来罢了
'''
def PrintNumber(number):
    isBeginning0=True
    nLength=len(number)
    for i in range(nLength):
        if isBeginning0 and number[i]!='0':
            isBeginning0=False
        if not isBeginning0:
            print("%c"%number[i])
    print("")

def Print1ToMaxOfNDigitsRecursively(number,length,index):
    if index==length-1:
        PrintNumber(number)
        return 
    for i in range(10):
        number[index+1]=str(i)
        Print1ToMaxOfNDigitsRecursively(number,length,index+1)

def Print1ToMaxDigit(n):
    if n<=0:
        return
    number=['0']*n
    for i in range(10):
        number[0]=str(i)
        Print1ToMaxOfNDigitsRecursively(number,n,0)

Print1ToMaxDigit(2)

