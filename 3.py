file_object = open('guess.in', 'rb')
flag = 1
for line in file_object:
	if flag:
		N = int(line)
		listtotal = {}
		maxnum = 0
		anm =  [[] for i in range(N)]
		flag = 0
		i = 0
	else:
		tempinput = map(str, line.split())
		cc = int(tempinput[1])
		for j in range(cc):
			anm[i].append(tempinput[j+2])
			if listtotal.has_key(tempinput[j+2]) == 1: 
				listtotal.update({tempinput[j+2]:2})
			else:
				listtotal.update({tempinput[j+2]:1})							
		i = i + 1
for i in range(N):
	tempsum = 0
	for j in range(len(anm[i])):
		if listtotal[anm[i][j]] == 2:
			tempsum = tempsum + 1
	if tempsum < len(anm[i]):
		tempsum = tempsum + 1
	if tempsum > maxnum:
		maxnum = tempsum
		
file_object = open('guess.out', 'w')
file_object.write(str(maxnum)+'\n')
file_object.close()
