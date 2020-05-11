# coding=UTF-8
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
# 如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

while True:
  try:
    n = raw_input()
  except:
    exit()
  
  zhengshu = ""
  j = 0
  for i in n:
    j += 1
    if i != '.':
      zhengshu += i
    else:
      xiaoshu = n[j]
      break
  
  res = int(zhengshu)
  if xiaoshu >= '5':
    print res + 1
  else:
    print res
  
  

  