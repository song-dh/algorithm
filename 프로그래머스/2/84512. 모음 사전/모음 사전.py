def solution(word):
    m = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    
    for i, char in enumerate(word):
        weight = sum(5**j for j in range(5-i))
        answer += m[char] * weight + 1
    
    return answer

print(solution('EIO'))