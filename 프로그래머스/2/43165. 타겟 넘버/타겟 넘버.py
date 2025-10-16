def solution(numbers, target):
    return dfs(numbers, 0, target, 0)

def dfs(numbers, index, target, pre):
    cnt = 0
    if len(numbers) == index:
        if pre == target:
            return 1
        else:
            return 0
    else:
        cnt += dfs(numbers, index+1, target, pre + numbers[index])
        cnt += dfs(numbers, index+1, target, pre - numbers[index])
    return cnt