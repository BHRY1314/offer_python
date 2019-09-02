#!/usr/bin/env python
# coding: utf-8

# # 题目
# 
# ### 请实现两个函数，分别用来序列化和反序列化二叉树
# 
# ##### 注
# ##### 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
# 
# ##### 二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

# In[ ]:


'''
思路：

如果二叉树的序列化是从根节点开始的，那么相应的反序列化在根节点的数值读出来的时候就可以开始了。因此，我们可以根据前序遍历的顺序来序列化二叉树，因为前序遍历是从根节点开始的。在遍历二叉树碰到null指针时，这些null指针序列化为一个特殊的字符（如“$”）。另外，节点的数值之间要用一个特殊字符（如','）隔开
'''
# def Serialize(pRoot,stream):
#     if not pRoot:
#         stream=stream+"$"
#         return
#     stream=stream+str(pRoot.val)+","
#     Serialize(pRoot.left,stream)
#     Serialize(pRoot.right,stream)
def Serialize(pRoot):
    if not pRoot:
        return '$'
    return str(pRoot.val)+','+Serialize(pRoot.left)+','+Serialize(pRoot.right)
'''
我们以字符串“1,2,4,$,$,$,3,5,$,$,6,$,$”为例分析如何反序列化二叉树。第一个读出的数字是1.由于前序遍历是从根节点开始的，这是根节点的值。接下来读出的数字是2，根据前序遍历的规则，这是根节点的左子节点的值。同样，接下来的数字4是值为2的节点的左子节点。接着从序列化字符串里读出两个字符“$”，这表明值为4的节点的左、右节点均为Null指针，因此它是一个叶节点。接下来回到值为2的节点，重建它的右子节点。由于下一个字符是'$'，这表明值为2的节点的右子节点为Null指针。这个节点的左、右子树都已经构建完毕，接下来回到根节点，反序列化根节点的右子树。

下一个序列化字符串中的数字是3，因此右子树的根节点的值为3。它的左子节点是一个值为5的叶节点，因此接下来的三个字符是“5，$，$”。同样，它的右子节点是值为6的叶节点，因为最后3个字符是“6，$,$”
'''
def Deserialize(pRoot,stream):
    if len(stream)<=0:
        return None
    return DeserializeCore(stream.split(','))

def DeserializeCore(sList):
    if len(sList)<=0:
        return None
    value=sList.pop(0)
    root=None
    if value!="$":
        root=TreeNode(int(value))
        root.left=DeserializeCore(sList)
        root.right=DeserializeCore(sList)
    return root

