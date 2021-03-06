# coding=UTF-8
# 第一行表示公交站位置序号，第二行表示路灯位置，求最小亮度。
# 1,3,4,2
# 3
# 2 output

def is_fu_gai(lu_deng,gong_jiao_zhan,liang_du): #当亮度为x时，是否满足要求
  fu_gai = {}#被覆盖的点集合

  for i in lu_deng:#进行覆盖计算
    fu_gai[i] = 1
    for j in range(liang_du):
      fu_gai[i-j-1] = 1
      fu_gai[i+j+1] = 1
  # print fu_gai
  
  for i in gong_jiao_zhan:#检查是否所有公交站都在覆盖点集内
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

  for i in range(2000):#从亮度为0开始测试，一旦成功则跳出，并输出结果
    if is_fu_gai(ld,gjz,liang_du):
      print liang_du
      break
    liang_du += 1

