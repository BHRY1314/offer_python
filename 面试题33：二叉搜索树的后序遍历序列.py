#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入一个整数数组，判断该数组是不是某二叉搜索树的遍历结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字互不相同

# In[23]:


'''
思路：

在后序遍历得到的序列中，最后一个数字是树的根节点的值。数组中前面的数字可以分为两部分：第一部分是左子树节点的值，它们都比根节点的值小；第二部分是右子树节点的值，它们都比根节点的值大。
以数组{5,7,6,9,11,10,8}为例，后序遍历结果的最后一个数字8就是根节点的值。在这个数组中，前3个数字5,7和6都比8小，是值为8的节点的左子树节点；后三个数字9,10,11都比8大，是值为8的节点的右子树节点
接下来用同样的方法确定与数组每一部分对应的子树的结构，这其实就是一个递归的过程。对于序列{5,7,6}，最后一个数字6是左子树的根节点的值。数字5比6小，是值为6的节点的左子节点，而7则是它的右子节点。同样，在序列{9,11,10}中，最后一个数字10是右子树的根节点，数字9比10小，是值为10的节点的左子节点，而11则是它的右子节点

'''
def VerifySquenceOfBST(sequence):
    if not sequence:
        return False
    length=len(sequence)
    if length==1:
        return True
    root=sequence[length-1]
    #在二叉搜索树中左子树节点的值小于根节点的值
    i=0
    while sequence[i]<root:
        i+=1
    #在二叉搜索树中左子树节点的值大于根节点的值
    j=i
    for j in range(i,length-1):
        if sequence[i]<root:
            return False
    #判断左子树是不是二叉树
    left=True
    right=True
    if i>0:
        left=VerifySquenceOfBST(sequence[:i])
    #判断右子树是不是二叉树

    if i<length-1:
        right=VerifySquenceOfBST(sequence[i:-1])
    return left and right
VerifySquenceOfBST([4,6,7,5])

