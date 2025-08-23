def solution(num_list, n):
    list_size = len(num_list)
    answer = [[0] * n for _ in range(list_size//n) ]
    for index, value in enumerate(num_list):
        answer[index // n][index % n] = value;
    return answer