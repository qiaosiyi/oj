# coding=UTF-8
# 使用 高阶函数 sorted 对list进行排序

a = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#对分数进行排序
def by_s(a):
    return -a[1]

#对名字进行排序
def by_n(a):
    return a[0].lower()

b = sorted(a,key=by_s)
print b

c = sorted(a,key=by_n)
print c