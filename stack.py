#!/usr/bin/python3
#-*— coding:utf -8-*-

__author__ = 'churentyan'

'''
栈模块
栈的构建，与基本方法
'''


class Stack(object):
    def __init__(self, max=10):
        self.data = [] #储存
        self.max = max #栈的大小

    #压栈
    def push(self, elem):
        if len(self.data)< self.max:
            self.data.append(elem)
            print("插入成功")
        else:
            print("栈溢出,插入未成功")
    
    #出栈
    def pop(self):
        if len(self.data)< 1:
            print("栈为空")
        else:
            return self.data.pop()
            
    #返回栈的大小
    def size(self):
        return len(self.data)
        
    #返回栈顶元素
    def peek(self):
        if self.isempty():
            print("空栈")
        else:
            return self.data[len(self.data)-1]
            
    #判断栈是否为空
    def isempty(self):
        return len(self.data) == 0
        
    def print_stack(self):
        for i in range(self.size()):
            print("这是第%d个元素"%i)
            print(self.data[i])
        
        
'''
测试函数
'''
if __name__ == '__main__':
    stack = Stack()
    list_a = ('rusell', 'lbj', 'hello', 'one', 'thunder', 'rocket', 'gs', 'sups')
    for i in list_a:
        stack.push(i)
    
    print(stack.isempty())
    print("最后一个元素是", stack.peek())
    print(stack.pop())
    stack.print_stack()
            