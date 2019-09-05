#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 给定一个数字，我们按照如下的规则把它翻译成字符串：0翻译成“a”，1翻译成“b”,……，11翻译成“l”,……,25翻译成“z”。一个数字可能有多个翻译。例如，12258有5种不同的翻译，分别是“bccfi”,"bwfi",“bczi”,“mcfi”和“mzi”。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# In[ ]:


'''
思路：

以12258为例，翻译12258可以分解成两个子问题：翻译1和2258，以及翻译12和258.接下来我们翻译第一个子问题中剩下的2258，同样也可以分解成两个子问题：翻译2和258，以及翻译22和58.此时，子问题翻译258重复出现了
我们可以从最小的子问题开始自下而上解决问题，这样就可以消除重复的子问题。也就是说，我们从数字的末尾开始，然后从右到左翻译并计算不同翻译的数目。
'''
def GetTranslationCount(strN):
    l=len(strN)
    counts=[0]*l
    count=0
    for i in range(l-1,-1,-1):
        count=0
        if i<l-1:
            count=counts[i+1]
        else:
            count=1
        if i<l-1:
            digit1=strN[i]-'0'
            digit2=strN[i+1]-'0'
            converted=digit1*10+digit2
            if converted>=10 and converted<=25:
                if i<l-2:
                    count+=counts[i+2]
                else:
                    count+=1
        counts[i]=count
    count=counts[0]
    del counts
    return count

def GetTranslation(number):
    if number<0:
        return 0
    numberInString=str(number)
    return GetTranslationCount(numberInString)


# In[ ]:


'''
借用别人的分析
自下而上，动态规划，从最小的问题开始 ：
f(r)表示以r为开始（r最小取0）到最右端所组成的数字能够翻译成字符串的种数。对于长度为n的数字，f(n)=0,f(n-1)=1,求f(0)。
递推公式为 f(r-2) = f(r-1)+g(r-2,r-1)*f(r)；
其中，如果r-2，r-1能够翻译成字符，则g(r-2,r-1)=1，否则为0。
因此，对于12258：
f(5) = 0
f(4) = 1
f(3) = f(4)+0 = 1
f(2) = f(3)+f(4) = 2
f(1) = f(2)+f(3) = 3
f(0) = f(1)+f(2) = 5
'''
def trans_num_to_str(num):
    if num < 0:
        return 0
    if num == 1:
        return 1
    string = str(num)
    f1, f2, g = 0, 1, 0
    for i in range(len(string)-2, -1, -1):
        if int(string[i]+string[i+1]) < 26:
            g = 1
        else:
            g = 0
        f2, f1 = f2 + g * f1, f2
    return f2

