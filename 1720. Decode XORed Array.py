def decode(encoded, first: int):
    arr = []
    arr.append(first)
    
    i = 0
    for el in encoded:
        arr.append(arr[i]^el)
        i += 1
    return arr