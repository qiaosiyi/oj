# coding=UTF-8
def if_cover(a,b):
	if a[0] < b[0] and b[1] < a[1]:
		return 1
	if a[0] > b[0] and b[1] > a[1]:
		return 1
	return 0

file_object = open('mountains.in', 'rb')
flag = 1
for line in file_object:
	if flag:
		N = int(line)
		flag = 0
		ppp =  [[] for i in range(N)]
		j = 0
	else:
		x, y= map(int, line.split())
		ppp[j].append(x - y)
		ppp[j].append(x + y)
		j = j + 1
maxnum = N
for i in range(N):
	for j in range(N):
		if i < j:
			maxnum = maxnum - if_cover(ppp[i], ppp[j])

file_object = open('mountains.out', 'w')
file_object.write(str(maxnum )+'\n')
file_object.close()
