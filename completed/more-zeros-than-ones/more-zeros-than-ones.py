def more_zeros(s):
    answer = []
    for l in s:
        count = 0
        for x in str(bin(ord(l))[2:]):
            if x == "1":
                count += 1
            else:
                count -= 1
        if count < 0:
            if answer.count(l) == 0:
                answer.append(l)
    return answer
        
            