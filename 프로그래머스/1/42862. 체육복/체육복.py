def solution(n, lost, reserve):
    students = [1 for _ in range(n+2)]
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
    print(students[1:n+1])

    for index, value in enumerate(students):
        if value == 2:
            if students[index - 1] == 0:
                students[index] = 1
                students[index - 1] = 1
            elif students[index + 1] == 0:
                students[index] = 1
                students[index + 1] = 1
    print(students[1:n+1])
    answer = 0
    for s in students[1:n+1]:
        if s != 0:
            answer+=1
    return answer