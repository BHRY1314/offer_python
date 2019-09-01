#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请实现函数复制一个复杂链表。在复杂链表中，每个节点除了有一个next指针指向下一个节点，还有一个pSibling指针指向链表中的任意节点或者Null

# In[1]:


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# In[ ]:


'''
思路一：
   把复制过程分为两步，第一步是复制原始链表上的每个节点，并用next链接起来；第二步是设置每个节点的pSibling指针。假设原始链表中的某个节点N的pSibling指向节点S，由于S在链表中可能在N的前面也可能在N的后面，所以要定位S的位置需要从原始链表的头节点开始找。如果从原始链表的头节点开始沿着next经过s步找到节点S，那么在复制链表上节点N'的pSiling（记为S'）离复制链表的头节点的距离也是沿着next指针s步。用这种方法就可以为复制链表上的每个节点设置pSibling指针。（时间复杂度O(n^2）

思路二：
   步骤同样分为两步：第一步仍然是复制原始链表上的每个节点N创建N',然后把这些创建出来的节点用next链接起来。同时我们把<N,N'>的配对信息放到一个哈希表中；第二步还是设置复制链表上每个节点的pSibling。如果在原始链表中节点N的pSibling指向节点S，那么在复制链表中，对应的N'应该指向S'。由于有了哈希表，我们可以用O（1）的时间根据S找到S'

思路三：（代码使用的思路）
   第一步：根据原始链表的每个节点N创建对应的N',这一次，我们把N'链接在N的后面
'''
def CloneNodes(pHead):
    pNode=pHead
    while pNode:
        pCloned=RandomListNode(0)
        pCloned.label=pNode.label
        pCloned.next=pNode.next
        pCloned.random=None
        
        pNode.next=pCloned
        pNode=pCloned.next

'''
  第二步设置复制出来的节点的pSibling。假设原始链表上的N的pSibling指向节点S，那么其对应复制出来的N'是N的next指向的节点，同样S'也是S的next节点指向的节点
'''
def ConnectSiblingNodes(pHead):
    pNode=pHead
    while pNode:
        pCloned=pNode.next
        if pNode.random:
            pCloned.random=pNode.random.next
        pNode=pCloned.next
'''
  第三步把这个长链表拆分成两个链表：把奇数位置的节点用next链接起来就是原始链表，把偶数位置的节点用next链接起来就是复制出来的链表。
'''
def ReconnectNodes(pHead):
    pNode=pHead
    pClonedHead=None
    pClonedNode=None
    if pNode:
        pClonedHead=pClonedNode=pNode.next
        pNode.next=pClonedNode.next
        pNode=pNode.next
    while pNode:
        pClonedNode.next=pNode.next
        pClonedNode=pClonedNode.next
        pNode.next=pClonedNode.next
        pNode=pNode.next
    return pClonedHead

'''
然后把三步合并起来
'''
def Clone(pHead):
    CloneNodes(pHead)
    ConnectSiblingNodes(pHead)
    return ReconnectNodes(pHead)

