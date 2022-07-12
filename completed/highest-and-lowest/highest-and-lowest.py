def high_and_low(numbers):
    the_numbers_in_a_list = numbers.split(" ")
    highest = the_numbers_in_a_list[0]
    lowest = the_numbers_in_a_list[0]
    for x in range(len(the_numbers_in_a_list)):
        if int(the_numbers_in_a_list[x]) > int(highest):
            highest = the_numbers_in_a_list[x]
        if int(the_numbers_in_a_list[x]) < int(lowest):
            lowest = the_numbers_in_a_list[x]
    return f"{highest} {lowest}"