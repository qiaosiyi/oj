# 10个小球，随机分到12个盒子里，求恰好10个盒子都为空的概率。要求用Python程序模拟十万次，暴力求出该概率。

import random
def GetRdNum():
    rd1 = random.random()
    rd12 = int(rd1*12)
    return rd12

def GetT1():
    dict = {}
    for i in range(10):
        a = GetRdNum()
        dict[a] = 1
        if len(dict) > 2: #2-9
            return 0
    if len(dict) == 1:
        return 0 #11
    return 1 #10

P = 0
NumT = 10000000
for i in range(NumT):
    if(GetT1() == 1):
        P = P + 1

pp = P*1.0 / NumT

print "P=",pp