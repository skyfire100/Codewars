def generate_hashtag(s):
    answer = "#"
    if len(s) < 1:
        return False
    x = s.split(" ")
    for words in x:
        answer += words.capitalize()
    if len(answer) > 140:
        return False
    return answer
    