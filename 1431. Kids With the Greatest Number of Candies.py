def kidsWithCandies(candies, extraCandies: int):
    max_ = max(candies)
    greatest = []
    for candy in candies:
        if candy+extraCandies >= max_:
            greatest.append(True)
        else:
            greatest.append(False)
    return greatest