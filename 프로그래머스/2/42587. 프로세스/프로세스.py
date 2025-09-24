from collections import deque

def solution(priorities, location):
    answer = 0
    maxPri = max(priorities)

    priorities = deque(list(enumerate(priorities)))
    
    cnt = 0
    
    while 1:
        currunt = priorities[0]
        if currunt[1] == maxPri:
            cnt += 1
            if currunt[0] == location:
                break
            priorities.popleft()
            maxPri = max(priorities, key=lambda x: x[1])[1]

        else:
            priorities.append(priorities.popleft())
            
    
    return cnt