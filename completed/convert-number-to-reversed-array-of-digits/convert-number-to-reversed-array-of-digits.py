def digitize(n):
    answer = []
    for x in str(n):
        answer.insert(0, int(x))
    return answer