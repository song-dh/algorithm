def solution(numbers):
    answer = []
    
    addList = [0 for _ in range(201)]
    maxNum = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            n = numbers[i] + numbers[j]
            addList[n] = 1
            if n > maxNum:
                maxNum = n
            
    for i in range(maxNum + 1):
        if addList[i]:
            answer.append(i)
        
    return answer