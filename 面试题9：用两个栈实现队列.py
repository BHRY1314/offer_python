#!/usr/bin/env python
# coding: utf-8

# #  面试题9：用两个栈实现队列
# 
# ### 用两个栈实现一个队列，请实现它的两个函数appendTail和deleteHead,分别完成在队列尾部插入节点和队列头部删除节点的功能
# 

# In[ ]:


'''
思路：
利用两个栈，把数据压入一个栈中，然后逐个弹出压入第二个栈，然后从第二个栈中弹出。
删除一个元素的步骤：当stack2不为空时，在stack2中的栈顶元素是最先进入队列的元素，可以弹
出。当stack2为空时，我们把stack1中的元素逐个弹出并压入stack2.由于先进入队列的元素被压
到Stack1的底端，经过弹出和压入操作后就处于stack2的顶端，又可以直接弹出
'''

def __init__(self):
    self.stack1=[]
    self.stack2=[]

def push(self,node):
    self.stack1.push(node)
    
def pop(self):
    if self.stack2=[]:
        while self.stack1:
            data=self.stack1.pop()
            self.stack2.append(data)
            return self.stack2.pop()
    return self.stack2.pop()

