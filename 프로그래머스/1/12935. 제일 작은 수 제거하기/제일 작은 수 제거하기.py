def solution(arr):
    
    min = 2147000000
    indexArr = []
    for index, value in enumerate(arr):
        if min > value:
            min = value
            indexArr = [index]
        elif min == value:
            indexArr.append(index)
    
    for index in indexArr:
        arr.pop(index)
        
    if not arr:
        return [-1]
    return arr