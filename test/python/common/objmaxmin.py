#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
class Stu:
    'base class of all students.'

    def __init__(self, name, code, score):
        self.name = name
        self.code = code
        self.score = score

    def prt(self):
        print self.name, self.code
    
n = int(input())
maxscore = []
minscore = []


for _ in range(n):
    a = sys.stdin.readline().strip('\n')
    a = a.split()
    print "new stu:", a
    obj = Stu(name = a[0], code = a[1], score = int(a[2]))
    if len(maxscore) == 0:
        maxscore.append(obj.score)
        minscore.append(obj.score)
        maxstu = obj
        minstu = obj
    else:
        if obj.score > maxscore[0]:
            maxscore[0] = obj.score
            maxstu = obj
        if obj.score < minscore[0]:
            minscore[0] = obj.score
            minstu = obj

maxstu.prt()
minstu.prt()


