def solution(s):
    answerList = []
    for x in s:
        if x.isupper():
            answerList.append(f" {x}")
        else:
            answerList.append(x)
    return ''.join(answerList)