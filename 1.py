# coding=UTF-8
def next_position(before,a,b):
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
			if next_p[j] == g:
				result[j] = result[j] + 1
			position[j] = next_p[j]
aaaaa = max(result[0],result[1],result[2])
										
file_object = open('shell.out', 'w')
file_object.write(str(aaaaa)+'\n')
file_object.close()
