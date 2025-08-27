def solution(s):
    answer = ''
    asciiArr = []
    for c in s:
        asciiArr.append(ord(c))
    asciiArr.sort(reverse=True)
    for a in asciiArr:
        answer += chr(a)
    return answer