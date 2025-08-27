def solution(s):
    length = len(s)
    middle = length // 2

    if length % 2 == 1:
        return s[middle]
    else:
        return s[middle-1:middle+1]