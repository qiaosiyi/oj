def trans(k):
	temp = num[0]
	for i in range(k):
		num[i] = num[i + 1]
	num[k] = temp

def find_p(p1):
	k = N - 1
	if num[N - 1] < p1:
		return k
	k = k - 1
	for i in range(N):
		if num[N - 1 - i] > num[N - 1 - i - 1] and num[N - 1 - i - 1] > p1:
			k = k - 1
		else:
			return k

def done():
	for i in range(N - 1):
		if num[i] > num[i+1]:
			return 0
	return 1

file_object = open('sleepy.in', 'rb')
result = 0
flag = 1
for line in file_object:
	if flag:
		N = int(line)
		flag = 0
	else:
		num = map(int, line.split())
		while ~done():
			
			k = find_p(num[0])
			trans(k)
			result = result + k
			if done():
				#print result
				break

file_object = open('sleepy.out', 'w')
file_object.write(str(result)+'\n')
file_object.close()



	
