#!/usr/bin/python3
#-*-coding:utf-8-*-

__author__ = 'churentyan'

'''
队列模块
队列的创建和相关函数
'''
class Queue(object):
    def __init__(self, max=20):
        self.data = []
        self.max = max
    
    #入队函数
    def add(self, elem):
        if self.max == len(self.data):
            print("队列已经满了！！！")
        else:
            self.data.append(elem)
    
    #出队函数
    def delete(self):
        #不为空则第一个出队
        if self.data:
            self.data.pop[0]
        else:
            print("队列为空哦！！！")
        
    #清空队列
    def delete(self):
        self.data = []
    
    #判断队列是否为空
    def isempty(self):
        return 0 == len(self.data)
    
    #判断队列是否满
    def isFull(self):
        return self.max == len(self.data)
        
    #队列长度
    def length(self):
        return len(self.data)
        
        
if __name__ == '__main__':
    team = ('thunder', 'heat', 'GS', 'hoston', '76', 'cavs')
    jhs_team = Queue()
    for a in team:
        jhs_team.add(a)
    jhs_team.add("76er")
    #输出
    print("all team count is :", jhs_team.length())
    print("球队有没有完全出来", jhs_team.isFull())
    
        