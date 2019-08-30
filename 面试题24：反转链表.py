#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点

# In[1]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[ ]:


'''
思路：
我们可以定义三个指针（索引），分别指向当前遍历到的节点，它的前一个节点以及后一个节点。而且反转后链表的头节点是原始链表的尾结点，即当next为null的节点
'''
def ReverseList(pHead):
    pReversedHead=None
    pNode=pHead
    pPrev=None
    while pNode:
        pNext=pNode.next
        if not pNext:
            pReversedHead=pNext
        pNode.next=pPrev
        pPrev=pNode
        pNode=pNode.next
    return pReversedHead


# In[ ]:


'''
简化版的代码
'''
def Reverse(head):
    pPrev=None
    while head:
        pNext=head.next
        head.next=pPrev
        pPrev,head=head,pNext
    return pPrev

