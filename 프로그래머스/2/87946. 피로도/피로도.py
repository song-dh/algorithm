def solution(k, dungeons):
    visit = [0 for _ in range(len(dungeons))]
    return go(k, dungeons, 0, visit)

def go(k, dungeons, m, visit):
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visit[i] == 0:
            visit[i] = 1
            k -= dungeons[i][1]
            m = max(go(k, dungeons, m, visit), sum(visit))
            visit[i] = 0
            k += dungeons[i][1]
    return m