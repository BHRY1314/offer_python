#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个链表，输出该链表倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

# In[2]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[ ]:


'''
思路（实现只遍历链表一遍）:

我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1步，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，当第一个指针达到链表的尾节点时，第二个（走在后面的）指针正好指向倒数第k个节点
'''
# def FindKthToTail(pHead,k):
#     pAhead=pHead
#     pBehind=None
#     for i in range(k-1):
#         pAhead=pAhead.next
#     pBehind=pHead
#     while pAhead.next:
#         pAhead=pAhead.next
#         pBehind=pBehind.next
#     return pBehind
'''
由于这段代码鲁棒性不够，在以下三种情况下会导致崩溃：
（1）输入的pHead为空
（2）输入的以pHead为头节点的链表的节点总数少于k
（3）输入的参数k为0
'''


# In[ ]:


'''
根据上述三种情况进行优化：

如果输入的链表头指针为空，那么整个链表为空，此时查找倒数第k个节点自然应该返回空。如果输入的k是0，也就是试图查找倒数第0个节点，由于我们计数是从1开始的，因此输入0没有实际意思，也可以返回空。如果链表的节点数少于k，那么for循环中遍历链表可能会出现指向空的next，因此我们在for循环中应该加一个if判断
'''
def FindKthToTail_1(pHead,k):
    if not pHead or k==0:
        return None
    pAhead=pHead
    pBehind=None
    for i in range(k-1):
        if pAhead.next:
            pAhead=pAhead.next
        else:
            return None
    pBehind=pHead
    while pAhead.next:
        pAhead=pAhead.next
        pBehind=pBehind.next
    return pBehind


# In[ ]:


'''
纯Python的代码
'''
def FindKth(head,k):
    if not head or k==0:
        return None
    result=[]
    while head:
        result.append(head)
        head=head.next
    if k>len(result) or k<1:
        return
    return result[-k]

