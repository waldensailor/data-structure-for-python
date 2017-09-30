#coding:utf-8

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None

class LinkDouble(object):
    def __init__(self):
        self.head = None

                
    #求双链表的长度
    def length(self):
        len = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            len += 1
        return len
   
   #求链表是否为空
    def isempty(self):
        return self.length() == 0
    
    #添加元素
    def add(self, node):
        #对象化传值
        node = self.__node(node)
        if self.isempty():
            self.head = node
            #第一个元素怎么链接头部
            self.head = node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            node.pre = current_node
    
    #打印链表
    def print_doublelink(self):       
        if self.isempty():
            print("链表为空")
        else:
            i = 0
            current_node = self.head
            while current_node:
                print("第%d个元素"%i)
                print(current_node.data)
                current_node = current_node.next
                i += 1
   
   #插入元素
    def insert(self, i, value):
        if not self.__check(i):
            print("插入元素失败")
            return
        node = self.__node(value)
        if 0 == i:
            current_next = self.head
            current_next.pre = node
            node.next = current_next
            self.head = node
        else:
            current_node = self.head
            site = 0
            while site < (i-1):
                current_node = current_node.next
                site += 1
            #print("前一个值是：", current)    
            current_next = current_node.next
            current_node.next = node
            node.next = current_next
            current_next.pre = node
            node.pre = current_node
             
    #删除节点
    def delete(self, i):
        if not self.__check(i):
            print("亲确认节点是否正确")
            return
            
        current_node = self.head
        if self.length() == 1:
            self.head = None
        elif i == 0:
            next = current_node.next
            self.head = next
            next.pre = None
        elif i == self.length()-1:
            while current_node.next.next:
                current_node = current_node.next
            #被抛弃的节点是否取消指向
            current_node.next.pre = None
            current_node.next = None            
        else:
            site = 0
            while site < i-1:
                current_node = current_node.next
                site += 1
            next = current_node.next.next
            next.pre = current_node
            current_node.next = next
        
    #返回节点的值
    def getvalue(self, i):
        if not self.__check(i):
            return
        current_node = self.head
        while i:
            current_node = current_node.next
            i = i-1
        return current_node.data
    
    #修改节点的值
    def update(self, i, value):
        if not self.__check(i):
            return
        current_node = self.head
        while i:
            current_node = current_node.next
            i = i-1
        current_node.data = value
        print("结点值已经更改")
    
    #返回第一次出现该元素的位置
    def getsite(self, data):
        if self.length() == 0:
            print("链表为空")
            return -1
        else:
            current_node = self.head
            site = 0
            while current_node:
                if current_node.data == data:
                    return site
                site += 1
                current_node = current_node.next
            return -1        

    #检查传入的坐标是否合法
    def __check(self, i):
        if not isinstance(i, int):
            print("输入的i不是一个int数据")
            return 0
        if i > (self.length()-1) or i < 0:
            print("请确认i的范围")
            return 0
        return 1
 
    #将传入的值对象化
    def __node(self, elem):
        if isinstance(elem, Node):
            return elem
        else:
            return Node(elem)

'''
测试数据
'''
if __name__ == "__main__":
    linkdoubla_a = LinkDouble()
    list_link = [1, 3, 'python', 'java', 'ruby', 'js']
    for i in list_link:
        linkdoubla_a.add(i)
    linkdoubla_a.print_doublelink()
    print("链表的长度是", linkdoubla_a.length())
    
    #插入节点
    #linkdoubla_a.insert(4, "我是插入的haha")
    
    '''
    #删除某个节点
    linkdoubla_a.delete(0)    
    linkdoubla_a.print_doublelink()
    print("链表的长度是", linkdoubla_a.length())

    
    
    #取节点的值
    num = 2
    print("第%d个结点的值是"%num)
    print(linkdoubla_a.getvalue(num))
    
    linkdoubla_a.update(3, "hello world")
    linkdoubla_a.print_doublelink()
    '''
    
    #校验获取第一次出席那data的位置
    value = 'jsf'
    print(value, "出现的位置是")
    print(linkdoubla_a.getsite(value))
        