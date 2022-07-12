def century(year):
    if str(year)[-2:] == "00":
        return int(year/100)
    return int((year/100)+1)