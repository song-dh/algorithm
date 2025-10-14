def solution(k, dungeons):
    visit = [0 for _ in range(len(dungeons))]
    return go(k, dungeons, 0, visit)

def go(k, dungeons, cnt, visit):
    m = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visit[i] == 0:
            visit[i] = 1
            m = max(go(k - dungeons[i][1], dungeons, cnt + 1, visit), m)
            visit[i] = 0
    return m