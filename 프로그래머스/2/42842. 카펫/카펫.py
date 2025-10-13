import math

def solution(brown, yellow):
    total = brown + yellow
    for h in range(2, int(math.sqrt(total)) + 1):
        if total % h == 0 and brown == (h + total//h) * 2 - 4:
                return [total//h, h]