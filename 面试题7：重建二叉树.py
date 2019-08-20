#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
题目：输入某二叉树的前序遍历和中序遍历的结果，重建该二叉树，假设输入的前序遍历和中序遍历
的结果都不含重复的数字
'''
'''
思路：
在中序遍历中找到根节点的位置，然后通过递归构建左右子树
'''
'''
纯python实现
'''
def TreeBuild(pre,tin):
    if not pre or not tin:
        return None
    root=TreeNode(pre.pop(0))
    index=tin.index(root.val)
    root.left=TreeBuild(pre,tin[:index])
    root.right=TreeBuild(pre,tin[index+1:])
    return root

a=[1,2,4,7,3,5,6,8]
b=[4,7,2,1,5,3,8,6]
TreeBuild(a,b)

