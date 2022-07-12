def create_phone_number(n):
    answer = ""
    for x in n:
        answer += str(x)
    return f"({answer[0:3]}) {answer[3:6]}-{answer[6:]}"