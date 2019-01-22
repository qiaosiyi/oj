# coding=UTF-8
#桌上有倒置的三个坚果壳，其中一个下面有一个石头，两两交换坚果壳的位置，可以知道
#石头最终在哪里，猜对得一分，若开始不知道位置，现在给出交换位置和猜测位置，求能得到的最高分数。
#in:
#3
#1 2 1
#3 2 1
#1 3 1
#out:
#2
def next_position(before,a,b):#根据上一个位置和翻转数据，求下一个位置
	if before == a or before == b:
		if before == a:
			return b
		else:	
			return a
	return before

result = [0]*3
next_p = [0]*3
position = [0]*3
position[0] = 1
position[1] = 2
position[2] = 3
file_object = open('shell.in', 'rb')
flag = 1
for line in file_object:
	if flag:
		N = int(line)
		flag = 0
	else:
		a, b, g = map(int, line.split())
		for j in range(3):
			next_p[j] = next_position(position[j],a,b)
			if next_p[j] == g:#如果猜对了，分数记录加1
				result[j] = result[j] + 1
			position[j] = next_p[j]
aaaaa = max(result[0],result[1],result[2])#假设坚果的初始位置分别在1，2，3。
										#最后输出最大的那个假设所对应的分数值。
file_object = open('shell.out', 'w')
file_object.write(str(aaaaa)+'\n')
file_object.close()
