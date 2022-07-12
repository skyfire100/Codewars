def assemble(arr):
    answer = ""
    if arr == []:
        return answer
    for char in arr[0]:
        if char == "*":
            for a in range(1, len(arr)):
                if arr[a][len(answer)] != "*":
                    answer += arr[a][len(answer)]
                    break
                elif a == (len(arr) - 1):
                    answer += '#'
        else:
            answer += char
    return answer