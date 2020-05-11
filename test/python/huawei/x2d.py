# coding=UTF-8
# 写出一个程序，接受一个十六进制的数，
# 输出该数值的十进制表示。（多组同时输入 ）

s2n={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,\
  '6':6,'7':7,'8':8,'9':9,'A':10,\
  'B':11,'C':12,'D':13,'E':14,'F':15}

while True:
  try:
    n0 = raw_input()
  except:
    exit()

  numhex = n0[2:]
  n = len(numhex)
  e = 1
  num10 = 0
  for i in range(n):
    num10 += s2n[numhex[n-i-1]]*e
    e *= 16
  print num10
