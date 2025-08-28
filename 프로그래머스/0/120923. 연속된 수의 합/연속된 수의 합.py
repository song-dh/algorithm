def solution(num, total):
    return [total // num - (num-1)//2 + n for n in range(num)]
    