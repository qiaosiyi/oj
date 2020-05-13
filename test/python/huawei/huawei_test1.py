# coding=UTF-8
# 给出两个日期，以及第一个日期对应的星期数，求第二个日期是星期几
# 输入 “1980 05 21 4|1980 05 22”
# 输出 “5”


yuefen = [31,28,31,30,31,30,31,31,30,31,30,31]#非闰年的月份天数

def run_nian(a):#定义函数：判断一个年份是否为闰年
  if (a%4==0 and a%100!=0) or (a%400==0):
    return 1
  return 0

def derta_day(a,b):#定义函数： date b - a 两个日期之间的间隔天数
  cha_nian = b[0] - a[0]
  cha_yue = b[1] - a[1]
  cha_ri = b[2] - a[2]

  day_nian = 0
  day_yue = 0
  day_ri = 0

  if cha_nian == 0:#由于年份引起的间隔天数
    pass
  else:
    for i in range(cha_nian):
      if run_nian(a[0]+i):
        day_nian += 366
      else:
        day_nian += 365
  
  if cha_yue == 0:#由于月份引起的间隔天数
    pass
  else:
    for i in range(cha_yue):
      day_yue += yuefen[i]
    if run_nian(b[0]) and cha_yue >=2:
      day_yue += 1
  
  day_ri = cha_ri#由于日期引起的间隔天数

  return day_nian+day_yue+day_ri

while True:
  try:
    data = raw_input()#获得输入数据
  except:
    exit()
  
  data = data.split('|')#分割输入数据

  data1 = data[0]
  data2 = data[1]

  data1 = data1.split()
  data2 = data2.split()#分割输入数据

  d0 = [int(data1[0]),1,1]
  d1 = [int(data1[0]),int(data1[1]),int(data1[2])]
  d2 = [int(data2[0]),int(data2[1]),int(data2[2])]
    

  xingqi = int(data1[-1])

  derta1 = derta_day(d0,d1)#得到第一个日期的绝对天数
  derta2 = derta_day(d0,d2)#得到第二个日期的绝对天数
  derta = derta2 - derta1#得到两个日期的相对天数
  xingqi_res = (derta+xingqi)%7 #判断相对天数对7的余数
  
  if xingqi_res == 0:
    print 7
  else:
    print xingqi_res
  
  