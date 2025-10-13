import math

def solution(brown, yellow):
    a = []
    total = brown + yellow
    for i in range(2, int(math.sqrt(total)) + 1):
        if total % i == 0:
            if brown == (i + total//i) * 2 - 4:
                return [total//i, i]