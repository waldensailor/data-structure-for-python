# -*-coding:utf-8-*-
'__author__ = tyan'

"""
定义节点类：是不是为空，左节点，右节点
"""
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

"""
树类
生c成一颗完全二叉树
"""
class Tree(object):
    def __init__(self):
        self.root = Node()
        '''记录二叉树的中序序列，当一个子树的左右子树都添加时候，该节点会在该链表中删除'''
        self.myQuene = []
        
    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQuene.append(self.root)
        else:
            treeNode = self.myQuene[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQuene.append(treeNode.lchild)
            else：
                 treeNode.rchild == node
                 self.nyQuene.append(treeNode.rchild)
                 self.myQuene.pop(0) #如果存在右子树就将该节点丢弃
    
    '''
    '''