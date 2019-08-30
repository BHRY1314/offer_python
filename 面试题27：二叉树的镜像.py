#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请完成一个函数，输入一个二叉树，该函数输出它的镜像
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
# In[ ]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
思路：

画图之后就可以看出镜像其实很简单，互为镜像的树根节点一样，交换非叶节点的左右节点即可
'''
def MirrorRecursively(pNode):
    if not pNode:
        return None
    if not pNode.left and not pNode.right:
        return None
    pTemp=pNode.left
    pNode.left=pNode.right
    pNode.right=pTemp
    if pNode.left:
        MirrorRecursively(pNode.left)
    if pNode.right:
        MirrorRecursively(pNode.right)
    


# In[ ]:


'''
非递归的版本
'''
def Mirror(root):
    if not root:
        return None
    tree=[]
    tree.append(root)
    pNode=root
    while tree:
        root=tree.pop(0)
        root.left,root.right=root.right,root.left
        if root.left:
            tree.append(root.left)
        if root.right:
            tree.append(root.right)
    return pNode

