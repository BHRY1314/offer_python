#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[ ]:


'''
题目：
输入一个链表的头节点，从尾到头反过来打印出每个节点的值
'''
'''
思路：
运用栈来实现这种顺序，每经过一个节点的时候，把该节点放到一个栈中。当遍历完整个链表后，再
从栈顶开始逐个输出节点的值
'''
def PrintList(headnode:ListNode):
    '''
    根据书中C++代码重写
    '''
    stack=[]
    pNode=headnode
    while pNode!=None:
        stack.append(pNode.val)
        pNode=pNode.next
    return stack[::-1]


# In[ ]:


'''
Python方法实现
'''
def printListFromTailToHead(self, listNode):
    # write code here
    result=[]
    currentNode=listNode
    while currentNode:
        result.insert(0,currentNode.val)
        currentNode=currentNode.next
    return result
'''

'''

