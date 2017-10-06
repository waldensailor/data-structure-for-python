#!/usr/bin/python3
#-*- coding:utf-8 -*-

'''
搜索二叉树的是吸纳
'''

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.lchrild = None
        self.rchrild = None

class TreeSearch(object):
    def __init__(self):
        self.root = None
        
    #中序遍历二叉树
    def bianli(self, node="root"):
        #因为当参数列表（self, self.root）报错参数列表中不能相互引用
        if node == "root":
            node = self.root
        if not node:
            #print("该搜索二叉树为空")
            return
        
        '''要用self调用'''
        self.bianli(node.lchrild)
        print(node.elem)
        self.bianli(node.rchrild)
    
    #添加节点，非递归方法
    def append(self, elem):
        if not self.root:
            self.root = Node(elem)
            return
        #判断节点
        node = self.root
        #记录上一个节点
        par_node = self.root
        #记录是左子树上的还是右子树
        chrild = 0
        while node:
            par_node = node
            if elem < node.elem:
                node = node.lchrild
                chrild = 0
            else:
                node = node.rchrild
                chrild = 1
        if chrild:
            par_node.rchrild = Node(elem)
        else:
            par_node.lchrild = Node(elem)
        #print("插入成功", node.elem)   
    
    #插入节点，递归方法
    def append_digu(self, elem, root = None):
        #检查根节点是否存在
        if not self.root:
            self.root = Node(elem)
            return
        '''
        root是递归传入的值，但是每次插入的第一次调用不会有值传入
        此时的值就应该是根节点
        '''
        current_node = root
        if not root:
            current_node = self.root
            
        #与当前节点判断
        if elem < current_node.elem:  
            #如果存在左子树
            if current_node.lchrild:
                current_node = current_node.lchrild             
                self.append_digu(elem, current_node)
            #不存在则直接插入
            else:
                current_node.lchrild = Node(elem)
               
        else:
            if current_node.rchrild:
                current_node = current_node.rchrild
                self.append_digu(elem, current_node)
            else:
                current_node.rchrild = Node(elem)
            
    #删除节点
    def delete(elem):
        pass
        
    #
if __name__ == '__main__':
    sdtree = TreeSearch()
    list = [3, 5, 12, 54, 2, 1, 54, 678, 2, 54]
    team = ['thunder', 'gs', 'rockets', 'suprs', 'lakers', '快船', 'rop']
    for i in list:
        sdtree.append_digu(i)
    sdtree.bianli()