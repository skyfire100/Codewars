def str_count(strng, letter):
    
    answer = 0
    
    for x in strng:
        if x == letter:
            answer += 1
            
    return answer