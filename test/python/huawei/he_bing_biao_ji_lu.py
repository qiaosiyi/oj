# coding=UTF-8
# 数据表记录包含表索引和数值（int范围的整数），
# 请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，
# 输出按照key值升序进行输出。

def b_key(a):
  return a[0]

while True:
  try:
    n = input()
    datain = []
    for i in range(n):
      d = raw_input()
      d = d.split()
      e = [int(d[0]), int(d[1])]
      datain.append(e)

  except:
    exit()
  
  a = sorted(datain, key=b_key)
  
  res = []
  n = len(a)
  res.append(a[0])
  for i in range(n-1):
    if res[-1][0] == a[i+1][0]:
      res[-1][1] += a[i+1][1]
    else:
      res.append(a[i+1])

  for i in res:
    print i[0],i[1]
  
  
  



