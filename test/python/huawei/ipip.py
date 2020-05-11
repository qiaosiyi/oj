# coding=UTF-8
# 0：IP1与IP2属于同一子网络；     
# 1：IP地址或子网掩码格式非法；    
# 2：IP1与IP2不属于同一子网络

def ipvalid(ip):
  nums = ip.split('.')
  for i in nums:
    i = int(i)
    if i<0 or i >255:
      return 0
  return 1

def ip2bin(ip):
  nums = ip.split('.')
  # print nums
  bin = 0
  j = 3
  for i in nums:
    i = int(i)
    i = i & 0xff
    # print i
    i = i << j*8
    bin |= i
    j -= 1
  return bin


while True:
  try:
    n = raw_input()
  except:
    exit()
  
  ipstrings = n.split()
  bins = []
  res = 0
  for i in ipstrings:
    if ipvalid(i):
      pass
    else:
      res = 1
      # print "res1"
  
  for i in ipstrings:
    bins.append(ip2bin(i))
  if bins[0]&bins[1] == bins[0]&bins[2]:
    res2 = 0
  else:
    res2 = 2
    
  if res:
    print res
  else:
    print res2
  
  
  