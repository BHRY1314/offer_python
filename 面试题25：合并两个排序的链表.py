#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入两个递增排序的链表，合并这两个链表并使新链表的节点仍然是递增排序的。

# In[1]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[ ]:


'''
思路：
我们的分析从合并两个链表的头节点开始。链表1的头节点的值小于链表2的头节点的值，因此链表1的头节点将是合并后的链表的头节点

我们继续合并两个链表中剩余的节点。在两个链表中剩下的节点仍然是排序的，因此合并这两个链表的步骤和前面的步骤是一样的，我们还是比较两个头节点的值。此时链表2的头节点的值小于链表1的头节点的值，因此链表2的头节点的值将是合并剩余节点得到的链表的头节点。我们把这个节点和前面合并链表时得到的链表的尾节点(值为1的节点)链接起来。

当我们得到两个链表中值较小的头节点并把它链接到已经合并的链表之后，两个链表剩余的节点依然是排序的，因此合并的步骤和之前的步骤是一样的。这就是典型的递归过程，我们可以定义递归函数完成这一合并过程。

然后分析鲁棒性的问题。当其中一个链表时空链表时，合并后的结果就是另一个链表。当两个链表都为空时，合并的结果就是一个空链表
'''
def Merge(pHead1,pHead2):
    if not pHead1:
        return pHead2
    elif not pHead2:
        return pHead1
    pMergeHead=None
    if pHead1.val<pHead2.val:
        pMergeHead=pHead1
        pMergeHead.next=Merge(pHead1.next,pHead2)
    else:
        pMergeHead=pHead2
        pMergeHead.next=Merge(pHead1,pHead2.next)
    return pMergeHead


# In[14]:


'''
非递归处理
思路和上面类似，都是通过移动索引来进行比较，然后把比较结果在额外空间中进行更新
'''
def Merge(List1,List2):
    if not List1:
        return List2
    elif not List2:
        return List1
    l1=len(List1)
    l2=len(List2)
    nums=[0]*(l1+l2)
    index=l1+l2-1
    m=l1-1
    n=l2-1
    while m>=0 and n>=0:
        if List1[m]>List2[n]:
            nums[index]=List1[m]
            m-=1
        else:
            nums[index]=List2[n]
            n-=1
        index-=1
    if n<0:
        nums[:m+1]=List1[:m+1]
    if m<0:
        nums[:n+1]=List1[:n+1]
    return nums
a=[1,2,3,4,5]
b=[2,3,4,6,7,8]
Merge(a,b)


# In[ ]:




