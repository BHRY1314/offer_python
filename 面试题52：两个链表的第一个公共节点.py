#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入两个链表，找出它们的第一个公共节点

# In[1]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# ###### 从链表节点的定义可以看出，这两个链表是单向链表。如果两个单向链表有公共的节点，那么这两个链表从某一节点开始，它们的next都指向同一个节点。但由于是单向链表的节点，每个节点只有一个next，因此从第一个公共节点开始，之后它们所有的节点都是重合的，不可能再出现分叉。所以两个有公共节点而部分重合的链表，其拓扑形状看起来像一个Y，而不可能像X，如图5.4所示
# ![title](list.png)

# In[ ]:


'''
我们可以用栈来解决这个问题：分别把两个链表的节点放入两个栈里，这样两个链表的尾结点就位于两个栈的栈顶，接下来比较两个栈顶的节点是否相同。如果相同，则把栈顶弹出接着比较下一个栈顶，直到找到最后一个相同的节点。
之所以需要用到栈，是因为我们想同时遍历达到两个栈的尾结点。当两个链表的长度不相同时，如果我们从头开始遍历，那么达到尾结点的时间就不一致。其实解决这个问题还有一种更简单的方法:首先遍历两个链表得到它们的长度，就能知道哪个链表比较长，以及长的链表比短的链表多几个节点。在第二次遍历的时候，在较长的链表上先走若干步，接着同时在两个链表上遍历，找到第一个相同的节点就是它们的第一个公共节点
时间复杂度O(m+n)
'''
def GetListLength(pHead):
    nLength=0
    pNode=pHead
    while pNode:
        nLength+=1
        pNode=pNode.next
    return nLength

def FindFirstCommonNode(pHead1,pHead2):
    #得到两个链表的长度
    nLength1=GetListLength(pHead1)
    nLength2=GetListLength(pHead2)
    nLengthDif=nLength1-nLength2
    pListHeadLong=pHead1
    pListHeadShort=pHead2
    if nLength2>nLength1:
        pListHeadLong=pHead2
        pListHeadShort=pHead1
        nLengthDif=nLength2-nLength1
    #先在长链表上走几步，再同时在两个链表上遍历
    for i in range(nLengthDif):
        pListHeadLong=pListHeadLong.next
    while pListHeadLong and pListHeadShort and pListHeadLong!=pListHeadShort:
        pListHeadLong=pListHeadLong.next
        pListHeadShort=pListHeadShort.next
    #得到第一个公共节点
    pFirstCommonNode=pListHeadLong
    return pFirstCommonNode


# In[ ]:


'''
用栈来实现
'''
def FindFirstCommonNode(pHead1,pHead2):
    if not pHead1 or not pHead2:
        return None
    stack1=[]
    stack2=[]
    while pHead1:
        stack.append(pHead1)
        pHead1=pHead1.next
    while pHead2:
        stack.append(pHead2)
        pHead2=pHead2.next
    node=None
    while stack1 and stack2:
        node1=stack1.pop()
        node2=stack2.pop()
        if node1 is node2:
            node=node1
        else:
            break
    return node

