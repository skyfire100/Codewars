def alphabet_position(text):
    answer = ""
    for x in text:
        if x.isupper():
            answer += f"{(ord(x) - 64)} "
        elif x.islower():
            answer += f"{ord(x) - 96} "
        else:
            continue
    return answer[:-1]