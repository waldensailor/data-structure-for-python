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
    def delete(self, elem):
        pass
        
    #层次遍历
    def leave(self):
        que = []
        #如果是空树，则跳出
        if self.root:
            que.append(self.root)
        else:
            print("此树为空")
            return
        while que:
            if que[0].lchrild:
                que.append(que[0].lchrild)
            if que[0].rchrild:
                que.append(que[0].rchrild)
            print(que[0].elem)
            del que[0]
            
     #按照每层打印的层次遍历
    def print_leave(self):
        que = []     
        hh = []#换行记发的list
        #如果是空树，则跳出
        if self.root:
            que.append(self.root)
            dq_num = 1
            xiacen_num = 0
        else:
            print("此树为空")
            return
        while que:
            if que[0].lchrild:
                que.append(que[0].lchrild)
                xiacen_num += 1
            if que[0].rchrild:
                que.append(que[0].rchrild)
                xiacen_num += 1    
            print(que[0].elem, end=" ")
            dq_num -= 1
            if dq_num == 0:
                dq_num = xiacen_num
                xiacen_num = 0
                print()
            del que[0]
            
    #递归层次遍历
    def digu_leave(self):
        que = []
        if self.root:
            que.append(self.root)
        else:
            print("此树为空")
            return
        def di_leave(que):
            print(que[0].elem)
            if que[0].lchrild:
                que.append(que[0].lchrild)
            if que[0].rchrild:
                que.append(que[0].rchrild)
            que.pop(0)
            if que:#如果队列为不为空则递归           
                di_leave(que)
        di_leave(que)
        
if __name__ == '__main__':
    sdtree = TreeSearch()
    list = [9, 3, 7, 28,6, 5, 12, 54, 2, 1, 54, 678, 2, 54]
    team = ['thunder', 'gs', 'rockets', 'suprs', 'lakers', '快船', 'rop']
    for i in list:
        sdtree.append_digu(i)
    sdtree.leave()
    #sdtree.digu_leave()
    print("按照层遍历，按照行输出")
    sdtree.print_leave()