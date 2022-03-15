def finalValueAfterOperations(operations) -> int:
    x = 0
    for str_ in operations:
        if str_ in ["X++","++X"]:
            x += 1
        if str_ in ["X--","--X"]:
            x -= 1
    return x