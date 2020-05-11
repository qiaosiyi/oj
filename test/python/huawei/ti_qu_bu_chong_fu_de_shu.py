# coding=UTF-8
# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

while True:
  try:
    n = raw_input()
  except:
    exit()
  
  if n[0] == '-':
    n = n[1:]
  
  a = {}
  l = len(n)
  res = ""
  for i in range(l):
    if n[l-i-1] not in a:
      res += n[l-i-1]
      a[n[l-i-1]] = 1
  print res