from collections import deque

m, n = map(int, input().split())
matrix = []
sx = 0
sy = 0
gx = 0
gy = 0
for num in range(n):
    ls = list(map(str, input().split(' ')))
    matrix.append(ls)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 's':
            sx = i
            sy = j
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'g':
            gx = i
            gy = j
depth = [[0] * m for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)]
q.append((sx, sy))
visited[sx][sy] = True
flag = False
while q:
    now = q.popleft()
    base_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for base in base_list:
        next = (now[0] + base[0], now[1] + base[1])
        try:
            if not visited[next[0]][next[1]] and matrix[next[0]][next[1]] == '0' and next[0] >= 0 and next[1] >= 0:
                visited[next[0]][next[1]] = True
                depth[next[0]][next[1]] = depth[now[0]][now[1]] + 1
                q.append(next)
            elif not visited[next[0]][next[1]] and matrix[next[0]][next[1]] == 'g' and next[0] >= 0 and next[1] >= 0:
                visited[next[0]][next[1]] = True
                depth[next[0]][next[1]] = depth[now[0]][now[1]] + 1
                flag = True
                break
        except:
            pass
if flag == True:
    print(depth[gx][gy])
else:
    print("Fail")