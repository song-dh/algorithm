def solution(my_string):
    answer = 0
    num = 0
    for s in my_string:
        if s.isdecimal():
            num = num * 10 + int(s)
            print(num)
        elif num:
            answer += num
            num = 0
    return answer + num
