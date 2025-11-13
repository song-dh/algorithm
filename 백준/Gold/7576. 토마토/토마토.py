import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

days = 0
queue = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append((i, j))

length = len(queue)
while queue:
    if length == 0:
        length = len(queue)
        days += 1
    a, b = queue.popleft()
    length -= 1
    for k in range(4):
        x, y = a + dx[k], b + dy[k]
        if 0 <= x < m and 0 <= y < n and arr[x][y] == 0:
            arr[x][y] = 1
            queue.append((x, y))
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            days = -1
print(days)
