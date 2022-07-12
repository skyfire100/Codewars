def no_space(x):
    answer = ''
    for a in x:
        if a == " ":
            continue
        else:
            answer += a
    return answer