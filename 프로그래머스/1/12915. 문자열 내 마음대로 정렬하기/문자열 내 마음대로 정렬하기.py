def solution(strings, n):
    stringDict = {}
    
    for s in strings:
        indexChar = s[n]
        arr = stringDict.get(indexChar, [])
        arr.append(s)
        stringDict[indexChar] = arr
    
    answer = []
    for key in sorted(stringDict.keys()):
        stringDict[key].sort()
        answer = answer + stringDict[key]  
        
    return answer