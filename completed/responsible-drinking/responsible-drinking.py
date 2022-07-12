def hydrate(drink_string): 
    count = 0
    for x in drink_string:
        try:
            int(x)
            count += int(x)
        except:
            pass
    if count > 1:
        return f"{count} glasses of water"
    else:
        return f"{count} glass of water"