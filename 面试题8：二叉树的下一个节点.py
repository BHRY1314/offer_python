#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
       self.parent = None


# # 题目
# #### 给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？书中的节点除了有两个分别指向左，右子节点的指针，还有一个指向父节点的指针

# In[ ]:


'''
思路：
如果一个节点有右子树，那么它的下一个节点就是它的右子树中的最左子节点。也就是说，从右子
节点出发一直沿着指向左子节点的指针，我们就能找到它的下一个节点。接着我们分析一个节点没
有右子树的情形。如果节点是它父节点的左子节点，那么它的下一个节点就是它的父节点。如果一
个节点既没有右子树，而且它还是它父节点的右子节点，那么这种情形就比较复杂。我们可以沿着
指向父节点的指针一直向上遍历，知道找到一个是它父节点的左子节点的节点。如果这样的节点存
在，那么这个节点的父节点就是我们要找的下一个节点
'''
def GetNext(pNode:TreeNode):
    '''
    根据书中的C++代码改写
    '''
    if not pnode:
        return None
    pNext=None
    if pNode.right!=None:
        pNode=pNode.right
        while pNode.left!=None:
            pNode=pNode.left
        return pNode
    else:
        while pNode.parent!=None:
            if pNode==pNode.parent.left:
                return pNode.parent
            pNode=pNode.parent
    return None

