def first_non_consecutive(arr):
    prev_number = arr[0]
    for x in arr[1:]:
        if x-1 != prev_number:
            return x
        prev_number = x
    return None