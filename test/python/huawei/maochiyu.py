# coding=UTF-8
# 
# 
n = input()
price = []
freight_fee = []

for i in range(n):
  tmp = raw_input()
  tmp = tmp.split()
  price.append(tmp[0])
  freight_fee.append(tmp[1])

minn = 999999
cost = 0

for i in range(n):
  if minn > price[i]:
    minn = price[i]
  
  cost += minn           #
  minn += freight_fee[i] #

print cost





