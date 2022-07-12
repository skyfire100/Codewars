def disemvowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    answer = ''
    for x in string:
        if x in vowel:
            continue
        answer += x
    return answer