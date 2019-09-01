#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[3]:


'''
思路：

当用前序遍历的方式访问到某一节点时，我们把该节点添加到路径上，并累加该节点的值，如果该节点为叶节点，并且路径中节点值的和刚好等于输入的整数，则当前路径符合要求，我们把它打印出来。如果当前节点不是叶节点，则继续访问它的子节点。当前节点访问结束后，递归函数将自动回到它的父节点。因此，我们在函数退出之前要在路径上删除当前节点并减去当前节点的值，以确保返回父节点时路径刚好是从根节点到父节点。我们不难看出保存路径的数据结构实际上是一个栈，因为路径要与递归调用状态一致，而递归调用的本质就是一个压栈和出栈的过程
'''
def FindPath(pRoot,expectedSum,path,currentSum,res):
    if not pRoot:
        return 
    currentSum+=pRoot.val
    path.append(pRoot.val)
    #如果是叶节点，并且路径上节点值的和等于输入的值，则打印出这条路径
    isLeaf=not pRoot.left and not pRoot.right
    if currentSum==expectedSum and isLeaf:
        res.append(path[:])
        print("A path is found")
        for i in path:
            print("%d\t"%i)
        print("\n")
    #如果不是叶节点，则遍历它的子节点
    if pRoot.left:
        FindPath(pRoot.left,expectedSum,path,currentSum,res)
    if pRoot.right:
        FindPath(pRoot.right,expectedSum,path,currentSum,res)
    #在返回父节点之前，在路径上删除当前节点
    path.pop()

def FindTreePath(pRoot,expectedSum):
    if not pRoot:
        return []
    res=[]
    path=[]
    currentSum=0
    FindPath(pRoot,expectedSum,path,currentSum,res)
    return res
    


# In[ ]:


'''
别人的解法
'''
def FindPath(self, root, expectNumber):
    # write code here
    if not root:
        return []
    if root and not root.left and not root.right and root.val==expectNumber:
        return [[root.val]]
    res=[]
    left = self.FindPath(root.left, expectNumber-root.val)
    right = self.FindPath(root.right, expectNumber-root.val)
    #可进行到这一步说明此时expect Number大于root.val，对res中每个数组前加上当前根节点值
    for i in left+right:
        res.append([root.val]+i)         
    return res

