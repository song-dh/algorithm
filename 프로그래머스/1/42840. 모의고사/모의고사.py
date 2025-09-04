def solution(answers):
    s1AnswerList = [1, 2, 3, 4, 5]
    s2AnswerList = [2, 1, 2, 3, 2, 4, 2, 5]
    s3AnswerList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1 = s2 = s3 = 0
    for i, v in enumerate(answers):
        if s1AnswerList[i%5] == v:
            s1 += 1
        if s2AnswerList[i%8] == v:
            s2 += 1
        if s3AnswerList[i%10] == v:
            s3 += 1
        
    scores = [s1, s2, s3]
    m = max(scores)
    return [i + 1 for i, v in enumerate(scores) if m == v]
