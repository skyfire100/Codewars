def digital_root(n):
    if 0 <= n <= 9:
        return n
    else:
        answer = 0
        for x in str(n):
            answer += int(x)
        return digital_root(answer)