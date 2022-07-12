def count_positives_sum_negatives(arr):
    positive = 0
    negitive = 0
    if len(arr) == 0:
        return []
    for x in arr:
        if x > 0:
            positive += 1
        else:
            negitive += x
    return [positive, negitive]