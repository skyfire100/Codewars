def positive_sum(arr):
    ans = 0
    for x in arr:
        if x >= 0:
            ans += x
    return ans