def spin_words(sentence):
    answer = ''
    first = 0
    split = sentence.split()
    for x in split:
        if first != 0:
            answer += ' '
        first += 1
        if len(x) >= 5:
            answer += x[::-1]
        else:
            answer += x
    return answer