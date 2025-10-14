def solution(k, dungeons):
    return len(dungeons) - go(k, dungeons, len(dungeons))

def go(k, dungeons, m):
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            temp = dungeons.pop(i)
            if not dungeons:
                m = 0
            k -= temp[1]
            m = min(m, go(k, dungeons, m))
            dungeons.insert(i, temp)
            k += temp[1]
        else:
            m = min(m, len(dungeons))
    return m