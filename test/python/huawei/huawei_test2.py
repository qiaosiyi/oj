# coding=UTF-8
# 第一行表示公交站位置序号，第二行表示路灯位置，求最小亮度。

def is_fu_gai(lu_deng,gong_jiao_zhan,liang_du):
  fu_gai = {}

  for i in lu_deng:
    fu_gai[i] = 1
    for j in range(liang_du):
      fu_gai[i-j-1] = 1
      fu_gai[i+j+1] = 1
  # print fu_gai
  
  for i in gong_jiao_zhan:
    if i in fu_gai:
      pass
    else:
      return 0
  
  return 1


while True:
  try:
    gong_jiao_zhan = raw_input()
    lu_deng = raw_input()
  except:
    exit()
  
  gong_jiao_zhan = gong_jiao_zhan.split(',')
  lu_deng = lu_deng.split(',')
  gong_jiao_zhan.sort()


  gjz = []
  ld = []
  for i in gong_jiao_zhan:
    gjz.append(int(i))
  for i in lu_deng:
    ld.append(int(i))
  liang_du = 0

  # print gjz
  # print ld


  for i in range(2000):
    if is_fu_gai(ld,gjz,liang_du):
      print liang_du
      break
    liang_du += 1

