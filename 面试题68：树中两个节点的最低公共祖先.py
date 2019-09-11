#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# In[ ]:


def lowestCommonAncestor(root, A, B):
    if not root or root==A or root==B:
        return root
    left=lowestCommonAncestor(root.left,A,B)
    right=lowestCommonAncestor(root.right,A,B)
    if left and right:
        return root
    if not left:
        return right
    if not right:
        return left
    return None

