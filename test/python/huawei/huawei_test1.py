yuefen = [31,28,31,30,31,30,31,31,30,31,30,31]
def run_nian(a):
  if (a%4==0 and a%100!=0) or (a%400==0):
    return 1
  return 0

def derta_day(a,b):# date b - a
  cha_nian = b[0] - a[0]
  cha_yue = b[1] - a[1]
  cha_ri = b[2] - a[2]

  day_nian = 0
  day_yue = 0
  day_ri = 0

  if cha_nian == 0:
    pass
  else:
    for i in range(cha_nian):
      if run_nian(a[0]+i):
        day_nian += 366
      else:
        day_nian += 365
  
  if cha_yue == 0:
    pass
  else:
    for i in range(cha_yue):
      day_yue += yuefen[i]
    if run_nian(b[0]) and cha_yue >=2:
      day_yue += 1
  
  day_ri = cha_ri

  return day_nian+day_yue+day_ri


while True:
  try:
    data = raw_input()
  except:
    exit()
  
  data = data.split('|')

  data1 = data[0]
  data2 = data[1]

  data1 = data1.split()
  data2 = data2.split()

  d0 = [int(data1[0]),1,1]
  d1 = [int(data1[0]),int(data1[1]),int(data1[2])]
  d2 = [int(data2[0]),int(data2[1]),int(data2[2])]
    

  xingqi = int(data1[-1])

  derta1 = derta_day(d0,d1)
  # print derta1
  derta2 = derta_day(d0,d2)
  # print derta2
  derta = derta2 - derta1
  xingqi_res = (derta+xingqi)%7
  
  if xingqi_res == 0:
    print 7
  else:
    print xingqi_res
  
  