#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列{1,2,3,4,5}是某栈的压栈序列，序列{4,5,3,2,1}是该压栈序列对应的一个弹出序列，但{4,3,5,1,2}就不可能是该压栈序列的弹出序列

# In[ ]:


'''
思路：

判断一个序列是否是栈的弹出序列的规律如下：如果下一个弹出的数字刚好是栈顶元素，那么直接弹出；如果下一个弹出的数字不在栈顶，则把压栈序列中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止；如果所有数字都压入栈顶后仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列
'''
def isPopOrder(pPush,pPop):
    stack=[]
    while pPop:
        if pPush and pPop[0]==pPush[0]:
            pPush.pop(0)
            pPop.pop(0)
        elif stack and stack[-1]==pPop[0]:
            stack.pop(0)
            pPop.pop(0)
        elif pPush:
            stack.append(pPush.pop(0))
        else:
            return False
    return True

