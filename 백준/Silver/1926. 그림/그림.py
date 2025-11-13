import sys 
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0
result = []
queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            result.append(1)
            queue.append((i, j))
            arr[i][j] = cnt + 2 
            while queue:
                a, b = queue.popleft()
                for k in range(4):
                    x, y = a + dx[k], b + dy[k]
                    if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
                        arr[x][y] = cnt + 2
                        queue.append((x, y))
                        result[cnt] += 1
            cnt += 1
if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)