#!/usr/bin/env python
# coding: utf-8

# # 题目一：不分行从上到下打印二叉树
# 
# ### 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# In[ ]:


'''
思路：

从上到下打印二叉树的规律：每次打印一个节点的时候，如果该节点有子节点，则把该节点的子节点放到一个队列的末尾。接下来到队列的头部取出最早进入队列的节点，重复前面的打印操作，直至队列中所有的节点都被打印出来
'''
def PrintTree(pRoot):
    if not pRoot:
        return []
    res=[]
    roots=[pRoot]
    while roots:
        node=roots.pop(0)
        res.append(node.val)
        if node.left:
            roots.append(node.left)
        if node.right:
            roots.append(node.right)
    return res
        


# # 题目二：分行从上到下打印二叉树
# 
# ### 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# In[ ]:


'''
思路：

这道题和之前的类似，也可以用一个队列来保存将要打印的节点。为了把二叉树的每一行单独打印到一行里，我们需要两个变量，一个变量表示在当前层中还没有打印的节点数；另一个变量表示下一层节点的数目
'''
def Print(pRoot):
    if not pRoot:
        return None
    res=[] #存储结果
    roots=[pRoot] #存储结点的队列
    temp=[] #用来存储每一行的值
    nextLevel=0
    toBePrinted=1
    while roots:
        node=roots.pop(0)
        temp.append(node.val)
        print("%d"%node.val)
        if node.left:
            roots.append(node.left)
            nextLevel+=1
        if node.right:
            roots.append(node.right)
            nextLevel+=1
        node.pop()
        toBePrinted-=0
        if toBePrinted==0:
            res.append(temp)
            temp=[]
            print("\n")
            toBePrinted=nextLevel
            nextLevel=0


# # 题目三：之字形打印二叉树
# 
# ### 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推

# In[ ]:


'''
思路：

按之字形打印二叉树需要两个栈。我们在打印某一层的节点时，把下一层的子节点保存到相应的栈里。如果当前打印的是奇数层（第一层，第三层等），则先保存左子节点再保存右子节点到第一个栈里；如果当前打印的是偶数层（第二层、第四层等），则先保存右子节点再保存左子节点到第二个栈里(其实简单点说，只要在上一题的代码上加上是向左打印还是向右打印的判断就可以了，若向右打印则直接逆转打印序列即可)
'''
def  PrintInZ(pRoot):
    if not pRoot:
        return None
    flag=True
    res=[] #存储结果
    roots=[pRoot] #存储结点的队列
    temp=[] #用来存储每一行的值
    nextLevel=0
    toBePrinted=1
    while roots:
        node=roots.pop(0)
        temp.append(node.val)
        print("%d"%node.val)
        if node.left:
            roots.append(node.left)
            nextLevel+=1
        if node.right:
            roots.append(node.right)
            nextLevel+=1
        node.pop()
        toBePrinted-=0
        if toBePrinted==0:
            if flag: ##奇数行，正序打印
                res.append(temp)
                flag=False  ##下一行一定是偶数行，逆序打印
            else:   ##偶数行，逆序打印
                res.append(temp[::-1])
                flag=True ##下一行一定是奇数行，正序打印
            temp=[]
            print("\n")
            toBePrinted=nextLevel
            nextLevel=0
        

