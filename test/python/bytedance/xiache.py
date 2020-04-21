# coding=UTF-8
#一辆巴士载了25人，路经10个车站。
# 每个乘客以相同的概率在各个车站下车。
# 如果某个车站有乘客要下车，则大巴在该站停车。
# 每个乘客下车的行为是独立的。记大巴停车次数为X，
# 求X的数学期望（要求通过编程求数学期望）。
import random

numpeople = 25
numstation = 10
pxiache = 1.0 / 10

testnum = 10000

def xiache():
    a = random.random()
    if a < pxiache:
        return 1 #want to xiache
    return 0



def stop(people_left):
    xiachenum = 0
    if people_left == 0:
        return 0 #no need to stop
    for i in range(people_left):
        xiachenum = xiachenum + xiache()
    if xiachenum == 0:
        return 0 #no one want to get off
    else:
        return xiachenum #stop and some num of pp get off

numofstop = 0
for i in range(testnum):
    numpeopleleft = numpeople
    for i in range(numstation):
        a = stop(numpeopleleft)
        numpeopleleft -= a
        if a > 0:
            numofstop += 1
        if numpeopleleft == 0:
            break #there is no passenger on bus

print "E(X) =",numofstop*1.0/testnum

