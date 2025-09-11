def solution(name):
    answer = 0
    for s in name:
        answer += getCount(s)
    
    longAStart = 0
    longAEnd = 0
    length = 0
    aStart = -1
    aLength = 0
    
    for i, char in enumerate(name):
        if char == 'A':
            if aStart == -1:
                aStart = i
            aLength += 1
        else:
            if aStart != -1:
                if aLength > length:
                    longAStart = aStart
                    longAEnd = i - 1
                    length = aLength

                aStart = -1
                aLength = 0
    if aStart != -1:  
        if aLength >= length - 1:
            longAStart = aStart
            longAEnd = len(name) - 1
            length = aLength
    if length == len(name):
        return answer
    elif longAStart == 0:
        return answer + len(name) - 1 - longAEnd 
    elif longAEnd == len(name) - 1:
        return answer + longAStart - 1
    elif length == 0:
        return answer + len(name) - 1
    elif length == 1:
        return answer + min(len(name) - 1, longAStart + len(name) - longAEnd - 2 + min((longAStart - 1), (len(name) - 1 - longAEnd)))
    moves = longAStart + len(name) - longAEnd - 2 + min((longAStart - 1), (len(name) - 1 - longAEnd))
    return answer + moves

def getCount(c):
    return min(ord(c) - ord("A"), 26 - ord(c) + ord("A"))