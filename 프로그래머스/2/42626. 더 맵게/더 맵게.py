from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    overK = 0
    q = PriorityQueue() 
    for s in scoville:
        if s > K:
            if overK == 2:
                continue
            overK += 1
        q.put(s)
    minScoville = q.get()
    while minScoville < K:
        if q.qsize() < 1:
            answer = -1
            break
        q.put(minScoville + q.get()*2)
        minScoville = q.get()
        answer += 1
    
    return answer