def sabb(s, val, happiness):
    answer = val + happiness
    sabticl = ["s", "a", "b", "t", "i", "c", "l"]
    for letter in s:
        if letter.lower() in sabticl:
            answer += 1 
    if answer > 22:
        return "Sabbatical! Boom!"
    return "Back to your desk, boy."