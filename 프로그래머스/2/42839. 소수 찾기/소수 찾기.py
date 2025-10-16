import math
def solution(numbers):
    numSet = set()
    getAllNum('', numbers, numSet)
    
    answer = set()
    for num in numSet:
        if isPrimeNumber(num):
            answer.add(num)
    print(answer)
    return len(answer)

def isPrimeNumber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: 
            return False
    return True 
    
def getAllNum(current, remaining, result):
    if current and int(current) > 1:
        result.add(int(current))
    for i in range(len(remaining)):
        getAllNum(current + remaining[i], remaining[:i] + remaining[i+1:], result)
