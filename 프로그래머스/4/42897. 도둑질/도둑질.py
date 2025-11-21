def solution(money):
    a = [money[0], money[1], money[0] + money[2]]
    b = [0, money[1], money[2]]

    for m in range(3, len(money)):
        a.append(max(a[m-3], a[m-2]) + money[m])
        b.append(max(b[m-3], b[m-2])  + money[m])
    return max(max(a[:-1]), max(b))