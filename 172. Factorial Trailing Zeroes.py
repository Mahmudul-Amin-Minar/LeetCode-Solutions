def trailingZeroes(n: int) -> int:
    count = 0
    while(n >= 5):
        n = n//5
        count += n
    return count

print(trailingZeroes(100))