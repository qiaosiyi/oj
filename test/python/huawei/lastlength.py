# coding=UTF-8
# 计算字符串最后一个单词的长度，单词以空格隔开。
while True:
    try:
        indata = raw_input()
    except:
        exit()
    a = indata.split()
    b = a[-1]
    print len(b)