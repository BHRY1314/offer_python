#!/usr/bin/env python
# coding: utf-8

# # 题目一：在O(1)时间内删除链表节点
# 
# ### 给定单向列表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
# 

# In[20]:


class ListNode:
     def __init__(self,x):
            self.val = x
            self.next = None


# In[31]:


'''
思路:

我们要删除节点i,先把i的下一个节点j的内容复制到i，然后把i的指针指向节点j的下一个节点。
此时再删除节点j，其效果刚好是把当前需要的节点i删除了。
如果要删除的节点位于链表的尾部，我们仍然从链表的头节点开始，顺序遍历得到该节点的前序
节点，并完成删除操作
如果链表只有一个节点，而我们又要删除链表的头节点（也就是尾结点），那么，此时我们在删
除节点之后，还需要把头节点设置为null
'''
def DeleteNode(pListHead:ListNode,pToBeDeleted:ListNode):
    if not pListHead or not pToBeDeleted:
        return
    #1.要删除的节点不是尾结点
    if pToBeDeleted.next:
        pNext=pToBeDeleted.next
        pToBeDeleted.val=pNext.val
        pToBeDeleted.next=pNext.next

        pNext=None
        pNext.val=None
        pNext.next=None
    #2.链表中只有一个节点，删除头节点（也就是尾结点）
    elif pListHead==pToBeDeleted:
        pToBeDeleted=None
        pListHead=None
    #3.链表中有多个节点，删除尾结点
    else:
        pNode=pListHead
        while pNode.next!=pToBeDeleted:
            pNode=pNode.next
        pNode.next=None
        pToBeDeleted=None
    return pListNode
'''
平均时间复杂度:[O(1)*(n-1)+O(n)]/n=O(1)
'''


# # 题目二
# 
# ### 在一个排序的链表中，如何删除重复的节点?
# 

# In[32]:


'''
思路：

我们从头遍历整个链表。如果当前节点（代码中的pNode）的值与下一个节点的值相同，那么
它们就是重复的节点，都可以被删除。为了保证删除之后的链表仍然是相连的，我们要把当
前节点的前一个节点（代码中的pPreNode）和后面值比当前节点的值大的节点相连。我们要
确保pPreNode始终与下一个没有重复的节点连接在一起
'''
def DeleteDuplication(pHead:ListNode):
    if pHead==None:
        return
    pPreNode=None
    pNode=pHead
    while pNode:
        pNext=pNode.next
        needDelete=False
        if pNext and pNext.val==pNode.val:
            needDelete=True
        if not needDelete:
            pPreNode=pNode
            pNode=pNode.next
        else:
            value=pNode.val
            pToBeDel=pNode
            while pToBeDel and pToBeDel.val==value:
                pNext=pToBeDel.next
                pToBeDel=None
                pToBeDel=pNext
            if pPreNode==None:
                pHead=pNext
            else:
                pPreNode.next=pNext
            pNode=pNext


# In[33]:


'''
别人的解法，利用了之前的方法
'''
def isRepeat(node):
    if node.next:
        if node.val==node.next.val:
            return True
    return False

def delete_repeat(pHead):
    node=pHead
    flag=False
    '''
    flag说明：例如'a'->'a'，第一次循环删除第二个'a',然后通过这个flag来进行判断
    上一次操作是否删除重复节点,如果是的话，再次判断后面还有没有'a'了，没有，
    则通过这个flag把第一个'a'也应该删除，
    '''
    while node:
        if isRepeat(node):
            # 删除重复节点，并且不进行node=node.next_node，可能出现连续多个重复节点
            pHead=DeleteNode(pHead,node)
            flag=True
        else:
            if flag:
                pHead=DeleteNode(pHead,node)
                flag=False
            node=node.next
    return pHead

