def pig_it(text):
    answer = ''
    split_text = text.split(" ")
    for word in split_text:
        if word.isalpha():
            answer += word[1:]
            answer += f'{word[0]}ay '
        else:
            answer += word
    if answer[-1] == ' ':
        return answer[:-1]
    return answer