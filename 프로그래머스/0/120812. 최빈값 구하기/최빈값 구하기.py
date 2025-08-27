def solution(array):
    numCount = {}
    answer = -1
    maxNum = -1
    
    for num in array:
        numCount[num] = numCount.get(num, 0) + 1
        if maxNum < numCount[num]:
            maxNum = numCount[num]
            answer = num
        elif maxNum == numCount[num]:
            answer = -1
    
    return answer