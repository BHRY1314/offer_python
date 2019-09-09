#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 给定一棵二叉搜索树，请找出其中第k大的节点。例如，在图6.1中的二叉搜索树里，按节点数值大小顺序，第三大节点的值是4
# ![title](6_1.png)

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
思路：

如果按照中序遍历的顺序遍历一棵二叉搜索树，则遍历序列的数值是递增排序的。例如，图6.1中二叉搜索树的中序遍历序列是{2,3,4,5,6,7,8}。因此，只需要用中序遍历算法遍历一棵二叉搜索树，我们就很容易找出它的第k大节点。
'''
def KthNodeCore(pRoot,k):
    target=TreeNode(None)
    if pRoot.left:
        target=KthNodeCore(pRoot.left,k)
    if not target:
        if k==1:
            target=pRoot
        k-=1
    if not target and pRoot.right:
        target=KthNodeCore(pRoot.right,k)
    return target

def KthNode(pRoot,k):
    if not pRoot or k==0:
        return None
    return KthNodeCore(pRoot,k)


# In[ ]:


'''
另一种思路：

存成数组，然后从数组中找
'''
def dfs(self,root,res):
    if not root:
        return None
    dfs(root.left)
    res.append(root)
    dfs(root.right)
    return res
def kthNode(pRoot, k):
    res=[]
    dfs(pRoot,res)
    return res[-k] if 0<k<=len(res) else None

