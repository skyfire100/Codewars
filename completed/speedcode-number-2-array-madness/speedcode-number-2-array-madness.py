def array_madness(a,b):
    a_answer = 0
    b_answer = 0
    for x in a:
        a_answer += x**2
    for x in b:
        b_answer += x**3
    if a_answer > b_answer:
        return True
    return False