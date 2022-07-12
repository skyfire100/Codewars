count = 0
def persistence(n):
    global count
    if 0 <= n < 9:
        returnvalue = count
        count = 0
        return returnvalue
    else:
        count += 1
        answer = 1
        for x in str(n):
            answer *= int(x)
        return persistence(answer)