#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min,push及pop的时间复杂度都是O(1)

# In[ ]:


'''
思路：

使用辅助栈，把每次的最小元素（之前的最小元素和新压入栈的元素两者的较小值）都保存起来放到另外一个辅助栈里。
如果每次都把最小元素压入辅助栈，那么就能保证辅助栈的栈顶一直都是最小元素。当最小元素从数据栈内被弹出之后，同时弹出辅助栈的栈顶元素，此时辅助栈的新栈顶元素就是下一个最小值。
'''
m_data=[]
m_min=[]
def push(value):
    m_data.append(value)
    if len(m_min)==0 or m_min[-1]>value:
        m_min.append(value)
    else:
        m_min.append(m_min[-1])

def pop():
    assert(len(m_data)>0 and len(m_min)>0)
    m_data.pop()
    m_min.pop()

def top():
    return m_data[-1]

def min():
    assert(len(m_data)>0 and len(m_min)>0)
    return m_min[-1]

