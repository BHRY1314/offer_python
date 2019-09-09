#!/usr/bin/env python
# coding: utf-8

# # 题目一：二叉树的深度
# 
# ### 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。例如，在图6.2中的二叉树的深度为4，因为它从根节点到叶节点的最长的路径包含4个节点（从根节点1开始，经过节点2和节点5，最终达到叶节点7）
# ![title](6_2.png)

# In[1]:


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
思路：

我们从另一个角度来理解树的深度。如果一棵树只有一个节点，那么它的深度为1。如果根节点只有左子树而没有右子树，那么树的深度应该是其左子树的深度加1；同样，如果根节点只有右子树而没有左子树，那么树的深度应该是其右子树的深度加1.如果既有右子树又有左子树，那么该树的深度就是其左、右子树的深度的较大值加1.比如，在图6.2所示的二叉树中，根节点为1的树有左、有两课字数，其左、右子树的根节点分别为节点2和节点3.根节点为2的左子树的深度为3，而根节点为3的右子树的深度为2，因此，根节点为1的树的深度就是4
'''
def TreeDepth(pRoot):
    if not pRoot:
        return 0
    left=TreeDepth(pRoot.left)
    right=TreeDepth(pRoot.right)
    return left+1 if left>right else right+1


# # 题目二：平衡二叉树
# 
# ### 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树。例如，图6.2中的二叉树就是一棵平衡二叉树

# In[ ]:


'''
思路：

如果我们用后序遍历的方式遍历二叉树的每个节点，那么在遍历到一个节点之前我们就已经遍历了它的左、右子树。只要在遍历每个节点的时候记录它的深度（某一节点的深度等于它到叶节点的路径的长度），我们就可以一边遍历一边判断每个节点是不是平衡的
'''
def IsBalancedTree(pRoot,depth):
    if not pRoot:
        depth=0
        return True
    left=1
    right=1
    if IsBalancedTree(pRoot.left,left) and IsBalancedTree(pRoot.right,right):
        diff=left-right
        if diff<=1 and diff>=-1:
            temp=left if left>right else right
            depth=1+temp
            return True
    return False

def IsBalanced(pRoot):
    depth=0
    return IsBalancedTree(pRoot,depth)


# In[ ]:


'''
更简洁的写法
借用一下别人的解析：
如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。
先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1
'''
def IsBalanced_Solution(root):
    if not root:
        return True
    if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
        return False
    return IsBalanced_Solution(root.left) and IsBalanced_Solution(root.right)
 
def maxDepth(root):
    if not root: 
        return 0
    return max(maxDepth(root.left),maxDepth(root.right)) + 1

