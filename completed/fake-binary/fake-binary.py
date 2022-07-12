def fake_bin(x):
    answer = ""
    for item in str(x):
        if int(item) >= 5:
            answer += "1"
        else:
            answer += "0"
    return answer