#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 如果一个链表中包含环，如何找出环的入口节点？

# In[2]:


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[5]:


'''
思路：

我们可以用两个指针来解决这个问题，定义两个指针（索引），同时从链表的头节点出发，一个指针一次走一步，另一个指针一次走两步。如果走得快的指针追上了走得慢的指针，那么链表就包含环；如果走得快的指针走到了链表的末尾都没有追上第一个指针，那么链表就不包含环
第二步是如何找到环的入口。我们还是可以用两个指针来解决这个问题。先定义两个指针P1和P2指向链表的头节点。如果链表中的环有n个节点，则指针P1先在链表上向前移动n步，然后两个指针以相同的速度向前移动。当第二个指针指向环的入口节点时，第一个指针已经围绕着环走了一圈，又回到了入口节点
'''
def MeetingNode(pHead):
    '''
    在存在环的前提下找到一快一慢两个指针相遇的节点
    '''
    if not pHead:
        return None
    pSlow=pHead.next
    if not pHead:
        return None
    pFast=pSlow.next
    while pFast and pSlow:
        if pFast==pSlow:
            return pFast
        pSlow=pSlow.next
        pFast=pFast.next
        if pFast:
            pFast=pFast.next
    return None

def EntryNodeOfLoop(pHead):
    meetingNode=MeetingNode(pHead)
    if not meetingNode:
        return None
    #得到环中节点的数目
    nodesInLoop=1
    pNode=meetingNode
    while pNode.next!=meetingNode:
        pNode=pNode.next
        nodesInLoop+=1
    #先移动pNode，次数为环中节点的数目
    pNode=pHead
    for i in range(nodesInLoop):
        pNode=pNode.next
    #再移动pNode和pNode2
    pNode2=pHead
    while pNode!=pNode2:
        pNode=pNode.next
        pNode2=pNode2.next
    return pNode


# In[ ]:


'''
纯Python
'''
def EntryOfLoop(head):
    if not head:
        return None
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow2=head
            while slow!=slow2:
                slow=slow.next
                slow2=slow2.next
            return slow
    return None
            

