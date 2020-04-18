import sys
def move(i, j):
    global path
    
    maze[i][j] = 1
    temp_path.append((i, j))
    if i == N - 1 and j == N - 1:
        if len(path) == 0 or len(temp_path) < len(path):
            path = []
            path.extend(temp_path)
    if 0 <= i + 1 < N and not maze[i + 1][j]:
        move(i + 1, j)
    if 0 <= j + 1 < N and not maze[i][j + 1]:
        move(i, j + 1)
    if 0 <= i - 1 < N and not maze[i - 1][j]:
        move(i - 1, j)
    if 0 <= j - 1 < N and not maze[i][j - 1]:
        move(i, j - 1)

    temp_path.pop()
    maze[i][j] = 0



N = int(input())

maze = []
path = []
temp_path = []
for _ in range(N):
	a = sys.stdin.readline().strip('\n')
	a = a.split()
	for x in range(N):
		if a[x] == '1':
			a[x] = 0
		else:
			a[x] = 1
	maze.append(a)

move(0, 0)






print len(path) - 1
