def solution(string, ending):
    if string[-len(ending):] == ending or len(ending) == 0:
        return True
    return False