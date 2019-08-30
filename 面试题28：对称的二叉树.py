#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
思路：

二叉树有三种遍历算法，即前序遍历、中序遍历和后序遍历。我们可以针对前序遍历定义一种对称的便利算法，即先遍历父节点，再遍历它的左子节点。如果这两种序列一样，则认为二叉树是对称的。（在遍历时同时记录为空的结点）
'''
def isSame(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val!=root2.val:
        return False
    return isSame(root1.left,root2.right) and isSame(root1.right,root2.left)

def isSymmerical(root):
    return isSame(root,root)

