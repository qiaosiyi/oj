#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
class Stu:
    'base class of all students.'

    def __init__(self, name, cn, math, eng):
        self.name = name
        self.cn = int(cn)
        self.math = int(math)
        self.eng = int(eng)
        self.total = self.cn + self.math + self.eng
        if self.cn >= 60 and self.math >= 60 and self.eng >= 60:
            self.passd = 1
        else:
            self.passd = 0
    def __gt__(self, other):
        if self.total > other.total:
            return 1
        elif self.total < other.total:
            return 0
        else:
            if self.cn > other.cn:
                return 1
            elif self.cn < other.cn:
                return 0
            else:
                if self.math > other.math:
                    return 1
                elif self.math < other.math:
                    return 0
                else:
                    if self.eng > other.eng:
                        return 1
                    elif self.eng < other.eng:
                        return 0
                    else:
                        if self.name < other.name:
                            return 1
    def __str__(self):
        return "%s %d %d %d" % (self.name, self.cn, self.math, self.eng)
    def pt(self):
        print self.name, self.cn, self.math, self.eng

def sort_stu(stu):
    n = len(stu)
    for j in range(n):
        for i in range(n - 1):
            if stu[i+1] > stu[i]:
                stu[i+1], stu[i] = stu[i], stu[i+1]

stu=[]

for i in range(10):
    line = sys.stdin.readline().strip()
    line = line.split()

    stu.append(Stu(line[0], line[1], line[2], line[3]))

sort_stu(stu)
print "[first round name list]"
for i in stu:
    i.pt()
stu2nd = []
for i in stu:
    if i.passd:
        stu2nd.append(i)

print
print "[final round name list]"
a = stu2nd[0].total
b = 1
for i in stu2nd:
    if i.total != a:
        b = b + 1
        a = i.total
    if b < 4:
        i.pt()
    
