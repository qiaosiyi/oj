# coding=UTF-8
# 租书屋的老板打算进一批书，
# 选出n本价格相同的书作为备选
# 给VIP读者发了一批调查问卷，收集到想看列表
# 为节约money，老板保证vip至少有一本喜欢的书
# 最小化费用，书和读者从0开始编号，
# 整理出读者想看书列表为b，输出最少采购数量。
# 第一行书本数
# 第二行读者数
# 第三行开始读者想看书列表
# 每行至少包含1本书的id

def is_manzu(shu,ren,index,res):


while True:
  try:
    shu = input()
    ren = input()
    index = []
    for i in shu:
      index.append([])
    for i in range(ren):
      data = raw_input()
      data = data.split()
      tmp = []
      for i in data:
        tmp.append(int(i))
      for i in tmp:
        index[tmp].append(i)
  except:
    exit()
  
  res = 1
