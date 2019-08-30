#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 输入两颗二叉树A和B，判断B是不是A的子结构。

# In[1]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[ ]:


'''
思路：

我们可以分成两步：第一步，在树A中找到和树B的根节点的值一样的节点R；第二步，判断树A中以R为根节点的字数是不是包含和树B一样的结构
'''
'''
判断相等

由于节点值可能是double类型，所以不能直接使用==来比较
'''
def Equal(num1,num2):
    if (num1-num2>-0.0000001) and (num1-num2<0.0000001):
        return True    else:
        return False

'''
递归判断
'''    
def DoesTree1HaveTree2(root1,root2):
    if not root2:
        return True
    if not root1:
        return False
    if(Equal(root1.val,root2.val)==False):
        return False
    return DoesTree1HaveTree2(root1.left,root2.left) and DoesTree1HaveTree2(root1.right,root2.right)

def HasSubtree(root1,root2):
    result=False
    if root1 and root2:
        if Equal(root1.val,root2.val):
            result=DoesTree1HaveTree2(root1,root2)
        if result==False:
            result=HasSubtree(root1.left,root2)
        if result==False:
            result=HasSubtree(root1.right,root2)
    return result
        

