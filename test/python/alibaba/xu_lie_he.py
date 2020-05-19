# coding=UTF-8
# 输入N, L
# N表示和，L 表示非零连续自然数序列长度，如果长度大于等于L的序列之和恰好等于N，则返回此序列中最短的一组，
# 若L大于一百或无次序列，则返回No。
# 3
# 2 output

def find(N,L):
  l = L
  while 1:
    zh_ch = (N-(l*l + l)/2)%l
    n = (N-(l*l + l)/2)/l + 1
    an = (l*l+l)/2+(n -1)*l
    if an > N or l > 100:
      return -1,-1
    if zh_ch == 0:
      return n,l
    l += 1

while True:
  try:
    data = raw_input()
    data = data.split()
    datain = []
    for i in data:
      datain.append(int(i))
    # print datain
  except:
    exit()
  
  N = datain[0]
  L = datain[1]
  res = ""

  an,l = find(N,L)
  if an == -1:
    print "No"
  else:
    for i in range(l):
      tmp = an + i
      res += str(tmp)
      res += " "
    print res[:-1]
  



