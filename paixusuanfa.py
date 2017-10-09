#!/usr/bin/python3
#coding:utf-8
'''
稳定的算法：一个序列中两个相同的值在排序前后不会发生相对位置变化
稳定的算法包括：冒泡排序，插入排序， 归并排序， 基数排序
不稳定的算法有：快速排序， 希尔排序， 选择排序， 堆排序

我举得把，写程序都应该从外写到内，发现哪缺东西再回去补上就好
'''
lista = list(range(13))
lista.reverse()
lista.append(8)
lista.append(6)
print(lista)

#---1----选择排序
#不稳定算法
#时间复杂度O（n^2）
def selectSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):#i从0开始所以多减去一个哦
            if list[i] > list[i+j+1]:
                list[i], list[i+j+1] = list[i+j+1], list[i]
                
#冒泡排序
#时间复杂度O（n^2）：这么写的情况下，无论如何时间复杂度都是O(n^2)
def maoPao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],  list[j]
    return list 

#---2----改进的冒泡排序：最好情况复杂度为O(n)
def newMaoPao(list):
    for i in range(len(list)-1):
        didswap = False#记录是否做过交换
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],  list[j]
                didswap = True
        if didswap == False:#如果没有做过交换则此次遍历的部分全是正常排序的
            return list
    return list     
    

#---3----插入排序
def insertSort(list):
    for i in range(len(list)-1):
        index = list[i+1]
        for j in range(i+1):
            '''
            if index < list[j]:
                list.insert(j, index)            
                list.pop(i+2)#其实这儿是不正确的，应该用元素交换
                break#忘记了break找错误找了半天，都是泪啊
            '''
            if index < list[i-j]:
                list[i-j], list[i-j+1] = list[i-j+1], list[i-j]
            
    return list            

#@来源于网上：改进版的插入排序,第二次遍历类似于冒泡
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
    
#---4----希尔排序：升级版的插入排序
def shellSort(list):
    count = len(list)
    group = count // 2#第一次的梯度，也是组数
    while group > 0:#对每次的重新分组循环
        for i in range(0, group):#对每组进行遍历
            j = group + i
            while j < count:#从这层开始才是一个真的插入排序，递增是group,
                m = j - group
                while m >=0:
                    if list[m] > list[m+group]:
                        list[m], list[m+group] = list[m+group], list[m]
                    m -= group
                j += group   
        group //= 2
    return list


#@来源于网上快速排序
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, right - 1)
    quick_sort(lists, right + 1, high)
    return lists
    
#---5----快速排序 ：自己写的  
def quickSort(list, left, right):
    if right <= left:
        return list
    key = list[left]
    low = left#记住此时的最左和最右，方便递归调用
    high = right
    while left < right:
        while left < right and list[right] > key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] < key:
            left += 1
        list[right] = list[left]
        print("yijiaohuan")
    list[right] = key
    quickSort(list, low, right -1)#这儿的left和right值是相等的，用谁都可以
    quickSort(list, right+1, high)
    return list

    
lista = shellSort(lista)
print(lista)