# coding=UTF-8
#二分查找元素在有序数组中的位置，如果不存在，输出-1，
# 如果存在，输出下标（存在多个，输出下标最小的）。

lista = [1,6,6,7,8,9]
val = 6

def getpos(arr, val):
    n = len(arr)
    h = n - 1
    l = 0
    p = (l+h)/2
    while(h>l):
        if val < arr[p]:
            h = p
            p = (l+h)/2
            continue
        if val > arr[p]:
            l = p
            p = (l+h)/2
            continue
        if val == arr[p]:
            if val == arr[p-1]:
                p = p-1
                h = p
            else :
                # return p
                print "p =",p
                return 0

getpos(lista,val)
#  print "p = ", p