def solution(prices):
    answer = [0 for _ in prices]
    
    stack = []
    
    for price in enumerate(prices):
        while stack and stack[-1][1] > price[1]:
            index = stack.pop()
            index = index[0]
            answer[index] = price[0] - index
        stack.append(price) 
    
    for index, value in stack:
        answer[index] = stack[-1][0] - index
        
    return answer