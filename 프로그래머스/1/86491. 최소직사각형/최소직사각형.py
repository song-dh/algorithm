def solution(sizes):
    h = 0
    w = 0
    for size in sizes:
        h = max(h, max(size))
        w = max(w, min(size))
    answer = h*w
    return answer