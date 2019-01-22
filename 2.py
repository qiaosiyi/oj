# coding=UTF-8
#奶牛排队，控制第一个向后插入，然后按从小到大的编号排好，求需要插入的最小次数
#in：
#4
#1 2 4 3
#out：
#3
# basic idea:
#若遇到最大数字，直接放到最后面；然后，
#当前数字应放到比他大的数字后面，且放到从最后往前数单调递减的最后一个比他大的数字前面。
#这样可以保证从小到大的顺序。

def trans(k):
	temp = num[0]
	for i in range(k):
		num[i] = num[i + 1]
	num[k] = temp

def find_p(p1):#找到从最后往前数单调递减的最后一个比跪一个数字大的位置。且，如果是最大数字，则放到最后面。即，k。
	k = N - 1
	if num[N - 1] < p1:
		return k
	k = k - 1
	for i in range(N):
		if num[N - 1 - i] > num[N - 1 - i - 1] and num[N - 1 - i - 1] > p1:
			k = k - 1
		else:
			return k

def done():#判断是否排好，排好返回真
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
		if done():
			break
		while ~done():
			
			k = find_p(num[0])
			trans(k)
			result = result + 1
			if done():
				#print result
				break

file_object = open('sleepy.out', 'w')
file_object.write(str(result)+'\n')
file_object.close()



	
