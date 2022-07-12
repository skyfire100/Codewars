def sum_even_numbers(seq):
    answer = 0
    for x in seq:
        if x %2 == 0:
            answer += x
    return answer