# coding=UTF-8
file_object = open('planting.in', 'rb')
flag = 1
for line in file_object:
	if flag:
		N = int(line)
		flag = 0
		ppp =  [[] for i in range(N)]
	else:
		a, b= map(int, line.split())
		ppp[a - 1].append(b - 1)
		ppp[b - 1].append(a - 1)
maxnum = 0
for i in ppp:
	if len(i) > maxnum:
		maxnum = len(i)

file_object = open('planting.out', 'w')
file_object.write(str(maxnum + 1)+'\n')
file_object.close()
