# coding=UTF-8
# 输入一个算术表达式 3+2*{1+2*[-4/(8-6)+7]}

while True:
  try:
    data = raw_input()
  except:
    exit()
  
  
  data = data.replace("{","(")
  data = data.replace("}",")")
  data = data.replace("[","(")
  data = data.replace("]",")")
  a = eval(data)
  print a