def solution(phone_book):
    pb = {}
    for s in phone_book:
        p = pb
        end = len(s) -  1
        for i, c in enumerate(s):
            if c in p:
                if end == i or 'x' in p[c]:
                    return False
            else:
                if end != i:
                    p[c] = {}
                else:
                    p[c] = {'x':''}
            p = p[c]
    return True