def xo(string):
    count = 0
    for letter in string:
        if letter.upper() == 'X':
            count -= 1
        elif letter.upper() == 'O':
            count += 1
    if count == 0:
        return True
    return False