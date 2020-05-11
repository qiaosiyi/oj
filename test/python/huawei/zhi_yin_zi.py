# coding=UTF-8
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）
#（如180的质因子为2 2 3 3 5 ) 最后一个数后面也要有空格

def zheng_chu(beichushu,chushu):
  if beichushu % chushu == 0:
    return 1
  else:
    return 0

while True:
  try:
    n = raw_input()
    n = int(n)
  except:
    exit()
  res = []

  for i in range(n):
    chushu = i + 2
    if chushu > n:
      break
    while zheng_chu(n,chushu):
      n /= chushu
      res.append(chushu)
  
  for i in res:
    print i,
  print ""
    

