#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的节点，只能调整书中节点指针的指向。比如，输入图4.15中左边的二叉搜索树，则输出转换之后的排序双向链表
# ![title](tree.png)

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# ![title](three_part.png)

# In[ ]:


'''
思路：

在搜索二叉树中，左子节点的值总是小于父节点的值，右子节点的值总是大于父节点的值。因此，我们在将二叉搜索树转换成排序双向链表时，原先指向左子节点的指针调整为链表中指向前一个节点的指针，原先指向右子节点的指针调整为链表中指向后一个节点的指针。

由于要求转换之后的链表之后的链表时排好序的，我们可以中序遍历书中的每个节点，这是因为中序遍历算法的特点是按照从小到大的顺序遍历二叉树的每个节点。当遍历到根节点的时候，我们把树看做3部分：值为10的节点；根节点为6的左子树；根节点值为14的右子树。根据排序链表的定义，值为10的节点将和它的左子树的最大一个节点（值为8的节点）链接起来，同时它还将和右子树最小的节点（值为12的节点链接起来）,如图4.16所示

根据中序遍历的顺序，当我们遍历转换到根节点（值为10的节点）时，它的左子树已经转换成一个排序的链表了，并且处于链表中的最后一个节点是当前值最大的节点。我们把值为8的节点和根节点连接起来。此时链表中的最后一个节点就是10了。接着我们去遍历右子树，并把根节点和右子树中最小的节点链接起来。至于怎么去转换它的左子树和右子树，我们可以使用递归
'''
# class solution:
def ConvertNode(self.pNode,pLastNodeInList):
    if not pNode:
        return
    pCurrent=pNode
    if pCurrent.left:
        self.ConvertNode(pCurrent.left)
    pCurrent.left=self.pLastNodeInList
    if self.pLastNodeInList:
        self.pLastNodeInList.right=pCurrent
    self.pLastNodeInList=pCurrent
    if pCurrent.right:
        self.ConvertNode(pCurrent.right)

def Convert(self,pRootOfTree):
    self.pLastNodeInList=None
    self.ConvertNode(pRootOfTree)
    
    #pLastNodeInLast指向双向链表的尾结点
    #我们需要返回头节点
    pHeadOfLast=self.pLastNodeInList
    while pHeadOfLast and pHeadOfList.left:
        pHeadOfLast=pHeadOfLast.left
    return pHeadOfLast
        


# In[ ]:


'''
纯python的解决方法
'''
def __init__(self):
    self.Head=None
    self.Last=None
def Convert(self,pRoot):
    if not pRoot:
        return
    #中序遍历左子树
    self.Convert(pRoot.left)
    
    if self.Head==None:
        self.Head=pRoot
        self.Last=pRoot
    else:
        self.Last.right=pRoot
        pRoot.left=self.Last
        self.Last=pRoot
    self.Convert(pRoot.left)
    return self.Head
    

