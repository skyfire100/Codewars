def solution(number):
    answer = []
    count = 0
    for num in range(number):
        if num % 3 ==0:
            answer.append(num)
        elif num % 5 == 0:
            answer.append(num)
    for x in answer:
        count += x
    return count