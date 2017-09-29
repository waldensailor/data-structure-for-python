#coding：utf-8

'''
定义节点
'''
class Node(object):
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = next
'''
定义单链表
'''        

class Link_list(object):
    '''初始化'''
    def __init__(self):
        self.length = 0
        self.next = None

    '''
    索取长度
    '''
    def length(self):
        return self.length
    '''判断是否为空'''    
    def is_empty(self):
        return self.next == None
    
    '''
    获取元素
    '''
    def get(self, i):
        if not isinstance(i, int):
            print("i值错误")
            return
        elif i < 1 or i > self.length:
            print("位置溢出")
            return
        else:
            current_node = self.next
            while i-1:
                current_node = current_node.next
                i -= 1
            return current_node
  
    '''添加元素'''
    def append(self, node):
        if isinstance(node, Node):
           pass
        else:
            node = Node(elem = node)
        if self.is_empty():
            self.next = node
        else:
            current_node = self.next
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
        
    '''
    删除元素
    注意next算0
    真实节点从1开始算
    '''
    def delete(self, index):
        if not isinstance(index, int):
            print("index is not right type")
            return
        if index > self.length or index < 1:
            print("index is out of range")
            return
        else: 
            if index == 1:
                #头部跟其他节点不同，故单独拿出来
                self.next = self.next.next
            else:                
                node = self.next
                while index-2:
                    node = node.next
                    index -= 1
                    
                #更改将前面节点的next属性指向下一个节点
                if node.next.next == None:
                    node.next = None
                else:
                    node.next = node.next.next
                self.length -= 1
                return

                
    '''
    打印链表
    '''
    def print_link(self):
        if self.next == None:
            print("there is no value")
            return
        node = self.next
        i = 1
        print("从1开始，这是第%d个值"%(i))
        print(node.elem)
        while node.next != None:
            node = node.next
            i += 1
            print("这是第%d个值"%(i))
            print(node.elem)

    '''
    插入元素
    '''
    def insert_value(self, i, node):
        if isinstance(node, Node):
           pass
        else:
            node = Node(elem = node)
        #索引检查    
        if not isinstance(i, int):
            print("i值错误")
            return
        elif i < 1 or i > self.length:
            print("位置溢出")
            return
        elif i == 1:
            node.next = self.next
            self.next = node
        else:                   
            site = 1
            current_node = self.next    
            while site != (i-1):
                site += 1
                current_node = current_node.next 
                print("搞不懂")
                print(current_node.next.elem)
            node.next = current_node.next
            current_node.next = node
          
        self.length += 1
        return
    '''
    入口校验
    '''            
    def destroy_link(self):
        self.next = None
        self.length = None
        return
   
    '''
    设置节点
    '''
    def set(self, i, value):
        current_node = self.next
        while i-1:
            i -= 1
            current_node = current_node.next
        current_node.elem = value

    '''
    反转链表
    '''
    def myreserve(self):
        if self.next == None or self.next.next == None:
            print("至少需要两个节点")
            return
        def reserve(pre_node, node):
            if pre_node == self.next:
                pre_node.next = None
            if node:
                if node.next:
                    current_node = node.next
                    node.next = pre_node
                    return reserve(node, current_node)
                else:
                    self.next = node
                    node.next = pre_node
        return reserve(self.next, self.next.next)

    '''
    别人的反转链表，确实简洁些呢
    '''
    def __reversed__(self):
        """
        1.pre-->next 转变为 next-->pre
        2.pre 若是next 则把 pre.nex --> None
        3.tail-->self.next
        :return:
        """
        def reverse(pre_node, node):
            if pre_node is self.next:
                pre_node.next = None
            if node:
                next_node = node.next
                node.next = pre_node
                return reverse(node, next_node)
            else:
                self.next = pre_node

        return reverse(self.next, self.next.next)
    
    
if __name__ == '__main__':
    a = [1, 2, 4, 4, 5, 'meizu', 'hello']
    link = Link_list()
 
    for i in a:
        link.append(i)

    #link.print_link()
    print("这个链表的长度", link.length)

    #link.delete(4) #删除测试
    #link.insert_value(5, "python") #插入测试
 
    link.set(3, "我是3") #设值测试
    
    
    '''
    测试自己和网上的反转函数
    '''
    link_one = Link_list()
    #link_one.append(2)
    #link_one.append(4)
    
    link.myreserve()#我写的函数
    #link_one.__reversed__()#网上的函数，当链表没有元素的时候会报错
    
    link.print_link()
    
    
    #长度测试
    #print(link.length)
    #for i in range(link.length):
    #    print("%d的值是"%(i), link.get(i).elem)
