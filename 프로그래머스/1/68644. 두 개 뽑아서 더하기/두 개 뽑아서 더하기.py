def solution(numbers):
    answerSet = set()
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answerSet.add(numbers[i] + numbers[j])
        
    return sorted(list(answerSet))