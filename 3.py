def same_num(a,b):
	summ = 0
	for i in a:
		for j in b:
			if i == j:
				summ = summ + 1
	return summ


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
	for j in range(N):
		if i != j and i < j:
			tempsum = same_num(anm[i],anm[j]) + 1
	if maxnum < tempsum:
		maxnum = tempsum


file_object = open('guess.out', 'w')
file_object.write(str(maxnum)+'\n')
file_object.close()
