def accum(s):
    count = 0
    answer = ""
    for x in s:
        answer += s[count].upper()
        for i in range(count):
            answer += s[count].lower()
        count += 1
        if len(s) == count:
            return answer
        else:
            answer += "-"