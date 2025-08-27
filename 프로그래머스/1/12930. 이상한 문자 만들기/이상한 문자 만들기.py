def solution(s):
    answer = ''
    count = 1
    for c in s:
        if not c.isalpha():
            answer += c
            count = 1
            continue
        if count % 2 == 0:
            answer += c.lower()
        else:
            answer += c.upper()
        count+=1
    return answer