def countBits(n: int):
    contains_ones = []
    for i in range(0, n+1):
        contains_ones.append(hammingWeight(i))

    return contains_ones

def hammingWeight(n: int):
    # Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
    c = 0
    while n:
        n = n & n-1
        c += 1
    return c

print(countBits(5))