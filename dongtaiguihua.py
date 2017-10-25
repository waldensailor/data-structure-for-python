#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
动态规划找零问题：
已知币种：values
求凑齐money的最小数量：
想法不一致的地方：
用一个list记住要求的money以下的所有最小数，减少了运算次数
用另一个list记住money最小个数的当前面值币种
'''

#找零问题的最小个数
def searchMin(values, money, num_list, coin_now):
    for m in range(1, money+1):
        for cin in values:#遍历每一种货币
            if cin <= m:#
                if num_list[m-cin] + 1 < num_list[m]:
                    num_list[m] = num_list[m-cin] + 1
                    coin_now[m] = cin
            else:
                break
    return num_list[money]
    
#输出找零的数列
def outlist(money, coin_list):
    list = []
    #money为0的时候推出循环
    while money:
        list.append(coin_list[money])
        money -= coin_list[money]
    list.sort()#排序
    return list

#主函数
def main():
    values = [1,5,10,21,25]#从小到大排序
    money = 89
    #方便记录money小的每个钱的找零情况，方便后面直接取出来使用
    num_list = list(range(money+1))#会的到一个1， 2， 3……money+1的列表,当然因为默认最小单位有1存在
    #记录最小数目时，这儿对应的货币面额
    coin_now = list(range(money+1))
    print(searchMin(values, money, num_list, coin_now))
    print(outlist(money, coin_now))
if __name__ == '__main__':
    main()

    

