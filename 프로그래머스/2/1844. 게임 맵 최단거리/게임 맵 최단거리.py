from collections import deque

def solution(maps):
    arrows = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n = len(maps)
    m = len(maps[0])
    maps = [[0] * m] + maps + [[0] * m]
    maps = [[0] + i + [0] for i in maps]
    
    Q = deque([(1, 1)])
    maps[1][1] = 2
    while not len(Q) == 0:
        x, y = Q.popleft()
        if x == n and y == m:
            return maps[n][m] - 1
        for i, j in arrows:
            if maps[x+i][y+j] == 1:
                maps[x+i][y+j] = maps[x][y] + 1
                Q.append((x+i, y+j))
    
    return -1
