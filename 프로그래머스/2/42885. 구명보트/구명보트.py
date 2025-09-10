import math

def solution(people, limit):
    answer = 0
    
    hList = []
    lList = []
    
    for p in people:
        if limit - 40 < p:
            answer += 1
        elif limit / 2 < p:
            hList.append(p)
        else:
            lList.append(p)
    
    hList.sort()
    lList.sort(reverse=True)
    
    hIndex = len(hList)
    lIndex = len(lList)
    while 1:
        print
        if hIndex <= 0 or lIndex <= 0:
            break
        if hList[hIndex - 1] + lList[lIndex - 1] <= limit:
            lIndex -= 1
        hIndex -= 1
        answer += 1
        
    answer += hIndex + math.ceil(lIndex / 2)
        

    return answer