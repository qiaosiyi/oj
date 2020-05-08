# coding=UTF-8
# 大小写字母的转换 输入大写转换为小写，输入小写转换为大写

while 1:
    indata = raw_input("input:")
    if 'a' <= indata <= 'z':
        outdata = chr(ord(indata ) + ord('A') - ord('a'))
        print "indata:",indata,"outdata:",outdata
    elif 'A' <= indata <= 'Z':
        outdata = chr(ord(indata ) - ord('A') + ord('a'))
        print "indata:",indata,"outdata:",outdata






