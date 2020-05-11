# coding=UTF-8
# 连续输入字符串，请按长度为8拆分每个字符串后,输出到新的字符串数组.
# 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
def fen_ge(st):
  n = len(st)
  res = ""
  tmp = ""
  i = 0

  if n == 0:
    return res
  
  while n > 0:
    if n <= 8:
      num0 = (8-n) * "0"
      tmp = st[i*8:]
      res = res + tmp + num0
      return res
    else:
      tmp = st[i*8:i*8+8]
      res = res +tmp + "\n"
    i += 1
    n -= 8
      
      



while True:
  try:
    n0 = raw_input()
    n1 = raw_input()
  except:
    exit()
  
  print fen_ge(n0)
  print fen_ge(n1)
  



