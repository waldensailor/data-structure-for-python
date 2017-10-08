#!/usr/bin/python3
#coding:utf-8

lista = list(range(13))
lista.reverse()
print(lista)

#选择排序
#时间复杂度O（n^2）
def selectSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):#i从0开始所以多减去一个哦
            if list[i] > list[i+j+1]:
                list[i], list[i+j+1] = list[i+j+1], list[i]
                
#冒泡排序
#时间复杂度O（n^2）
def maoPao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],  list[j]
    return list 
    
#插入排序
def insertSort(list):
    for i in range(len(list)-1):
        index = list[i+1]
        for j in range(i+1):
            if index < list[j]:
                list.insert(j, index)            
                list.pop(i+2)
                break#忘记了break找错误找了半天，都是泪啊
    return list            
#改进版的插入排序,第二次遍历类似于冒泡
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
    
#希尔排序
def shellSort(list):
    count = len(list)
    step = 2
    group = count / step
    while group > 0:#组的个数
        for i in range(0, group):#对每组进行遍历
            while j < count:
                pass
            
        group /= step
        return list
#selectSort(lista)

#快速排序
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


lista = quick_sort(lista, 0, len(lista)-1)
print(lista)