import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    minScoville = heapq.heappop(scoville)
    while minScoville < K:
        if len(scoville) < 1:
            answer = -1
            break
        heapq.heappush(scoville, minScoville + heapq.heappop(scoville)*2)
        minScoville = heapq.heappop(scoville)
        answer += 1
    
    return answer