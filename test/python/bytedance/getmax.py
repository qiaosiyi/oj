# coding=UTF-8
# 给出一个数组 A，找到最大的 A[i] - A[j]，要求 i > j。

a = [1,4,2,5,7,3,7,8]


minn = a[0]
n = len(a)
res = a[1] - a[0]
for i in range(n-1):
    minn = min(minn,a[i+1])
    res = max(res, a[i+1]-minn)
print res
