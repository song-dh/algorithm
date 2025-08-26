def solution(s, n):
    answer = ''
    for c in s:
        if c.isupper():
            c = chr(ord('A') + (ord(c) - ord('A') + n) % 26)
        elif c.islower():
            c = chr(ord('a') + (ord(c) - ord('a') + n) % 26)
        answer += c

    return answer