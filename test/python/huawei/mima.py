# coding=UTF-8
# 他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
# 就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
# 声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，
# 如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。

ind = {
'a':2, 'b':2, 'c':2, \
'd':3, 'e':3, 'f':3, \
'g':4, 'h':4, 'i':4, \
'j':5, 'k':5, 'l':5, \
'm':6, 'n':6, 'o':6, \
'p':7, 'q':7, 'r':7, 's':7, \
't':8, 'u':8, 'v':8, \
'w':9, 'x':9, 'y':9, 'z':9\
}

def da2xiao(d):
  x = ord(d) + 32
  chr_xiao = chr(x)
  if chr_xiao == 'z':
    return 'a'
  else:
    return chr(x+1)

def xiao2num(x):
  return str(ind[x])




while True:
  try:
    n0 = raw_input()
  except:
    exit()
  
  res = ""
  for i in n0:
    if 'a' <= i <= 'z':
      res += xiao2num(i)
    elif 'A' <= i <= 'Z':
      res += da2xiao(i)
    else:
      res += i
  print res