# coding=UTF-8
# 写出一个程序，接受一个由字母和数字组成的字符串，
# 和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

def issame(a,w):# if these two char equo
    
    if ord('A')<=ord(w)<=ord('Z'):
        w1,w2 = ord(w) , ord(w) + 32
        if w1 == ord(a) or w2 == ord(a):
            return 1
        else:
            return 0

    if ord('a')<=ord(w)<=ord('a'):
        w1,w2 = ord(w) , ord(w) - 32
        if w1 == ord(a) or w2 == ord(a):
            return 1
        else:
            return 0
    if w == a:
        return 1
    else:
        return 0
    

summ = 0

while True:
    try:
        indata = raw_input()
        w = raw_input()
    except:
        exit()
    for i in indata:
        if issame(i,w):
            summ += 1
    print summ
    summ = 0
    
